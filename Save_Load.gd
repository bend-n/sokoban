extends Node

const settings_file = "user://settings.res"
const level_file = "user://level_data.res"

var files := {
	"settings" : {
		"file" : settings_file,
		"data" : { "stopwatch" : false }
	},
	"level" : {
		"file" : level_file,
		"data" : {"highest_level" : "1"}
	}
}

func _ready():
	load_data("settings")

func save(type):
	var file = File.new()
	file.open(files[type].file, File.WRITE)
	file.store_string(var2str(files[type].data))

func load_data(type : String):
	var file = File.new()
	if check_file(type):
		file.open(files[type].file, File.READ)
		var read_dictionary = str2var(file.get_as_text())
		files[type].data = read_dictionary
		file.close()

func check_file(type):
	var file = File.new()
	return file.file_exists(files[type].file)
