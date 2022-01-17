extends Node2D

signal level_reset_requested()

const GRID_SIZE = 16

var moves = 0 setget set_moves

var last_move = null
var last_move_crate = null

onready var cam = $Camera2D
onready var tween = $Tween
onready var ray = $RayCast2D
onready var dir = $Direction

func _unhandled_input(event):
	
	if tween.is_active():
		return
	
	var move_intent = Vector2.ZERO
	
	if event.is_action_pressed("ui_right", true):
		move_intent = Vector2.RIGHT
	elif event.is_action_pressed("ui_left", true):
		move_intent = Vector2.LEFT
	elif event.is_action_pressed("ui_up", true):
		move_intent = Vector2.UP
	elif event.is_action_pressed("ui_down", true):
		move_intent = Vector2.DOWN
	elif event.is_action_pressed("level_reload"):
		emit_signal("level_reset_requested")
		_animate(Vector2.DOWN, false)
		set_moves(0)
		last_move = null
		last_move_crate = null
		return
	elif event.is_action_pressed("undo_last_move"):
		if last_move != null:
			self.position -= last_move * GRID_SIZE
			if last_move_crate != null:
				last_move_crate.position -= last_move * GRID_SIZE
			set_moves(moves - 1)
			last_move = null
			last_move_crate = null
		return
	
	if move_intent != Vector2.ZERO:
		var offset = move_intent * GRID_SIZE
		
		ray.cast_to = offset
		dir.rotation = offset.angle()
		ray.force_raycast_update()
		
		if ray.is_colliding():
			var collider = ray.get_collider()
			if collider.is_in_group('crates'):
				if !collider.push(offset):
					_animate(move_intent, false)
					return
				
				last_move_crate = collider
			
			else:
				_animate(move_intent, false)
				return
		
		else:
			last_move_crate = null
		
		set_moves(moves + 1)
		last_move = move_intent
		
		tween.interpolate_property(
			self,
			"position",
			self.position,
			self.position + offset,
			0.1,
			Tween.TRANS_LINEAR,
			Tween.EASE_IN_OUT)
		tween.start()
		
		_animate(move_intent, true)

func set_moves(new_moves: int):
	moves = new_moves
	$"../../CanvasLayer/HUD/MovesLabel".text = "Moves: " + str(moves)


func _animate(direction: Vector2, active: bool):
	pass
#	if direction == Vector2.RIGHT:
#		$AnimationPlayer.play("right")
#	elif direction == Vector2.LEFT:
#		$AnimationPlayer.play("left")
#	elif direction == Vector2.UP:
#		$AnimationPlayer.play("up")
#	elif direction == Vector2.DOWN:
#		$AnimationPlayer.play("down")
#
#	if !active:
#		$AnimationPlayer.seek(0.05)
