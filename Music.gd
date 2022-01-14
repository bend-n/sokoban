extends Node

export(Array, AudioStream) var music_list = []

var music_index = 0
var lowering_sound = false
const min_vol_db = -17

onready var musicPlayer = $AudioStreamPlayer
onready var tween = $Tween


func _ready():
	music_list.shuffle()
	list_play()


func list_play():
	assert(music_list.size() > 0)
	musicPlayer.stream = music_list[music_index]
	musicPlayer.play()
	music_index += 1
	if music_index == music_list.size():
		music_index = 0

	tween.interpolate_property(
		musicPlayer,
		"volume_db",
		musicPlayer.volume_db,
		min_vol_db,
		40,
		Tween.TRANS_LINEAR,
		Tween.EASE_IN_OUT
	)


func lower_sound():
	lowering_sound = true
	var new_vol = musicPlayer.volume_db
	new_vol -= 10
	tween.interpolate_property(
		musicPlayer,
		"volume_db",
		musicPlayer.volume_db,
		new_vol,
		.5,
		tween.TRANS_LINEAR,
		tween.EASE_IN_OUT
	)
	tween.start()


func continue_playback():
	lowering_sound = false
	_on_Timer_timeout()


func list_stop():
	musicPlayer.stop()


func _on_AudioStreamPlayer_finished():
	music_list.shuffle()
	list_play()


func _on_Timer_timeout():
	var new_pitch = rand_range(.9, 1.1)
	tween.interpolate_property(
		musicPlayer,
		"pitch_scale",
		musicPlayer.pitch_scale,
		new_pitch,
		1,
		tween.TRANS_LINEAR,
		tween.EASE_IN_OUT
	)
	tween.start()
#	if not lowering_sound:
#		var new_vol = rand_range(-8, -12)
#		tween.interpolate_property(musicPlayer, "volume_db", musicPlayer.volume_db, new_vol, .5, tween.TRANS_LINEAR, tween.EASE_IN_OUT)
#		tween.start()
