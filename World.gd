extends Node2D

var currentintlevel := 1
var screenshots = 0
var game_over = false setget set_over
var game_won = false setget set_won
var over = false
var just_started = true

onready var level := $Level
onready var console = MainInstances.console

const path = "user://"


func _ready():
	if Utils.starting:
		start()
		Utils.starting = false
	if Utils.loading:
		Utils.loading = false
		currentintlevel = Utils.loading_int
		Utils.loading_int = 0
		start()
	$WinScreen.player = $Level/LevelContainer/Player
	$WinScreen.hide(false)
	level.connect("level_completed", self, "_on_Level_level_completed")
	level.connect("level_reset", self, "_on_Level_level_reset")
	level.connect("game_over", self, "_on_Level_game_over")


func _on_Level_level_completed(complete = false):
	$Level/CanvasLayer/HUD/StopWatch.set_process(false)
	if complete:
		$WinScreen._show(str(level.current_level))
		save(currentintlevel + 1)
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


func save(new_level):  # what level are we on/going to
	if (new_level) > int(SaveLoad.files.level.data.highest_level):
		SaveLoad.files.level.data.highest_level = str(new_level - 1)
		console.Log("New Highscore!")
	SaveLoad.save("level")


func _on_Level_game_over():
	game_over = true
	game_won = false
	$GameoverScreen._show(str(level.current_level))


onready var cam = $Level/LevelContainer/Player.cam

var max_zoom = 3
var min_zoom = .25


func _input(event: InputEvent):
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

		start()

	if event.is_action_released("ui_accept"):
		if $WinScreen.shown:
			currentintlevel += 1
			$WinScreen.hide(true)
			game_won = false
			level.load_level(str(currentintlevel))

		elif $GameoverScreen.shown:
			$GameoverScreen.hide(true)
			game_won = false
			game_over = false
			level.load_level(str(currentintlevel), false)

	elif event.is_action_released("prtscrn"):
		screenshots += 1
		screenshots = clamp(screenshots, 0, 20)
		var save_path = path + "sokobanscreenshot_%s.png" % str(screenshots)
		var image = get_viewport().get_texture().get_data()
		image.flip_y()
		if console.Log(
			(
				"saved to: "
				+ OS.get_user_data_dir()
				+ "/"
				+ "sokobanscreenshot_%s.png" % str(screenshots)
			),
			1,
			2.5
		):
			image.save_png(save_path)


func start():
	Utils.load_loading_screen()
	yield(Utils, "loaded_loading_screen")
	$Level/CanvasLayer/HUD.show()
	level.show()
	level.load_level(str(currentintlevel))


func set_won(value):
	game_won = value
	over = game_over or game_won


func set_over(value):
	game_over = value
	over = game_over or game_won
