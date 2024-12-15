from pathlib import Path

import gurulesson91.tests_form


def path(file_name):
    return str(
        Path(gurulesson91.tests_form.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )
