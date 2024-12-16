from pathlib import Path

import tests_form


def path(file_name):
    return str(
        Path(tests_form.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )
