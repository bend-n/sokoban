extends CanvasLayer

onready var label = $Label
onready var tween = $Tween


func _ready():
	MainInstances.console = self
	label.percent_visible = 0


func Log(new_text: String, time := .5, length := 2.5):
	if tween.is_active():
		return false
	label.percent_visible = 0
	label.text = new_text
	tween_(0, 1, time)
	yield(tween, "tween_all_completed")
	yield(get_tree().create_timer(length), "timeout")
	tween_(1, 0, time)
	return true


func _exit_tree():
	MainInstances.console = null


func tween_(from, to, time):
	tween.interpolate_property(
		$Label, "percent_visible", from, to, time, Tween.TRANS_LINEAR, Tween.EASE_IN_OUT
	)
	tween.start()
