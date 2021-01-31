from utils.redshift_connection import PandasClient
from datetime import datetime
import pandas as pd

__doc__ = 'For first element in json no table name , manualy adding it ' \
          'First step : orginize data from json file to dict  table_name :{[data]}' \
          'Second step : load data to dataframe and create stg tables'

orginized_dict = {}
def orginize_data(table_name,json_data,parent_id=None):
    l = {}

    for k, v in json_data.items():
        if str(k).endswith('id'):
            parent_id = {k:v}

        if isinstance(v, list):
            for val in v:
                val.update(parent_id)
                orginize_data(table_name=k,json_data=val,parent_id=parent_id)
        else:
            l.update({k: v})

    if table_name not in orginized_dict:
        orginized_dict[table_name] = [l]
    elif table_name  in orginized_dict:
        orginized_dict[table_name].append(l)


#load to stg
def load():
    for table_name,data in orginized_dict.items():
        df = pd.DataFrame(data)
        df.to_sql(table_name, PandasClient.conn, index=False, if_exists='replace') #always clean stg tables
        print(f'{datetime.now()}: stg {table_name} loaded ')
