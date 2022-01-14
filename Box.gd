extends KinematicBody2D

var target_count = 0

signal target_updated()


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
			0.05,
			Tween.TRANS_LINEAR,
			Tween.EASE_IN_OUT)
	$Tween.start()
	
	return true


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
