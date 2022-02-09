extends CanvasLayer

const world = preload("res://World.tscn")

signal start
signal load_level(level)

var level_to_load = 1

func _ready():
	$Control/CenterContainer/VBoxContainer/StartButton.grab_focus()

func _on_StartButton_pressed():
	emit_signal("start")
	Utils.starting = true
	Utils.change_scene_to(world)

func _on_LoadButton_pressed():
	var spinbox : SpinBox = $Control/CenterContainer/VBoxContainer/HBoxContainer/Spinbox
	spinbox.show()
	var spinline : LineEdit = spinbox.get_line_edit()
	spinline.connect("text_entered", self, "_on_spinbox_entered")

func _on_QuitButton_pressed():
	get_tree().quit()

func hide():
	$Control.hide()

func _on_spinbox_entered(text):
	level_to_load = int(text)
	level_to_load = clamp(level_to_load, 1, 60)
	emit_signal("load_level", level_to_load)
	Utils.loading = true
	Utils.loading_int = level_to_load
	Utils.change_scene_to(world)
