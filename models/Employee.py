from config.db import meta
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

employee = Table(
    'employee', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('email', String(100)),
    Column('age', String(10)),
    Column('country', String(100)),
    Column('created_at', TIMESTAMP),
    Column('updated_at', TIMESTAMP),
)