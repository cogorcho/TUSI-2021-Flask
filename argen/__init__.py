from flask import Flask, g, jsonify, render_template
import os

configFile = 'config.py'

def check_instance_path(app):
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

def create_config(app, test_config=None):
    app.config.from_mapping(
            SECRET_KEY='dev',
            SQLITE_DB='sqlite/argento.sqlite',
            LOGFILE='logs/app.log',
            MYSQL_USER='argen',
            MYSQL_PWD='argen',
            MYSQL_HOST='192.168.1.139',
            MYSQL_DB='Argentina',
            MSSQL_DRIVER='ODBC Driver 17 for SQL Server',
            MSSQL_SERVER='192.168.1.108',
            MSSQL_DB='Tusi2021',
            MSSQL_USER='sa',
            MSSQL_PWD='Soler225',
            CURRENT_DB='MYSQL',
            JSON_AS_ASCII=False
    )
    if test_config is None:
        app.config.from_pyfile(configFile, silent=True)
    else:
        app.config.from_mapping(test_config)

def create_app(test_config=True):
    app = Flask(__name__, instance_relative_config=True)
    check_instance_path(app)
    create_config(app)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import informationschema
    app.register_blueprint(informationschema.bp)

    from . import escuelas
    app.register_blueprint(escuelas.bp)

    @app.route('/')
    @app.route('/inicio')
    def inicio():
        return render_template('index.html', title='Inicio')

    @app.route('/rutas')
    def rutas():
        return render_template('rutas.html', title='Rutas')


    return app
