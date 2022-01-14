extends Node2D

var currentintlevel :int = 1

func _ready():
	VisualServer.set_default_clear_color(Color.black)
	$WinScreen.hide(false)
	$Level.connect("level_completed", self, "_on_Level_level_completed")
	$Level.connect("level_reset", self, "_on_Level_level_reset")
	
	$Level.load_level(str(currentintlevel))

func _on_Level_level_completed():
	$WinScreen.show(str($Level.current_level))

func _on_Level_level_reset():
	$WinScreen.hide(false)

func _input(event : InputEvent):
	if event.is_action_released("ui_accept"):
		currentintlevel += 1
		$WinScreen.hide()
		$Level.load_level(str(currentintlevel))
