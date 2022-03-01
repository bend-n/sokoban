extends Label

var time_elapsed := 0.0


func _ready():
	MainInstances.stopwatch = self
	set_process(false)


func start():
	set_process(true)


func _exit_tree():
	MainInstances.stopwatch = null


func reset():
	time_elapsed = 0.0
	text = _format_seconds(time_elapsed, true)
	set_process(false)


func _process(delta):
	time_elapsed += delta
	text = _format_seconds(time_elapsed, true)


func _format_seconds(time: float, use_milliseconds: bool) -> String:
	var minutes := time / 60
	var seconds := fmod(time, 60)

	if not use_milliseconds:
		return "%02d:%02d" % [minutes, seconds]

	var milliseconds := fmod(time, 1) * 100

	return "%02d:%02d:%02d" % [minutes, seconds, milliseconds]
