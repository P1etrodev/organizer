if __name__ == '__main__':
	import sys
	from pathlib import Path
	from winreg import HKEYType, REG_SZ, CreateKey, SetValueEx, HKEY_CLASSES_ROOT

	frozen: bool = hasattr(sys, 'frozen')

	location: Path = Path(sys.executable).parent if frozen else Path(__file__).parent
	main: str = 'Organizer.exe' if frozen else 'organizer.py'
	command: str = f'"{str(location.joinpath(main))}" "%V"' if frozen \
		else f'python "{str(location.joinpath(main))}" "%V"'

	class Icons:
		MASTER: str = str(location.joinpath("Master.ico"))
		ORGANIZER: str = str(location.joinpath("Icon.ico"))

	master_key_path: Path = Path(r'Directory\\Background\\shell\\Pietrodev')
	master_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(master_key_path))
	SetValueEx(master_key, 'MUIVerb', 0, REG_SZ, 'Pietrodev')
	SetValueEx(master_key, 'subcommands', 0, REG_SZ, '')
	SetValueEx(master_key, 'SeparatorAfter', 0, REG_SZ, '')
	SetValueEx(master_key, 'SeparatorBefore', 0, REG_SZ, '')
	SetValueEx(master_key, 'Icon', 0, REG_SZ, Icons.MASTER)

	master_key_path_shell: Path = master_key_path.joinpath('shell')
	master_key_shell: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(master_key_path_shell))

	organizer_key_path: Path = master_key_path_shell.joinpath('Organizer')
	organizer_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(organizer_key_path))
	SetValueEx(organizer_key, 'MUIVerb', 0, REG_SZ, 'Organizer')
	SetValueEx(organizer_key, 'subcommands', 0, REG_SZ, '')
	SetValueEx(organizer_key, 'Icon', 0, REG_SZ, Icons.ORGANIZER)

	organizer_shell_key_path: Path = organizer_key_path.joinpath('shell')
	organizer_shell_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(organizer_shell_key_path))

	organize_key_path: Path = organizer_shell_key_path.joinpath('Organize')
	organize_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(organize_key_path))
	SetValueEx(organize_key, 'MUIVerb', 0, REG_SZ, 'Organize')

	organize_command_key_path: Path = organize_key_path.joinpath('command')
	organize_command_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(organize_command_key_path))
	SetValueEx(organize_command_key, '', 0, REG_SZ, command)

	settings_key_path: Path = organizer_shell_key_path.joinpath('Settings')
	settings_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(settings_key_path))
	SetValueEx(settings_key, 'MUIVerb', 0, REG_SZ, 'Settings...')

	settings_command_key_path: Path = settings_key_path.joinpath('command')
	settings_command_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(settings_command_key_path))
	SetValueEx(settings_command_key, '', 0, REG_SZ, rf'"{str(location.joinpath("config.json"))}"')
