extends CanvasLayer

func show(integer):
	$Container/AnimationPlayer.play("Animate")
	$Container.visible = true
	$Container/Label._dialogue(" %s COMPLETED PRESS enter TO CONTINUE" % integer)

func hide(backwards = true):
	if backwards:
		$Container/Label._erase()
		$Container/AnimationPlayer.play_backwards("Animate")
	else:
		$Container.hide()
