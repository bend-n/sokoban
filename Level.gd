extends Node2D

const GRID_SIZE = 16
const grassDecorationIds = [0, 1, 2, 3, 4, 5, 6, 7]
const treeDecorationIds = [8, 9, 10, 11]

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
var just_started = true setget set_just_started

var level_size = Vector2(0, 0)

signal game_over()
signal level_completed()
signal level_reset()

func _ready():
	player.connect("level_reset_requested", self, "_on_Player_level_reset_requested")
	thread = Thread.new()

func load_level(level: String):
	thread.start(self, "level_load", level)

func level_load(level : String):
	set_just_started(true)
	player.set_moves(0)
	current_level = level
	_reset_level()

func _exit_tree():
	thread.wait_to_finish()

func set_just_started(new_start):
	just_started = new_start

func _reset_level():
	walls.clear()
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
				if x in ['X', '%']:
					add_crate(tile_pos)
				if x in ['O', '%', 'A']:
					add_target(tile_pos)
				
				col += 1
			row += 1
			level_size.y += 1
			level_size.x = max(level_size.x, col)
			
	file.close()

	for x in range(-50, 50):
		for y in range(-50, 50):
			if check_for_empty_tile(Vector2(x, y), tilemaps):
				if randi() % 11 == 5:
					others.set_cell(x, y, treeDecorationIds[randi() % treeDecorationIds.size()])
	
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
	
	cam.zoom = new_zoom
	timer.start(2)
	yield(timer, "timeout")
	set_just_started(false)

static func delete_children(node):
	for n in node.get_children():
		node.remove_child(n)
		n.queue_free()

func _on_Crate_target_updated():
	var crates_in_place = 0
	
	for crate in crates.get_children():
		if crate.target_count > 0:
			crates_in_place += 1
	
	if crates_in_place == crates.get_child_count():
		emit_signal("level_completed")

func _on_Player_level_reset_requested():
	_reset_level()
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
#	var flr = floor_prefab.instance()
#	flr.position = tile_pos
#	floors.add_child(flr)
	floors.set_cellv(tile_pos / 16, 0)
	randomize()
	if randi() % 5 == 2:
		others.set_cellv(tile_pos / 16, grassDecorationIds[randi() % grassDecorationIds.size()])

func add_wall(tile_pos):
	walls.set_cellv(tile_pos / 16, 1)
	walls.update_bitmask_area(tile_pos / 16)

func check_for_empty_tile(tile_pos : Vector2, tilemaps : Array) -> bool:
	for tilemap in tilemaps:
		var lower_tile_pos = tile_pos
		var left_tile_pos = tile_pos
		var right_tile_pos = tile_pos
		var up_tile_pos = tile_pos
		lower_tile_pos += Vector2.DOWN
		left_tile_pos += Vector2.LEFT
		right_tile_pos += Vector2.RIGHT
		up_tile_pos += Vector2.UP
		var tile_positions = [lower_tile_pos, left_tile_pos, right_tile_pos, up_tile_pos, tile_pos]
		for tile in tile_positions:
			if tilemap.get_cellv(tile) != -1:
				return false
	return true
