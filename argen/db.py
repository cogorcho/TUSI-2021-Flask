import sqlite3
import mysql.connector
import pyodbc
from flask import current_app, g


def get_db_sqlite():
    if not 'db' in g:
        g.db = sqlite3.connect(
                current_app.config['SQLITE_DB'],
                detect_types = sqlite3.PARSE_DECLTYPES
                )
        g.db.row_factory = sqlite3.Row
    return g.db

def get_db_mysql():
    if not 'db' in g:
        g.db = mysql.connector.connect(
                user=current_app.config['MYSQL_USER'],
                password=current_app.config['MYSQL_PWD'],
                host=current_app.config['MYSQL_HOST'],
                database=current_app.config['MYSQL_DB'])
    return g.db

def get_db_mssql():
    if not 'db' in g:
        g.db = pyodbc.connect(
                'DRIVER={%s};SERVER=%s;DATABASE:%s;UID=%s;PWD=%s' %
                (current_app.config['MSSQL_DRIVER'],
                current_app.config['MSSQL_SERVER'],
                current_app.config['MSSQL_DB'],
                current_app.config['MSSQL_USER'],
                current_app.config['MSSQL_PWD']))
    return g.db

def get_db():
    current_db = current_app.config['CURRENT_DB']
    if current_db == 'MYSQL':
        return get_db_mysql()
    elif current_db == 'SQLITE':
        return get_db_sqlite()
    elif current_db == 'SQLSERVER':
        return get_db_mssql()


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
