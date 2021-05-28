import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
) 
from werkzeug.security import check_password_hash, generate_password_hash

from argen.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = db_get()
        error = None

        if not username:
            error = 'El usuario es requerido'
        elif not password:
            error = 'La password es requerida'
        elif db.execute(
            'select id from user where username = ?', (username,)
        ).fetchone() is not None:
            error = 'El usuario {username} a está registrado'

        if error is None:
            db.execute(
                'insert into user(username, password) values (?,?)',
                (username, generate_password_hash(password))
            )
            db.comit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html', title='Registrarse')


@bp.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = db_get()
        error = None
        user = db.execute(
            'select * from user where username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Usuarie Incorrecte'
        elif not check_password_hash(user['password'], password): 
            error = 'Password Incorrecte'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html', title='Ingresar')
 
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'select * from user where id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

