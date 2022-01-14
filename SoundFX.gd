extends Node

var res = "res://"

var sounds = {
	"victory": load(res + "victory.wav"),
	"motion_box": load(res + "motion_box.wav"),
	"defeat": load(res + "gameover.wav"),
	"walk": load(res + "walk.wav")
}

onready var sound_players = get_children()


func play(sound_string, volume_db = 0, pitch_scale = randf() + 0.4):
	if sound_string == "target":
		if not $WINTONEPLAYER.playing:
			$WINTONEPLAYER.stream = sounds[sound_string]
			$WINTONEPLAYER.play()
			yield($WINTONEPLAYER, "finished")
			return
		return
	for soundPlayer in sound_players:
		if not soundPlayer.playing:
			soundPlayer.pitch_scale = pitch_scale
			soundPlayer.volume_db = volume_db
			soundPlayer.stream = sounds[sound_string]
			soundPlayer.play()
			return
	print_debug("TOO MANY SOUNDS")
