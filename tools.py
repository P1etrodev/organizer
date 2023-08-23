

def check_config_existence(location):
	from pathlib import Path
	from json import load, dump

	default_config = {
		'Documents': [
			'txt',
			'pdf',
			'html',
			'css',
			'yaml',
			'json',
			'docx',
			'xml',
			'xlsx',
			'csv'
		],
		'Images': [
			'png',
			'jpg',
			'gif',
			'svg',
			'ico'
		],
		'Video': [
			'mp4',
			'webm',
			'mkv',
			'mov',
			'flv',
			'avi',
			'wmv',
			'm4v'
		],
		'Compressed': [
			'zip',
			'7z',
			'rar'
		],
		'Audio': [
			'mp3',
			'ogg',
			'wav',
			'wma'
		],
		'Software': [
			'exe',
			'msi'
		]
	}

	config_file = Path(location).joinpath('config.json')

	if not config_file.exists():
		with config_file.open('w') as f:
			dump(default_config, f, indent=2)
		return default_config

	with config_file.open('rb') as f:
		return load(f)