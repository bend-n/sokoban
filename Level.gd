extends Node2D

const GRID_SIZE = 16

var wall_prefab = load("res://Wall.tscn")
var floor_prefab = load("res://Floor.tscn")
var crate_prefab = load("res://Crate.tscn")
var target_prefab = load("res://Target.tscn")

onready var crates = $LevelContainer/Crates
onready var player = $LevelContainer/Player
onready var targets = $LevelContainer/Targets
onready var walls = $LevelContainer/Walls
onready var floors = $LevelContainer/Floors

onready var cam = $LevelContainer/Player/Camera2D

var current_level := ""

var just_started = true setget set_just_started

var level_size = Vector2(0, 0)

signal game_over()
signal level_completed()
signal level_reset()

onready var timer = $Timer

func _ready():
	player.connect("level_reset_requested", self, "_on_Player_level_reset_requested")

func load_level(level: String):
	set_just_started(true)
	player.set_moves(0)
	current_level = level
	_reset_level()

func set_just_started(new_start):
	just_started = new_start

func _reset_level():
	delete_children(walls)
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
	var flr = floor_prefab.instance()
	flr.position = tile_pos
	floors.add_child(flr)

func add_wall(tile_pos):
	var wall = wall_prefab.instance()
	wall.position = tile_pos
	walls.add_child(wall)
