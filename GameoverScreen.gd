extends CanvasLayer

var player: KinematicBody2D
var shown = false


func _ready():
	$Container.hide()


func _show(integer):
	shown = true
	$Container/AnimationPlayer.play("Animate")
	$Container.visible = true
	$Container/Label._dialogue("LEVEL %s FAILED PRESS enter TO RETRY!" % integer)
	SoundFx.play("defeat")


func hide(backwards = true):
	if backwards:
		$Container/Label._erase()
		$Container/AnimationPlayer.play_backwards("Animate")
		yield($Container/AnimationPlayer, "animation_finished")
	shown = false
	$Container.hide()
