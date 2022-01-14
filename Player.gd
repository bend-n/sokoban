extends CollisionObject2D

signal level_reset_requested

const GRID_SIZE = 16

var moves = 0 setget set_moves

var last_move = null
var last_move_crate = null
var world: Node2D
var count = 0
var started = false
var won := false

signal won

onready var cam = $Camera2D
onready var tween = $Tween
onready var ray = $RayCast2D
onready var dir = $Direction
onready var anitree: AnimationTree = $AnimationTree
onready var anistate = anitree.get("parameters/playback")


func _ready():
	anitree.active = true


func initialize():
	won = false
	set_physics_process(false)
	yield(get_tree().create_timer(2), "timeout")
	set_physics_process(true)


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

	if Utils.stop_input:
		return

	if get_parent().get_parent().just_started:
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
		if not started:
			get_parent().get_parent().start_stopwatch()
			started = true
		var offset = move_intent * GRID_SIZE

		apply_rotation(offset)

		if ray.is_colliding():
			var collider = ray.get_collider()
			if collider.is_in_group("crates"):
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
			Tween.EASE_IN_OUT
		)
		tween.start()

		SoundFx.play("walk", -10, rand_range(.9, 1.1))
		anistate.travel("Run")
		anitree.set("parameters/Run/blend_position", move_intent)
	else:
		anistate.travel("Idle")


func set_moves(new_moves: int):
	moves = new_moves
	$"../../CanvasLayer/HUD/MovesLabel".text = "Moves: " + str(moves)


func apply_rotation(offset: Vector2):
	ray.cast_to = offset

	var new_rot := offset.angle()

	ray.force_raycast_update()

	var future_rot := lerp_angle(dir.rotation, new_rot, 1)

	if future_rot != dir.rotation:
		tween.interpolate_property(
			dir, "rotation", dir.rotation, future_rot, 0.3, Tween.TRANS_LINEAR, Tween.EASE_IN_OUT
		)
		tween.start()


func _over():
	if won:
		return
	emit_signal("won")
	won = true


func _on_Player_body_exited(_body):
	pass
	# if not body.name == "Player" and not body.is_in_group("crates"):
	# 	print("emitting won")
	# 	if won:
	# 		return
	# 	emit_signal("won")
	# 	won = true
