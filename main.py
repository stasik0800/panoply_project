import os
import json
from flow import stg,dwh

#project conf
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE_PATH = os.path.join(ROOT_DIR, 'data_and_schema/ann_stock.json')
SQL_SCRIPT_PATH = os.path.join(ROOT_DIR, 'sql_scripts')


def main():
    with open(JSON_FILE_PATH) as f:
        json_data = json.load(f)

    try:
        stg.orginize_data(table_name='company',json_data=json_data) # for the first loop table_name set hardcoded
        stg.load()
    except Exception as e:
        print('failed on stg layer')
        raise e

    dwh.load(SQL_SCRIPT_PATH)

main()





