from flask import jsonify
import sqlite3

from argen.db import get_db

def json(sql):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql)
    cols = [x[0] for x in cur.description]
    filas = cur.fetchall()
    data = []
    for fila in filas:
        e = {}
        cnt = 0
        for c in cols:
            e[c] = fila[cnt]
            cnt += 1
        data.append(e)
    return jsonify({'total': len(filas), 'datos': data})


def html(h1, sql):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql)
    cols = [x[0] for x in cur.description]
    filas = cur.fetchall()

    header = '<h1>%s (%s)</h1><hr>' % ( h1.title(), len(filas))
    tabla = '<table class="table table-sm table-bordered table-striped table-hover">'

    tabla += '<thead>'
    tabla += '<tr>'
    for col in cols:
        tabla += '<th>%s</th>' % (col.title(),)
    tabla += '</tr>'
    tabla += '</thead>'

    tabla += '<tbody>'
    for fila in filas:
        tabla += '<tr onclick="alert(this.cells[0].innerText)">'
        cnt = 0
        for c in cols:
            if isinstance(fila[cnt], str):
                tabla += '<td>%s</td>' % (fila[cnt].title(),)
            else:
                tabla += '<td>%s</td>' % (fila[cnt],)
            cnt += 1
        tabla += '</tr>'
    tabla += '</tbody>'
    tabla += '</table>'
    
    return genhtml(header,tabla)

def sfunc(sql):
    cmd = "Select %s" % (sql, )
    conn = get_db()
    cur = conn.cursor()
    p = ""
    try:
        filas = cur.execute(cmd, multi=True)
        for fila in filas:
            for col in fila:
                print(col[0])
                p = col[0]
        return p
    except Exception as e:
        return None

def htmlproc(h1, sql, args):
    cmd = 'Call %s (%s);' % (sql, args)
    conn = get_db()
    cur = conn.cursor()
    try:
        filas = cur.execute(cmd, multi=True)
        (tabla,cnt) = gentabla(filas)
        header = '<h1>%s (%s)<h1><hr>' % (h1,cnt) 
    except mysql.connector.Error as err:
        pass

    return genhtml(header,tabla)

def jsonproc(sql, args):
    cmd = 'Call %s (%s);' % (sql, args)
    conn = get_db()
    cur = conn.cursor()
    try:
        filas = cur.execute(cmd, multi=True)
        (cnt, datos) = genjson(filas)
    except mysql.connector.Error as err:
        pass

    return jsonify({'total': cnt, 'datos': datos})

def gentabla(filas):
    cnt = 0
    tabla = '<table class="table table-bordered table-striped table-hover">'
    try:
        for fila in filas:
            if cnt == 0:
                tabla += '<thead class="thead-dark">'
                tabla += '<tr>'
                for column in fila.column_names:
                    tabla += '<th>%s</th>' % (column,)
                tabla += '</tr>'
                tabla += '</thead>'
                cnt = 1
            tabla += '<tbody>'
            for c in fila:
                tabla += '<tr onclick="alert(this.cells[0].innerText)">'
                for d in c:
                    if isinstance(d, str):
                        tabla += '<td>%s</td>' %(d.title(),)
                    else:
                        tabla += '<td>%s</td>' %(d,)
                tabla += '</tr>'
                cnt += 1
            tabla += '</tbody>'
        warnings = cursor.fetchwarnings()
        if warnings:
            for warning in warnings:
                print('warning',warning)
    except Exception as e:
        pass
    tabla += '</table>'
    return (tabla, cnt)

def genhtml(header,tabla):
    html = '<DOCTYPE html>'
    html = '<head>'
    html += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">'
    html += '</head>'
    html += '<body class="container">'
    html += header
    html += tabla
    html += '</body>'
    html += '</html>'
    return html

def genjson(filas):
    cnt = 0
    data = []
    cols = []
    try:
        for fila in filas:
            e = {}
            if cnt == 0:
                cols = [ col for col in fila.column_names ]
                cnt = 1

            for elem in fila:
                cnt += 1
                e = dict(zip(cols,elem))
                data.append(e)
    except Exception as e:
        pass
    return (cnt,data)

