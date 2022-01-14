extends Node

var color := Color(0.333333, 0.490196, 0.333333)

var starting = false
var loading = false
var loading_int = 0

var loadScreen: CanvasLayer = null
var stop_input = false

signal loaded_loading_screen

const LoadScreen = preload("res://LoadingScreen.tscn")


func _ready():
	VisualServer.set_default_clear_color(color)


func instance_scene_on_main(position, scene):
	var main = get_tree().current_scene
	var instance = scene.instance()
	main.add_child(instance)
	if not instance is CanvasLayer:
		instance.global_position = position
	return instance


func change_scene_to(scene):
	get_tree().change_scene_to(scene)


func load_loading_screen():
	# redundancy check
	if loadScreen != null:
		return
	yield(get_tree().create_timer(.1), "timeout")
	loadScreen = instance_scene_on_main(Vector2.ZERO, LoadScreen)
	loadScreen.startup()
	yield(loadScreen, "startup_complete")
	emit_signal("loaded_loading_screen")


func unload_loading_screen():
	if loadScreen == null:
		return
	loadScreen.exit()
	loadScreen = null


func _set_disable_inputs(inputs):
	stop_input = inputs
	get_viewport().gui_disable_input = inputs
	get_tree().call_group("input", "set_process_input", !inputs)
