import functools

from flask import ( Blueprint, g )

from argen.utiles import json

bp = Blueprint('db',__name__, url_prefix='/db')


@bp.route('/json/schemas')
def schemasjson():
    sql = """
    select distinct table_schema from information_schema.TABLES
    """
    return json(sql)

@bp.route('/json/tables/<schema>')
def tablesjson(schema ):
    sql = """
    select table_name from information_schema.TABLES
    where table_schema = '%s'
    """ % (schema,)
    return json(sql)

@bp.route('/json/columns/<schema>/<table>')
def columnsjson(schema, table):
    sql = """
    select ordinal_position, column_name,column_default,
    is_nullable, data_type, character_maximum_length,
    character_octet_length
    from information_schema.COLUMNS
    where table_schema = '%s'
      and table_name = '%s'
    order by ordinal_position
    """ % (schema,table)
    return json(sql)

@bp.route('/json/routines/<schema>')
def routinesjson(schema ):
    sql = """
    select routine_schema,routine_name, specific_name, routine_type 
    from information_schema.ROUTINES
    where routine_schema = '%s'
    """ % (schema,)
    return json(sql)

@bp.route('/json/code/<schema>/<routine>')
def routinescodejson(schema, routine):
    sql = """
    select routine_schema,routine_name, specific_name, 
    routine_type, routine_body,routine_definition
    from information_schema.ROUTINES
    where routine_schema = '%s'
      and routine_name = '%s'
    """ % (schema,routine)
    return json(sql)

@bp.route('/json/params/<schema>/<routine>')
def routinesparamsjson(schema, routine):
    sql = """
    select ordinal_position, parameter_mode, parameter_name, data_type
    from information_schema.PARAMETERS
    where specific_schema = '%s'
      and specific_name = '%s'
    order by ordinal_position
    """ % (schema,routine)
    return json(sql)

