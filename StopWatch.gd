extends Label

var time_elapsed := 0.0 setget set_time_elapsed

func set_time_elapsed(time):
	time_elapsed = time

	text = _format_seconds(time_elapsed, true)

func _ready():
	set_process(false)

func _process(delta):
	self.time_elapsed += delta

func _format_seconds(time : float, use_milliseconds : bool) -> String:
	var minutes := time / 60
	var seconds := fmod(time, 60)

	if not use_milliseconds:
		return "%02d:%02d" % [minutes, seconds]

	var milliseconds := fmod(time, 1) * 100

	return "%02d:%02d:%02d" % [minutes, seconds, milliseconds]
