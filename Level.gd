extends Node2D

const GRID_SIZE = 16
const grassDecorationIds = [0, 1, 2, 3, 4, 5, 6, 7]
const treeDecorationIds = [8, 9, 10, 11]
const stoneDecorationIds = [12, 13, 14, 15, 16]
const mushroomDecorationIds = [17, 18, 19, 20, 21, 22, 23, 24]

var thread : Thread
var crate_prefab = preload("res://Crate.tscn")
var target_prefab = preload("res://Target.tscn")

onready var crates = $LevelContainer/Crates
onready var player = $LevelContainer/Player
onready var targets = $LevelContainer/Targets
onready var walls = $LevelContainer/Walls
onready var floors = $LevelContainer/Floors
onready var timer = $Timer
onready var others = $LevelContainer/Others
onready var cam = $LevelContainer/Player/Camera2D

var current_level := ""
onready var tilemaps = [walls, others, floors]
var just_started = true

var level_size = Vector2(0, 0)

signal game_over()
signal level_completed()
signal level_reset()

func _ready():
	player.connect("level_reset_requested", self, "_on_Player_level_reset_requested")
	thread = Thread.new()
	reset_time()

func reset_time():
	$CanvasLayer/HUD/StopWatch.time_elapsed = 0.0
	$CanvasLayer/HUD/StopWatch.set_process(false)
	print("attempting to reset, remaining time: %s" % $CanvasLayer/HUD/StopWatch.time_elapsed)
	return true

func start_stopwatch():
	$CanvasLayer/HUD/StopWatch.set_process(true)

func load_level(level: String, decorate = true):
	print("thread alive? ", thread.is_alive(), " | thread active? ", thread.is_active())
	if thread.is_alive():
		return
	if thread.is_active():
		thread.wait_to_finish()
	print(reset_time())
	print("attempting to load level %s" % level)
	thread.start(self, "level_load", [level, decorate])

func level_load(level : Array):
	print("loading level %s" % level[0])
	just_started = true
	player.set_moves(0)
	current_level = level[0]
	call_deferred("_reset_level", level[1])

func _exit_tree():
	thread.wait_to_finish()

func _reset_level(decorate):
	walls.clear()
	if decorate:
		others.clear()
	delete_children(floors)
	delete_children(crates)
	delete_children(targets)
	
	if current_level == "":
		return
	
	var file = File.new()
	file.open("res://Levels/%s.sokolvl" % current_level, File.READ)
	
	var version = 0
	var row = 0
	level_size = Vector2(0, 0)
	
	while !file.eof_reached():
		var line = file.get_line()
		if line.begins_with(";"):
			var meta = line.split(': ', false, 1)
			if meta[0] == ';version':
				version = int(meta[1])
		elif line != '':
			if version != 1:
				push_error("Not supported .sokolvl version: " + str(version))
				return
			var col = 0
			
			for x in line:
				var tile_pos = Vector2(col, row) * GRID_SIZE
				
				if x == '#':
					add_wall(tile_pos)
				if x in ['.', 'X', 'O', '@', '%', 'A']:
					add_floor(tile_pos)
				if x in ['@', 'A']:
					initialize_player(tile_pos)
					player.initialize()
				if x in ['X', '%']:
					add_crate(tile_pos)
				if x in ['O', '%', 'A']:
					add_target(tile_pos)
				
				col += 1
			row += 1
			level_size.y += 1
			level_size.x = max(level_size.x, col)
			
	file.close()

	$CanvasLayer/HUD/LevelLabel.text = "Level = %s" %current_level

	var new_zoom = .5
	new_zoom = clamp(new_zoom, get_parent().min_zoom, get_parent().max_zoom)
	new_zoom = Vector2(new_zoom, new_zoom)
	var level_int
	if level_size.x > level_size.y:
		level_int = level_size.x
	else:
		level_int = level_size.y
	
	new_zoom += Vector2(level_int / 45, level_int / 45)
	$Tween.interpolate_property(
		cam,
		"zoom",
		cam.zoom,
		new_zoom,
		2,
		Tween.TRANS_LINEAR,
		Tween.EASE_IN_OUT
	)
	$Tween.start()
	timer.start(2)
	if decorate:
		decorate(-75, 75)
	yield(timer, "timeout")
	just_started = false
	return

static func delete_children(node):
	for n in node.get_children():
		node.remove_child(n)
		n.queue_free()

func decorate(x, y):
	add_trees(x, y)
	add_rock(x, y)
	add_mushroom(x, y)

func _on_Crate_target_updated():
	var crates_in_place = 0
	
	for crate in crates.get_children():
		if crate.target_count > 0:
			crates_in_place += 1
	
	if crates_in_place == crates.get_child_count():
		emit_signal("level_completed")

func _on_Player_level_reset_requested():
	load_level(current_level, false)
	emit_signal("level_reset")

func _on_Crate_game_over():
	emit_signal("game_over")

func add_target(tile_pos):
	var target = target_prefab.instance()
	target.main = self
	target.position = tile_pos
	targets.add_child(target)

func add_crate(tile_pos):
	var crate = crate_prefab.instance()
	crate.position = tile_pos
	crate.main = get_parent()
	crate.connect("target_updated", self, "_on_Crate_target_updated")
	crate.connect("game_over_detected", self, "_on_Crate_game_over")
	crates.add_child(crate)

func initialize_player(tile_pos):
	player.position = tile_pos
	player.world = get_parent()

func add_floor(tile_pos):
	floors.set_cellv(tile_pos / 16, 0)
	randomize()
	if randi() % 5 == 2:
		others.set_cellv(tile_pos / 16, grassDecorationIds[randi() % grassDecorationIds.size()])

func add_wall(tile_pos):
	walls.set_cellv(tile_pos / 16, 1)
	walls.update_bitmask_area(tile_pos / 16)

func check_for_empty_tile(tile_pos : Vector2) -> bool:
	for tilemap in tilemaps:
		var lower_tile_pos = tile_pos
		var left_tile_pos = tile_pos
		var right_tile_pos = tile_pos
		var up_tile_pos = tile_pos
		var down_right_tile_pos = tile_pos
		var down_left_tile_pos = tile_pos
		down_right_tile_pos += Vector2.DOWN + Vector2.RIGHT
		down_left_tile_pos += Vector2.DOWN + Vector2.LEFT
		lower_tile_pos += Vector2.DOWN
		left_tile_pos += Vector2.LEFT
		right_tile_pos += Vector2.RIGHT
		up_tile_pos += Vector2.UP
		var tile_positions = [down_left_tile_pos, down_right_tile_pos, lower_tile_pos, left_tile_pos, right_tile_pos, up_tile_pos, tile_pos]
		for tile in tile_positions:
			if tilemap.get_cellv(tile) != -1:
				return false
	return true

func add_trees(size1, size2):
	for x in range(size1, size2):
			for y in range(size1, size2):
				if check_for_empty_tile(Vector2(x, y)):
					if randi() % 100 == 5:
						others.set_cell(x, y, treeDecorationIds[randi() % treeDecorationIds.size()])

func add_rock(size1, size2):
	for x in range(size1, size2):
			for y in range(size1, size2):
				if check_for_empty_tile(Vector2(x, y)):
					if randi() % 75 == 5:
						others.set_cell(x, y, stoneDecorationIds[randi() % stoneDecorationIds.size()])

func add_mushroom(size1, size2):
	for x in range(size1, size2):
			for y in range(size1, size2):
				if check_for_empty_tile(Vector2(x, y)):
					if randi() % 75 == 5:
						others.set_cell(x, y, mushroomDecorationIds[randi() % mushroomDecorationIds.size()])
