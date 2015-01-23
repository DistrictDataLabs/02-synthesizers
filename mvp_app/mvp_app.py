#District Datalabs Incubator 2015
#The Synthesizers
#MVP app
#
#Source: http://flask.pocoo.org/docs/0.10/tutorial/setup/#tutorial-setup

import sqlite3
from mvp_db import qry_drop_table, qry_create_table, qry_insert_basic
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


#configuration
DATABASE = 'basic.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create application
app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('MVP_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
            db.cursor().executescript(qry_drop_table)
            db.cursor().executescript(qry_create_table)
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


#views with routes
#seperate view from routes for later versions
@app.route('/')
def show_entries():
    cur = g.db.execute('select name_last, name_first, gender from basic order by name_last desc')
    entries = [dict(name_last=row[0], name_first=row[1], gender=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into basic (name_last, name_first, gender) values (?, ?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('entry posted')
    return redirect(url_for('show_entries'))

#log in log out
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
