extends CanvasLayer

const world = preload("res://World.tscn")

var level_to_load = 1


func _ready():
	$Control/Hi.text = "Highscore: " + SaveLoad.files.level.data.highest_level
	$Control/CenterContainer/VBoxContainer/StartButton.grab_focus()


func _on_StartButton_pressed():
	Utils.starting = true
	Utils.change_scene_to(world)


func _on_LoadButton_pressed():
	var spinbox: SpinBox = $Control/CenterContainer/VBoxContainer/HBoxContainer/Spinbox
	spinbox.show()
	var spinline: LineEdit = spinbox.get_line_edit()
	spinline.connect("text_entered", self, "_on_spinbox_entered")


func _on_QuitButton_pressed():
	get_tree().quit()


func hide():
	$Control.hide()


func _on_spinbox_entered(text):
	level_to_load = int(text)
	level_to_load = clamp(level_to_load, 1, 60)
	Utils.loading = true
	Utils.loading_int = level_to_load
	Utils.change_scene_to(world)


func _on_ContinueButton_pressed():
	Utils.loading_int = int(SaveLoad.files.level.data.current_level)
	Utils.loading = true
	Utils.change_scene_to(world)


func _on_LoadScreenButton_pressed():
	Utils.load_loading_screen()
	yield(get_tree().create_timer(30), "timeout")
	Utils.unload_loading_screen()
