extends Area2D


func _on_Target_body_entered(body):
	if body.is_in_group('crates'):
		body.entered_target(self)


func _on_Target_body_exited(body):
	if body.is_in_group('crates'):
		body.left_target(self)
