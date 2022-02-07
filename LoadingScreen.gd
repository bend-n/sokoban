extends CanvasLayer

onready var animate : AnimationPlayer = $animate
onready var progress = $Container/occluder/Progressbar
onready var tween = $Container/Tween
onready var fade = $fade
onready var center = $Container.get_viewport_rect().size / 2

var queued = false

signal startup_complete
#signal exit_complete

func _ready():
	$Container/occluder.position = center

func startup():
	fade.play("Fadein")
	animate.play("Animate")
	yield(fade, "animation_finished")
	emit_signal("startup_complete")
	increment_progress()

func exit():
	if tween.is_active():
		queued = true
		yield(tween, "tween_all_completed")
	tween_progress(progress.value, 100, Vector2(1, 2))
	yield(tween, "tween_all_completed")
	fade.play("Fadeout")
#	emit_signal("exit_complete")

func tween_progress(old :float, new :float, length_range :Vector2):
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
