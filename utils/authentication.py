
HOST = 'db.panoply.io'
DB_NAME = 'stas_db'
PORT = '5439'
USER = "tsvayg1@gmail.com"
PASSWORD = "Stasek123"


class ConnectionStrings:
    sqlalchemy = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
    postgres = f"dbname={DB_NAME} host={HOST} port={PORT} user={USER}  password={PASSWORD}"
