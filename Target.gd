extends Node

onready var anim = $AnimationPlayer

var main: Node2D
onready var circle = $Circle


func _on_Target_body_entered(body):
	if body.is_in_group("crates"):
		body.entered_target(self)
		if not main.just_started:
			play_pulse()


func _on_Target_body_exited(body):
	if body.is_in_group("crates"):
		body.left_target(self)
		anim.play("Animate")


func r():
	return rand_range(0, 1)


func play_pulse():
	circle.self_modulate = Color(r(), r(), r(), 1)
	anim.play("Animate")
