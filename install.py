if __name__ == '__main__':
	import sys
	from pathlib import Path
	import winreg as reg

	if hasattr(sys, 'frozen'):
		location = Path(sys.executable).parent
		main = 'Organizer.exe'
		command = f'"{str(location.joinpath(main))}"'
	else:
		location = Path(__file__).parent
		main = 'organizer.py'
		command = f'python "{str(location.joinpath(main))}"'

	master_key_path = Path(r'Directory\\Background\\shell\\Pietrodev')
	master_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(master_key_path))
	reg.SetValueEx(master_key, 'MUIVerb', 0, reg.REG_SZ, 'Pietrodev')
	reg.SetValueEx(master_key, 'subcommands', 0, reg.REG_SZ, '')
	reg.SetValueEx(master_key, 'SeparatorAfter', 0, reg.REG_SZ, '')
	reg.SetValueEx(master_key, 'SeparatorBefore', 0, reg.REG_SZ, '')
	reg.SetValueEx(master_key, 'Icon', 0, reg.REG_SZ, f'{str(location.joinpath("Master.ico"))}')

	master_key_path_shell = master_key_path.joinpath('shell')
	master_key_shell = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(master_key_path_shell))

	organizer_key_path = master_key_path_shell.joinpath('Organizer')
	organizer_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(organizer_key_path))
	reg.SetValueEx(organizer_key, 'MUIVerb', 0, reg.REG_SZ, 'Organizer')
	reg.SetValueEx(organizer_key, 'subcommands', 0, reg.REG_SZ, '')
	reg.SetValueEx(organizer_key, 'Icon', 0, reg.REG_SZ, str(location.joinpath('Icon.ico')))

	organizer_shell_key_path = organizer_key_path.joinpath('shell')
	organizer_shell_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(organizer_shell_key_path))

	organize_key_path = organizer_shell_key_path.joinpath('Organize')
	organize_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(organize_key_path))
	reg.SetValueEx(organize_key, 'MUIVerb', 0, reg.REG_SZ, 'Organize')

	organize_command_key_path = organize_key_path.joinpath('command')
	organize_command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(organize_command_key_path))
	reg.SetValueEx(organize_command_key, '', 0, reg.REG_SZ, command)

	settings_key_path = organizer_shell_key_path.joinpath('Settings')
	settings_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(settings_key_path))
	reg.SetValueEx(settings_key, 'MUIVerb', 0, reg.REG_SZ, 'Settings...')

	settings_command_key_path = settings_key_path.joinpath('command')
	settings_command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, str(settings_command_key_path))
	reg.SetValueEx(settings_command_key, '', 0, reg.REG_SZ, rf'"{str(location.joinpath("config.json"))}"')
