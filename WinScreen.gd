extends CanvasLayer

var player : KinematicBody2D
var shown = false

func show(integer):
	if not $Container/Label/Timer.time_left > 0:
		shown = true
		$Container/AnimationPlayer.play("Animate")
		$Container.visible = true
		$Container/Label._dialogue("LEVEL %s COMPLETED PRESS enter TO CONTINUE" % integer)

func hide(backwards = true):
	if backwards:
		shown = false
		$Container/Label._erase()
		$Container/AnimationPlayer.play_backwards("Animate")
		yield($Container/AnimationPlayer, "animation_finished")
		$Container.hide()
	else:
		shown = false
		$Container.hide()
