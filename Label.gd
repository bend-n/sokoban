extends Label

onready var Timer = $Timer


func _ready():
	Timer.set_wait_time(.1)  # time between letters


func _dialogue(string):
	for letter in string:
		Timer.start()
		text += letter
		yield(Timer, "timeout")


func _erase():
	for letter in text:
		Timer.start()
		text = text.substr(0, len(text) - 1)
		yield(Timer, "timeout")
