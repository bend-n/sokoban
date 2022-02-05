extends Node2D

export(Color) var color

var currentintlevel :int = 1
var screenshots = 0
var game_over = false setget set_over
var game_won = false setget set_won
var over = false
var just_started = true

onready var console = $Level/CanvasLayer/HUD/console

const path = "user://"

func _ready():
	$WinScreen.player = $Level/LevelContainer/Player
	VisualServer.set_default_clear_color(color)
	$WinScreen.hide(false)
	$Level.connect("level_completed", self, "_on_Level_level_completed")
	$Level.connect("level_reset", self, "_on_Level_level_reset")
	$Level.connect("game_over", self, "_on_Level_game_over")
	$StartScreen.connect("start", self, "_on_start_start")
	$StartScreen.connect("load_level", self, "_on_start_load")

func _on_Level_level_completed(complete = false):
	$Level/CanvasLayer/HUD/StopWatch.set_process(false)
	if complete:
		$WinScreen.show(str($Level.current_level))
		game_over = false
		game_won = true
	else:
		$Level/LevelContainer/LevelComplete.play("Animate")
	get_tree().call_group("target", "play_pulse")

func _on_Level_level_reset():
	$WinScreen.hide(true)
	$GameoverScreen.hide(true)
	game_over = false
	game_won = false

func _on_Level_game_over():
	game_over = true
	game_won = false
	if not $GameoverScreen.shown:
		$GameoverScreen.show(str($Level.current_level))

onready var cam = $Level/LevelContainer/Player.cam

var max_zoom = 3
var min_zoom = .25

func _input(event : InputEvent):
	
	if event.is_action("scrollup"):
		var new_zoom = cam.zoom.x
		new_zoom += .01
		new_zoom = clamp(new_zoom, min_zoom, max_zoom)
		cam.zoom = Vector2(new_zoom, new_zoom)
	
	elif event.is_action("scrolldown"):
		var new_zoom = cam.zoom.x
		new_zoom -= .03
		new_zoom = clamp(new_zoom, min_zoom, max_zoom)
		cam.zoom = Vector2(new_zoom, new_zoom)
	
	elif event.is_action_released("next"):
		currentintlevel += 1
		currentintlevel = clamp(currentintlevel, 1, 60)
		_on_start_start()
	
	if event.is_action_released("ui_accept"):
		if $WinScreen.shown:
			currentintlevel += 1
			$WinScreen.hide(true)
			game_won = false
			$Level.load_level(str(currentintlevel))
		
		elif $GameoverScreen.shown:
			$GameoverScreen.hide(true) 
			game_won = false
			game_over = false
			$Level.load_level(str(currentintlevel), false)
		
	elif event.is_action_released("prtscrn"):
		screenshots += 1
		screenshots = clamp(screenshots, 0, 20)
		var save_path = path + "sokobanscreenshot_%s.png" % str(screenshots)
		var image = get_viewport().get_texture().get_data()
		image.flip_y()
		image.save_png(save_path)
		console.Log(OS.get_user_data_dir() + "/" + "sokobanscreenshot_%s.png" % str(screenshots), 5)

func _on_start_start():
	$Level/CanvasLayer/HUD.show()
	$Level.show()
	$StartScreen.hide()
	$Level.load_level(str(currentintlevel))

func _on_start_load(level):
	currentintlevel = level
	$Level.load_level(str(currentintlevel))
	$StartScreen.hide()
	$Level.show()
	$Level/CanvasLayer/HUD.show()

func _process(_delta):
	over = game_over or game_won

func set_won(value):
	game_won = value

func set_over(value):
	game_over = value
	over = game_over or game_won

