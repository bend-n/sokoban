extends Node2D

var currentintlevel := 1
var screenshots = 0

const path = "user://"

func _ready():
	$WinScreen.player = $Level/LevelContainer/Player
	VisualServer.set_default_clear_color(Color.black)
	$WinScreen.hide(false)
	$Level.connect("level_completed", self, "_on_Level_level_completed")
	$Level.connect("level_reset", self, "_on_Level_level_reset")
	$StartScreen.connect("start", self, "_on_start_start")
	$StartScreen.connect("load_level", self, "_on_start_load")

func _on_Level_level_completed():
	$WinScreen.show(str($Level.current_level))

func _on_Level_level_reset():
	$WinScreen.hide(false)

func _input(event : InputEvent):
	if event.is_action_released("ui_accept") and $WinScreen/Container.visible:
		currentintlevel += 1
		$WinScreen.hide()
		$Level.load_level(str(currentintlevel))
	
	elif event.is_action_released("prtscrn"):
		screenshots += 1
		screenshots = clamp(screenshots, 0, 20)
		print("SCREENSHOT " + str(screenshots))
		var image = get_viewport().get_texture().get_data()
		image.flip_y()
		image.save_png(path + "sokobanscreenshot_%s.png" % str(screenshots))

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
