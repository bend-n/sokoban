extends CanvasLayer

var player: KinematicBody2D
var shown = false


func _show(integer):
	shown = true
	$Container/AnimationPlayer.play("Animate")
	$Container.visible = true
	$Container/Label._dialogue("LEVEL %s COMPLETED PRESS enter TO CONTINUE!" % integer)
	SoundFx.play("victory", -15)


func hide(backwards = true):
	shown = false
	if backwards:
		$Container/Label._erase()
		$Container/AnimationPlayer.play_backwards("Animate")
		yield($Container/AnimationPlayer, "animation_finished")
	$Container.hide()
