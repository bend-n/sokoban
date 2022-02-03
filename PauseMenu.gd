extends CanvasLayer

func _input(event):
	if event.is_action_pressed("pause"):
		var new_pause_state = not get_tree().paused
		get_tree().paused = new_pause_state
		$PauseMenu.visible = new_pause_state
		if new_pause_state:
			$PauseMenu/ColorRect/CenterContainer/VBoxContainer/QuitButton.grab_focus()

func _ready():
	$PauseMenu.hide()

func _on_QuitButton_pressed():
	get_tree().quit()
