extends Control

var _settings := {resolution = Vector2(1280, 720), fullscreen = true, vsync = false, stopwatch = false}

export (NodePath) onready var vsyncbutton = get_node(vsyncbutton)
export (NodePath) onready var fullscreenbutton = get_node(fullscreenbutton)
export (NodePath) onready var resolution_input = get_node(resolution_input)
export (NodePath) onready var stopwatchbox = get_node(stopwatchbox)


func start():
	show()
	update_settings(false)
	yield(get_tree().create_timer(.3), "timeout")
	$ColorRect/ExitButton.grab_focus()

func update_settings_visual():
	fullscreenbutton.pressed = _settings.fullscreen
	vsyncbutton.pressed = _settings.vsync
	var resolution_text_placeholder = str(_settings.resolution.x) + "x" + str(_settings.resolution.y)
	resolution_input.placeholder_text = resolution_text_placeholder
	stopwatchbox.pressed = globalsettings.stopwatch

func _on_VscynButton_toggled(button_pressed):
	_settings.vsync = button_pressed
	update_settings()

func _on_FullscreenButton_toggled(button_pressed):
	_settings.fullscreen = button_pressed
	update_settings()

func update_settings(echo = true) -> void:
	resolution_input.placeholder_text = str(_settings.resolution.x) + "x" + str(_settings.resolution.y)
	OS.window_fullscreen = _settings.fullscreen
	OS.set_window_size(_settings.resolution)
	OS.vsync_enabled = _settings.vsync
	globalsettings.stopwatch = _settings.stopwatch
	update_settings_visual()
	if echo:
		MainInstances.console.Log("Settings applied.", 3)
	$ColorRect/VBoxContainer/HBoxContainer2/ResolutionHolder.visible = !_settings.fullscreen

func _on_ResolutionInput_text_entered(new_text : String):
	var text = new_text.split("x")
	if text.size() != 1: 
		MainInstances.console.Log("Please split text with a x (1270x720)", 5)
		return
	_settings.resolution = Vector2(text[0], text[1])
	update_settings()

func _on_ResolutionButton_pressed():
	resolution_input.visible = !resolution_input.visible

func _on_ExitButton_pressed():
	hide()
	update_settings(false)
	if get_parent().has_method("pause_toggle"):
		get_parent().pause_toggle(true)
	else:
		push_warning("Parent of %s not pausemenu" % self)

func _on_StopwatchBox_toggled(button_pressed):
	_settings.stopwatch = button_pressed
