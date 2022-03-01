extends Node

const settings_file = "user://settings.res"
const level_file = "user://level_data.res"

var files := {  # file types
	"settings":
	{
		"file": settings_file,
		"data":
		{"stopwatch": false, "fullscreen": true, "resolution": Vector2(1280, 720), "vsync": false}
	},
	"level": {"file": level_file, "data": {"highest_level": "0", "current_level": "1"}}
}


func _ready():
	load_data("settings")
	load_data("level")


func save(type):
	var file = File.new()
	file.open(files[type].file, File.WRITE)
	file.store_string(var2str(files[type].data))


func load_data(type: String):
	var file = File.new()
	if check_file(type):
		file.open(files[type].file, File.READ)
		if file.get_as_text().length() > 0:
			var read_dictionary: Dictionary = str2var(file.get_as_text())
			if files[type].data.size() == read_dictionary.size():
				files[type].data = read_dictionary
		file.close()


func check_file(type):
	var file = File.new()
	return file.file_exists(files[type].file)
