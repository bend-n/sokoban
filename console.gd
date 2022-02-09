extends CanvasLayer

onready var label = $Label
onready var anim : AnimationPlayer = $anim

func _ready():
	MainInstances.console = self
	label.percent_visible = 0

func Log(new_text :String, length := 5.0):
	if anim.is_playing():
		return false
	label.percent_visible = 0
	label.text = new_text
	anim.play("play")
	yield(anim, "animation_finished")
	yield(get_tree().create_timer(length), "timeout")
	anim.play_backwards("play")
	return true

func _exit_tree():
	MainInstances.console = null
