import os
from distutils.util import strtobool


class Environment:

    def __init__(self):
        self.url = os.getenv('DT_URL')
        self.api_key = os.getenv('DT_API_KEY')
        self.project_name = os.getenv('DT_PROJECT_NAME')
        self.project_version = os.getenv('DT_PROJECT_VERSION')
        self.parent_name = os.getenv('DT_PARENT_NAME')
        self.parent_version = os.getenv('DT_PARENT_VERSION')
        self.file_name = os.getenv('DT_FILE_NAME')
        # self.rocket_channel = os.getenv('DT_ROCKET_CHANNEL')
        # self.rocket_url = os.getenv('DT_ROCKET_URL', 'http://chat.misa.local:3000')
        self.ssl_verification = bool(strtobool(os.getenv('DT_SSL_VERIFY', 'true')))

    def check_import_bom(self):
        error_string = ''
        if self.url is None:
            error_string = 'DT_URL is missing'
        if self.api_key is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DT_API_KEY is missing'
        if self.project_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DT_PROJECT_NAME is missing'
        if self.project_version is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DT_PROJECT_VERSION is missing'
        if self.file_name is None:
            if error_string != '':
                error_string = error_string + ' / '
            error_string = error_string + 'DT_FILE_NAME is missing (XML file format)'
        # if self.rocket_channel is None:
        #     if error_string != '':
        #         error_string = error_string + ' / '
        #     error_string = error_string + 'DT_ROCKET_CHANNEL is missing (XML file format)'
        # if self.parent_name is None:
        #     if error_string != '':
        #         error_string = error_string + ' / '
        #     error_string = error_string + 'DT_PARENT_NAME is missing'
        # if self.parent_version is None:
        #     if error_string != '':
        #         error_string = error_string + ' / '
        #     error_string = error_string + 'DT_PARENT_VERSION is missing'
        if len(error_string) > 0:
            raise Exception(error_string)

        print('<--- DT-REIMPORT --->\n')
        print('DT_URL:                       ', self.url)
        print('DT_PROJECT_NAME:              ', self.project_name)
        print('DT_PROJECT_VERSION:           ', self.project_version)
        print('DT_PARENT_NAME:               ', self.parent_name)
        print('DT_PARENT_VERSION:            ', self.parent_version)
        print('DT_FILE_NAME:                 ', self.file_name)
        # print('DT_ROCKET_CHANNEL:            ', self.rocket_channel)
        # print('DT_ROCKET_URL:                ', self.rocket_url)
        print('')