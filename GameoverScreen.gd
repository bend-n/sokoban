extends CanvasLayer

var player : KinematicBody2D
var shown = false

func show(integer):
	shown = true
	$Container/AnimationPlayer.play("Animate")
	$Container.visible = true
	$Container/Label._dialogue("LEVEL %s FAILED PRESS enter TO RETRY" % integer)

func hide(backwards = true):
	if backwards:
		if shown:
			$Container/Label._erase()
			$Container/AnimationPlayer.play_backwards("Animate")
			yield($Container/AnimationPlayer, "animation_finished")
			$Container.hide()
			shown = false
	else:
		shown = false
		$Container.hide()
