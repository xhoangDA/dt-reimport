from dt_reimport.dt_api import Api
from dt_reimport.environment import Environment
import time

def dd_reimport_findings():
    try:
        environment = Environment()
        environment.check_import_bom()
        api = Api()
        time.sleep(1200)
        api.reimport_bom()
    except Exception as e:
        print(str(e))
        exit(1)

if __name__ == '__main__':
    dd_reimport_findings()
