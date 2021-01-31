import psycopg2
from sqlalchemy import create_engine
from utils.authentication import ConnectionStrings


class PandasClient:
    conn = create_engine(ConnectionStrings.sqlalchemy)


class RedshiftClient:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(ConnectionStrings.postgres)
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise e

    def execute(self,query):
        self.cursor.execute(query)
        self.commit()


    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()



