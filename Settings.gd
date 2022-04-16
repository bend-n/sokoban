extends Control

var _settings := {
	resolution = Vector2(1280, 720), fullscreen = true, vsync = true, stopwatch = false
}
var starting = true

export(NodePath) onready var vsyncbutton = get_node(vsyncbutton)
export(NodePath) onready var fullscreenbutton = get_node(fullscreenbutton)
export(NodePath) onready var resolution_input = get_node(resolution_input)
export(NodePath) onready var stopwatchbox = get_node(stopwatchbox)


func _ready():
	var data = SaveLoad.files.settings.data
	_settings.stopwatch = data.stopwatch
	_settings.resolution = data.resolution
	_settings.vsync = data.vsync
	_settings.fullscreen = data.fullscreen
	update_settings(false)


func start():
	starting = false
	yield(get_tree().create_timer(.3), "timeout")
	$ColorRect/ExitButton.grab_focus()
	show()


func update_settings_visual():
	fullscreenbutton.pressed = _settings.fullscreen
	vsyncbutton.pressed = _settings.vsync
	var resolution_text_placeholder = (
		str(_settings.resolution.x)
		+ "x"
		+ str(_settings.resolution.y)
	)
	resolution_input.placeholder_text = resolution_text_placeholder
	stopwatchbox.pressed = _settings.stopwatch


func _on_VscynButton_toggled(button_pressed):
	if starting:
		return
	_settings.vsync = button_pressed
	update_settings()


func _on_FullscreenButton_toggled(button_pressed):
	if starting:
		return
	_settings.fullscreen = button_pressed
	update_settings()


func update_settings(open := true) -> void:
	if not open:
		_settings.vsync = OS.vsync_enabled
		_settings.fullscreen = OS.window_fullscreen
		_settings.resolution = OS.window_size
		var data = SaveLoad.files.settings.data
		_settings = data
	apply_settings()
	update_settings_visual()
	if open:
		MainInstances.console.Log("Settings applied.", .1, 1)
	$ColorRect/VBoxContainer/HBoxContainer2/ResolutionHolder.visible = !_settings.fullscreen
	SaveLoad.save("settings")


func apply_settings():
	resolution_input.placeholder_text = (
		str(_settings.resolution.x)
		+ "x"
		+ str(_settings.resolution.y)
	)
	OS.window_fullscreen = _settings.fullscreen
	if _settings.fullscreen:
		_settings.resolution = OS.get_screen_size()
	OS.set_window_size(_settings.resolution)
	OS.vsync_enabled = _settings.vsync
	globalsettings.stopwatch = _settings.stopwatch


func _on_ResolutionInput_text_entered(new_text: String):
	if starting:
		return
	var text = new_text.split("x")
	if text.size() < 2:
		MainInstances.console.Log("Please split text with a x (1270x720)", 2.5, 5)
		return
	var text_processed = []
	for number in text:
		number = int(number)
		number = round(number)
		number = clamp(number, 400, 4000)
		text_processed.append(number)
	var new_res = Vector2(text_processed[0], text_processed[1])
	_settings.resolution = new_res
	update_settings()


func _on_ResolutionButton_pressed():
	if starting:
		return
	resolution_input.visible = !resolution_input.visible


func _on_ExitButton_pressed():
	hide()
	update_settings(false)
	if get_parent().has_method("pause_toggle"):
		get_parent().pause_toggle(true)
	else:
		push_warning("Parent of %s not pausemenu" % self)


func _on_StopwatchBox_toggled(button_pressed):
	if starting:
		return
	_settings.stopwatch = button_pressed
	update_settings()
