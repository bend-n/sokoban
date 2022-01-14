extends Node

var stopwatch = false setget set_stopwatch


func set_stopwatch(set):
	stopwatch = set
	MainInstances.stopwatch.visible = stopwatch
