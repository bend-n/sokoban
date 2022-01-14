extends CanvasLayer

onready var animate: AnimationPlayer = $animate
onready var progress = $Container/occluder/Progressbar
onready var tween = $Container/Tween
onready var fade = $fade
var queued = false

const distance = 150

signal startup_complete


func _ready():
	setup_curve(center($Container/occluder), $Container/Path)
	# sets up the curve with the return value from the centering of the occluder


func setup_curve(center, path):
	var curve := Curve2D.new()
	curve.clear_points()

	var top_left = center + Vector2(-distance, -distance)
	var bottom_left = center + Vector2(-distance, distance)
	var top_right = center + Vector2(distance, -distance)
	var bottom_right = center + Vector2(distance, distance)

	for corner in [top_left, top_right, bottom_right, bottom_left, top_left]:
		curve.add_point(corner)

	path.set_curve(curve)


func center(node):
	node.position = $Container.get_viewport_rect().size / 2
	return node.position


func startup():
	Utils._set_disable_inputs(true)
	fade.play("Fadein")
	animate.play("Animate")
	yield(fade, "animation_finished")
	emit_signal("startup_complete")
	increment_progress()


func exit():
	if tween.is_active():
		queued = true
		yield(tween, "tween_all_completed")
	tween_progress(progress.value, 100, Vector2(.1, .5))
	yield(tween, "tween_all_completed")
	fade.play("Fadeout")
	Utils._set_disable_inputs(false)


func _exit_tree():
	Utils._set_disable_inputs(false)


func tween_progress(old: float, new: float, length_range: Vector2):
	tween.interpolate_property(
		progress,
		"value",
		old,
		new,
		rand_range(length_range.x, length_range.y),
		Tween.TRANS_LINEAR,
		Tween.EASE_IN_OUT
	)
	tween.start()


func increment_progress():
	if not tween.is_active() and not queued:
		tween_progress(progress.value, progress.value + round(rand_range(5, 25)), Vector2(1, 2))
