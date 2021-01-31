import os
from datetime import datetime
from utils.redshift_connection import RedshiftClient

stg2dwh_scripts =['employees.sql','employees.sql','stores.sql']

def load(SQL_SCRIPT_PATH):
    redshift_client = RedshiftClient()

    for script in stg2dwh_scripts:
        path = os.path.join(SQL_SCRIPT_PATH,script)
        script_content = open(path).read()
        redshift_client.execute(script_content)
        print(f'{datetime.now()}: dwh {script} loaded ')

    redshift_client.close()
