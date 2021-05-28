import functools
from flask import ( Blueprint, g )
from argen.utiles import (json, html, htmlproc, jsonproc, sfunc)

bp = Blueprint('argen',__name__, url_prefix='/argen')


@bp.route('/html/escuelas/<provincia>')
def spprovinciahtml(provincia):
    sql = "sp_Escuelas"
    return htmlproc('Escuelas por provincia: %s' % (provincia.title(),), sql, provincia)

@bp.route('/json/escuelas/<provincia>')
def spprovinciajson(provincia):
    sql = "sp_Escuelas"
    return jsonproc(sql, provincia)

@bp.route('/json/escuelas/contar/')
def jsoncuantas():
    sql = """
    select j.nombre as Provincia, s.nombre as Sector, count(*) as total
    from NEscuelas ne
    inner join Localidad l
        on l.id = ne.localidad_id
    inner join Departamento d
        on d.id = l.departamento_id
    inner join Jurisdiccion j
        on j.id = d.jurisdiccion_id
    inner join Sector s
        on s.id = ne.sector_id
    group by j.nombre, s.nombre
    order by 1,2
    """
    return json(sql)

@bp.route('/html/escuelas/contar/')
def htmlcuantas():
    sql = """
    select j.nombre as Provincia, s.nombre as Sector, count(*) as total
    from NEscuelas ne
    inner join Localidad l
        on l.id = ne.localidad_id
    inner join Departamento d
        on d.id = l.departamento_id
    inner join Jurisdiccion j
        on j.id = d.jurisdiccion_id
    inner join Sector s
        on s.id = ne.sector_id
    group by j.nombre, s.nombre
    order by 1,2
    """
    return html('Cantidad de Escuelas', sql)

@bp.route('/json/ambito')
def jsonambito():
    sql = """
    select * from Ambito 
    """
    return json(sql)

@bp.route('/html/ambito')
def htmlambito():
    sql = """
    select * from Ambito
    """
    return html('ambito', sql)

@bp.route('/json/sector')
def jsonsector():
    sql = """
    select * from Sector 
    """
    return json(sql)

@bp.route('/html/sector')
def htmlsector():
    sql = """
    select * from Sector
    """
    return html('sector', sql)

@bp.route('/json/provincias')
def provinciasjson():
    sql = """
    select * from Jurisdiccion
    """
    return json(sql)

@bp.route('/html/provincias')
def provinciashtml():
    sql = """
    select * from Jurisdiccion
    """
    return html('provincias', sql)

@bp.route('/json/departamentos')
def departamentosjson():
    sql = """
    select d.id, j.nombre As Provincia, d.codigo as Codigo, d.nombre as Departamento
    from Departamento d
    inner join Jurisdiccion j
        on j.id = d.jurisdiccion_id
    order by 2,4
    """
    return json(sql)

@bp.route('/html/departamentos')
def departamentoshtml():
    sql = """
    select d.id, j.nombre As Provincia, d.codigo as Codigo, 
    d.nombre as Departamento
    from Departamento d
    inner join Jurisdiccion j
        on j.id = d.jurisdiccion_id
    order by 2,4
    """
    return html('departamentos', sql)

@bp.route('/html/escuelas/tiposeducacion')
def tiposeducacionhtml():
    sql = """
    select
    cast(sum(case when Comun = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Común",
    cast(sum(case when Especial = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as Especial,
    cast(sum(case when Adultos = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as Adultos,
    cast(sum(case when Artistica = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Artística",
    cast(sum(case when Hospitalaria = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as Hospitalaria,
    cast(sum(case when Intercultural = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Bilingüe",
    cast(sum(case when Carcelaria = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Contexto de Encierro",
    cast(count(*) as VARCHAR(10)) as "Total"
    from Modalidades 
    """
    return html('Escuelas por Tipo de Educación', sql)

@bp.route('/json/escuelas/tiposeducacion')
def tiposeducacionjson():
    sql = """
    select
    cast(sum(case when Comun = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Común",
    cast(sum(case when Especial = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as Especial,
    cast(sum(case when Adultos = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as Adultos,
    cast(sum(case when Artistica = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Artística",
    cast(sum(case when Hospitalaria = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as Hospitalaria,
    cast(sum(case when Intercultural = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Bilingüe",
    cast(sum(case when Carcelaria = '1' THEN 1 ELSE 0 End) as VARCHAR(10))as "Contexto de Encierro",
    cast(count(*) as VARCHAR(10)) as "Total"
    from Modalidades 
    """
    return json(sql)

@bp.route('/nombreprovincia/<provinciaid>')
def getnombreprovincia(provinciaid):
    data = getprovincia(provinciaid)
    print('getnombreprovincia', provinciaid, data)
    return data



def getprovincia(id):
    sql = """ fn_Provincia(%s) """ % (id, )
    data = sfunc(sql)
    print('getprovincia', sql, data)
    return data
