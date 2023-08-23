import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
	name="Organizer",
	executables=[
		Executable("install.py", base=base, target_name='Install', icon='Icon.ico', uac_admin=True),
		Executable("uninstall.py", base=base, target_name='Uninstall', icon='Icon.ico', uac_admin=True),
		Executable("organizer.py", base=base, target_name='Organizer', icon='Icon.ico'),
	],
	options={
		'build_exe': {
			'include_files': ['Icon.ico'],
			'silent_level': 1
		},
	}
)
