from sqlalchemy import create_engine, MetaData

import pymysql
pymysql.install_as_MySQLdb()

SQLALCHEMY_DB_URL = "mysql+pymysql://root:password@localhost/py_crud"

engine = create_engine(SQLALCHEMY_DB_URL)

meta = MetaData()
con = engine.connect()