extends Node2D

const GRID_SIZE = 16
const grassDecorationIds = [0, 1, 2, 3, 4, 5, 6, 7]
const treeDecorationIds = [8, 9, 10, 11]
const stoneDecorationIds = [12, 13, 14, 15, 16]
const mushroomDecorationIds = [17, 18, 19, 20, 21, 22, 23, 24]
var explosionEffect = preload("res://ExplosionEffect.tscn")

var thread: Thread
var wall_positions: PoolVector2Array = []
var crate_prefab = preload("res://Crate.tscn")
var target_prefab = preload("res://Target.tscn")

var game_over := false

onready var crates = $LevelContainer/Crates
onready var player = $LevelContainer/Player
onready var targets = $LevelContainer/Targets
onready var walls = $LevelContainer/Walls
onready var floors = $LevelContainer/Floors
onready var timer = $Timer
onready var others = $LevelContainer/Others
onready var cam = $LevelContainer/Player/Camera2D
var consol

var current_level := ""
onready var tilemaps = [walls, others, floors]
var just_started = true

var level_size = Vector2(0, 0)

signal game_over
signal level_completed(completed)
signal level_reset
signal level_made


func _ready():
	player.connect("level_reset_requested", self, "_on_Player_level_reset_requested")
	thread = Thread.new()
	reset_time()


func reset_time():
	MainInstances.stopwatch.reset()
	player.started = false


func start_stopwatch():
	MainInstances.stopwatch.start()


func load_level(level: String, decorate = true):
	$LevelContainer/Walls.modulate = Color.white
	$LevelContainer/Player/RayCast2D.set_collision_mask_bit(0, true)
	if thread.is_alive():
		return
	if thread.is_active():
		thread.wait_to_finish()
	reset_time()
	consol = MainInstances.console
	if decorate:
		consol.Log("Generating level " + level, .5, .5)
	SaveLoad.files.level.data.current_level = level
	SaveLoad.save("level")
	thread.start(self, "level_load", [level, decorate])


func level_load(level: Array):
	just_started = true
	player.set_moves(0)
	current_level = level[0]
	call_deferred("_reset_level", level[1])


func _exit_tree():
	if thread.is_active():
		thread.wait_to_finish()


func _reset_level(decorate):
	game_over = false
	player.initialize()
	delete_children(crates)
	if decorate:
		walls.clear()
		others.clear()
		delete_children(floors)
		delete_children(targets)

	if current_level == "":
		return

	var file = File.new()
	file.open("res://Levels/%s.sokolvl" % current_level, File.READ)

	var version = 0
	var row = 0
	var player_pos
	level_size = Vector2(0, 0)

	while !file.eof_reached():
		var line = file.get_line()
		if line.begins_with(";"):
			var meta = line.split(": ", false, 1)
			if meta[0] == ";version":
				version = int(meta[1])
		elif line != "":
			if version != 1:
				push_error("Not supported .sokolvl version: " + str(version))
				return
			var col = 0

			for x in line:
				var tile_pos = Vector2(col, row) * GRID_SIZE

				if x == "#":
					if decorate:
						add_wall(tile_pos)
				if x in [".", "X", "O", "@", "%", "A"]:
					if decorate:
						add_floor(tile_pos)
				if x in ["@", "A"]:
					player_pos = tile_pos
				if x in ["X", "%"]:
					add_crate(tile_pos)
				if x in ["O", "%", "A"]:
					if decorate:
						add_target(tile_pos)

				col += 1
			row += 1
			level_size.y += 1
			level_size.x = max(level_size.x, col)

	file.close()

	$CanvasLayer/HUD/LevelLabel.text = "Level = %s" % current_level

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
		cam, "zoom", cam.zoom, new_zoom, 2, Tween.TRANS_LINEAR, Tween.EASE_IN_OUT
	)
	$Tween.start()
	timer.start(2)
	if decorate:
		decorate(-50, 50)
	initialize_player(player_pos)
	Utils.unload_loading_screen()
	yield(timer, "timeout")
	just_started = false
	emit_signal("level_made")
	return


static func delete_children(node):
	for n in node.get_children():
		node.remove_child(n)
		n.queue_free()


func decorate(x, y):
	for tile in check_for_empty_tile(Vector2(x, y)):
		match randi() % 101:
			1:
				add_mushroom(tile)
			2:
				add_rock(tile)
			3:
				add_tree(tile)


func _on_Crate_target_updated():
	var crates_in_place = 0

	for crate in crates.get_children():
		if crate.target_count > 0:
			crates_in_place += 1

	if crates_in_place == crates.get_child_count():
		emit_signal("level_completed")


func _on_Player_level_reset_requested():
	if player.tween.is_active():
		yield(player.tween, "tween_all_completed")
	load_level(current_level, false)
	emit_signal("level_reset")


func _on_Crate_game_over():
	if not game_over:
		game_over = true
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
	wall_positions.append(tile_pos)
	walls.set_cellv(tile_pos / 16, 1)
	walls.update_bitmask_area(tile_pos / 16)


func check_for_empty_tile(size: Vector2 = Vector2(-75, 75)):
	var empty_tiles: PoolVector2Array = []
	for x in range(size.x, size.y):
		for y in range(size.x, size.y):
			var tile_pos = Vector2(x, y)
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
			var tile_positions = [
				down_left_tile_pos,
				down_right_tile_pos,
				lower_tile_pos,
				left_tile_pos,
				right_tile_pos,
				up_tile_pos,
				tile_pos
			]
			var count2 := 0
			for tile in tile_positions:
				var count := 0
				for tilemap in tilemaps:
					if empty(tilemap, tile):
						count += 1
						if count == tilemaps.size():
							count2 += 1
							if count2 == tile_positions.size():
								empty_tiles.append(tile_pos)
	return empty_tiles


func empty(tilemap, tile) -> bool:
	if tilemap.get_cellv(tile) != -1:
		return false
	return true


func add_tree(tile):
	others.set_cellv(tile, treeDecorationIds[randi() % treeDecorationIds.size()])


func add_rock(tile):
	others.set_cellv(tile, stoneDecorationIds[randi() % stoneDecorationIds.size()])


func add_mushroom(tile):
	others.set_cellv(tile, mushroomDecorationIds[randi() % mushroomDecorationIds.size()])


func explode_walls():
	for positions in wall_positions:
		Utils.instance_scene_on_main(positions, explosionEffect)


func _on_Player_won():
	emit_signal("level_completed", true)
