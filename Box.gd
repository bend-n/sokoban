extends Node2D

var main
var target_count = 0
var game_over = false

signal target_updated
signal game_over_detected


func push(offset: Vector2) -> bool:
	$RayCast.cast_to = offset
	$RayCast.force_raycast_update()

	if $RayCast.is_colliding():
		return false

	$Tween.interpolate_property(
		self,
		"position",
		self.position,
		self.position + offset,
		0.35,
		Tween.TRANS_LINEAR,
		Tween.EASE_IN_OUT
	)
	$Tween.start()
	SoundFx.play("motion_box", -17, rand_range(.5, 1))
	return true


func _is_stuck_in_a_corner() -> bool:
	var left_or_right_blocked = (
		$WallChecks/LR/Left.is_colliding()
		or $WallChecks/LR/Right.is_colliding()
	)
	var up_or_down_blocked = $WallChecks/DU/Up.is_colliding() or $WallChecks/DU/Down.is_colliding()

	return left_or_right_blocked and up_or_down_blocked


func entered_target(_target):
	target_count += 1
	_update_check_mark()
	emit_signal("target_updated")


func left_target(_target):
	target_count -= 1
	_update_check_mark()
	emit_signal("target_updated")


func _update_check_mark():
	$CheckSprite.visible = target_count > 0


func check_over():
	yield(get_tree().create_timer(0.2), "timeout")
	if target_count == 0 and not main.game_over and _is_stuck_in_a_corner():
		emit_signal("game_over_detected")


func _on_Tween_tween_all_completed():
	check_over()
