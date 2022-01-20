extends Node2D

signal level_reset_requested()

const GRID_SIZE = 16

var moves = 0 setget set_moves

var last_move = null
var last_move_crate = null
var world : Node2D

onready var cam = $Camera2D
onready var tween = $Tween
onready var ray = $RayCast2D
onready var dir = $Direction
onready var anitree : AnimationTree = $AnimationTree
onready var anistate = anitree.get("parameters/playback")

func _ready():
	anitree.active = true

func _physics_process(_delta):
	
	if Input.is_action_just_pressed("level_reload"):
		emit_signal("level_reset_requested")
		anistate.travel("Idle")
		set_moves(0)
		last_move = null
		last_move_crate = null
		return
	
	if not world:
		return
	
	if world.over:
		anistate.travel("Idle")
		return
	
	if tween.is_active():
		return
	
	var move_intent = Vector2.ZERO
	
	move_intent = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	
	if Input.is_action_just_pressed("undo_last_move"):
		if last_move != null:
			self.position -= last_move * GRID_SIZE
			if last_move_crate != null:
				last_move_crate.position -= last_move * GRID_SIZE
			set_moves(moves - 1)
			last_move = null
			last_move_crate = null
		return
	
	if move_intent.x != 0 && move_intent.y != 0:
		move_intent = Vector2.ZERO
		
	if move_intent != Vector2.ZERO:
		var offset = move_intent * GRID_SIZE
		
		apply_rotation(offset)

		if ray.is_colliding():
			var collider = ray.get_collider()
			if collider.is_in_group('crates'):
				if !collider.push(offset):
					anistate.travel("Idle")
					return
				
				last_move_crate = collider
			
			else:
				anistate.travel("Idle")
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
			0.35,
			Tween.TRANS_LINEAR,
			Tween.EASE_IN_OUT)
		tween.start()
		
		SoundFx.play("walk", -10, rand_range(.9, 1.1))
		anistate.travel("Run")
		anitree.set("parameters/Run/blend_position", move_intent)
	else:
		anistate.travel("Idle")

func set_moves(new_moves: int):
	moves = new_moves
	$"../../CanvasLayer/HUD/MovesLabel".text = "Moves: " + str(moves)

func apply_rotation(offset : Vector2):
	ray.cast_to = offset
	var new_rot = round(rad2deg(offset.angle()))
	ray.force_raycast_update()

	tween.interpolate_property(
		dir,
		"rotation_degrees",
		dir.rotation_degrees,
		new_rot,
		0.2,
		Tween.TRANS_LINEAR,
		Tween.EASE_IN_OUT)
	tween.start()
	
	return offset
