extends Node

var color := Color(0.333333, 0.490196, 0.333333)

var starting = false
var loading = false
var loading_int = 0

func instance_scene_on_main(position, scene):
	var main = get_tree().current_scene
	var instance = scene.instance()
	main.add_child(instance)
	instance.global_position = position
	return instance

func change_scene_to(scene):
	get_tree().change_scene_to(scene)

func _ready():
	VisualServer.set_default_clear_color(color)
