extends Sprite

onready var tween = $Tween

onready var initial_pos = position

var start_new = true


func _physics_process(_delta):
	if tween.is_active():
		return

	if not start_new:
		return

	tween.interpolate_property(
		self,
		"position",
		position,
		position + Vector2.RIGHT * 32,
		.7,
		tween.TRANS_LINEAR,
		tween.EASE_IN_OUT
	)
	tween.start()


func _on_VisibilityNotifier2D_screen_exited():
	start_new = false
	if tween.is_active():
		yield(tween, "tween_all_completed")
		tween.stop_all()
	position = initial_pos
	start_new = true
