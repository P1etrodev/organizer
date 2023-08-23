from functools import reduce
from pathlib import Path

from tools import check_config_existence


def main():
	import sys

	frozen: bool = hasattr(sys, 'frozen')

	location: Path = Path(sys.executable).parent if frozen else Path(__file__).parent

	directory: str = sys.argv[1]

	config: dict = check_config_existence(location=location.resolve())

	for file in Path(directory).glob('*'):
		if file.name not in list(config.keys()) + ['Others']:

			if file.suffix.split('.')[-1] not in list(reduce(lambda x, x2: x + x2, config.values())):
				others_f: Path = Path('Others')
				others_f.mkdir(exist_ok=True)

				file.rename(others_f.joinpath(file.name))

				continue

			for folder, extensions in config.items():
				f: Path = Path(folder)

				if file.suffix.split('.')[-1] in extensions:
					f.mkdir(exist_ok=True)
					file.rename(f.joinpath(file.name))
					continue


main()
