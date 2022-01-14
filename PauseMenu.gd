extends CanvasLayer


func _ready():
	$PauseMenu.hide()


func pause_toggle(new_pause_state):
#	var new_pause_state = not get_tree().paused
	get_tree().paused = new_pause_state
	$PauseMenu.visible = new_pause_state
	$Settings.pressed = new_pause_state
	if new_pause_state:
		$PauseMenu/ColorRect/CenterContainer/VBoxContainer/QuitButton.grab_focus()


func _on_QuitButton_pressed():
	get_tree().quit()


func _on_Settings_toggled(button_pressed):  # pause enablement button
	pause_toggle(button_pressed)


# not to be confused
func _on_SettingsButton_pressed():
	$SettingsMenu.start()


func _on_Back_pressed():
	pause_toggle(false)


func _on_BackButton_pressed():
	get_tree().change_scene("res://StartScreen.tscn")
