import json
import re
import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from dt_reimport.environment import Environment

# Disable SSL Warnings
disable_warnings(InsecureRequestWarning)

# Fix for reimport without file, see https://github.com/psf/requests/issues/1081#issuecomment-428504128
class ForceMultipartDict(dict):
    def __bool__(self):
        return True

FORCE_MULTIPART = ForceMultipartDict()  # An empty dict that boolean-evaluates as `True`.

class Api:

    def __init__(self):
        self.environment = Environment()
        self.headers = {'X-Api_Key': self.environment.api_key, 'Content-type': 'multipart/form-data'}
        self.upload_bom_url = self.environment.url + '/api/v1/bom/'
        self.ssl_verification = self.environment.ssl_verification

    def reimport_bom(self):
        payload = {'autoCreate': True,
                   'projectName': self.environment.project_name,
                   'projectVersion': self.environment.project_version
                  }
        if self.environment.parent_name is not None:
            payload['parentName'] = self.environment.parent_name
        if self.environment.parent_version is not None:
            payload['parentVersion'] = self.environment.parent_version

        if self.environment.file_name is not None:
            files = {'bom': (self.environment.file_name,
                              open(self.environment.file_name, 'rb'),
                              'application/xml', {'Expires': '0'})}
            response = requests.post(self.upload_bom_url,
                                     headers=self.headers,
                                     data=payload,
                                     files=files,
                                     verify=self.ssl_verification)
        else:
            response = requests.post(self.upload_bom_url,
                                     headers=self.headers_without_json,
                                     data=payload,
                                     files=FORCE_MULTIPART,
                                     verify=self.ssl_verification)

        response.raise_for_status()
        if response.status_code == 200:
            print("Upload successfully!")
        else:
            if response.status_code == 404:
                print("=> Error: parentName hoặc versionName không tồn tại?")
            elif response.status_code == 401:
                print("=> Error: API Key không đúng")
            elif response.status_code == 403:
                print("=> Error: API Key không có quyền truy cập vào project.")
            elif re.match('5*', response.status_code):
                print("=> Error: Error Internal Server")
            print('Detail:' + response.text,end="\n")

        # Gửi thông báo về rocket chat:
        # - Tên job, build ID
        # - Thông tin lỗi
        

