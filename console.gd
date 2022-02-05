extends Label

onready var anim : AnimationPlayer = $anim

func _ready():
	percent_visible = 0

func Log(new_text :String, length := 5.0):
	percent_visible = 0
	text = new_text
	anim.play("play")
	yield(anim, "animation_finished")
	yield(get_tree().create_timer(length), "timeout")
	anim.play_backwards("play")
