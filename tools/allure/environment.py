import platform
import sys

from config import settings


def create_allure_environment_file():

    environment_data = settings.model_dump()
    environment_data['os_info'] = platform.system(), platform.release()
    environment_data['python_version'] = sys.version

    items = [f'{key}={value}' for key, value in environment_data.items()]
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
