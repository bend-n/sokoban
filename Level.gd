extends Node2D

const GRID_SIZE = 16

var wall_prefab = load("res://Wall.tscn")
var floor_prefab = load("res://Floor.tscn")
var crate_prefab = load("res://Crate.tscn")
var target_prefab = load("res://Target.tscn")

onready var cam = $LevelContainer/Player/Camera2D

var current_level := ""

var just_started = true setget set_just_started

var level_size = Vector2(0, 0)

signal game_over()
signal level_completed()
signal level_reset()

onready var timer = $Timer

func _ready():
	$LevelContainer/Player.connect("level_reset_requested", self, "_on_Player_level_reset_requested")

func load_level(level: String):
	$LevelContainer/Player.set_moves(0)
	current_level = level
	_reset_level()

func set_just_started(new_start):
	just_started = new_start
	timer.start(.5)
	yield($Timer, "timeout")
	just_started = false

func _reset_level():
	delete_children($LevelContainer/Walls)
	delete_children($LevelContainer/Floors)
	delete_children($LevelContainer/Crates)
	delete_children($LevelContainer/Targets)
	
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
					var wall = wall_prefab.instance()
					wall.position = tile_pos
					$LevelContainer/Walls.add_child(wall)
				
				if x in ['.', 'X', 'O', '@', '%', 'A']:
					var flr = floor_prefab.instance()
					flr.position = tile_pos
					$LevelContainer/Floors.add_child(flr)
				
				if x in ['@', 'A']:
					$LevelContainer/Player.position = tile_pos
					$LevelContainer/Player.world = get_parent()
				
				if x in ['X', '%']:
					var crate = crate_prefab.instance()
					crate.position = tile_pos
					crate.main = get_parent()
					crate.connect("target_updated", self, "_on_Crate_target_updated")
					crate.connect("game_over_detected", self, "_on_Crate_game_over")
					$LevelContainer/Crates.add_child(crate)
				
				if x in ['O', '%', 'A']:
					var target = target_prefab.instance()
					target.position = tile_pos
					$LevelContainer/Targets.add_child(target)
				
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
	
	$LevelContainer/Player/Camera2D.zoom = new_zoom
	set_just_started(true)

static func delete_children(node):
	for n in node.get_children():
		node.remove_child(n)
		n.queue_free()

func _on_Crate_target_updated():
	var crates_in_place = 0
	
	for crate in $LevelContainer/Crates.get_children():
		if crate.target_count > 0:
			crates_in_place += 1
	
	if crates_in_place == $LevelContainer/Crates.get_child_count():
		emit_signal("level_completed")

func _on_Player_level_reset_requested():
	_reset_level()
	emit_signal("level_reset")

func _on_Crate_game_over():
	emit_signal("game_over")
