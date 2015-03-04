from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash
from werkzeug import check_password_hash

DATABASE = './data/ctron.db'

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'y\xf1\\\xd9u\xe1\xf6\xa9[\xc0\x99\xac\xb0\xc3\x16t\x06S;\xb4\xc9r\xc9Y'


# DB handling
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        g._database = db
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_user_id(username):
    # Convenience method to look up the id for a username
    rv = query_db('select user_id from user where username = ?', [username], one=True)
    return rv[0] if rv else None

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = query_db('select * from user where user_id = ?', str(session['user_id']), one=True)

# Routes
@app.route('/')
def index():
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template('home.html')

@app.route('/sensor')
def sensor():
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template('sensor.html', sensors=query_db('select * from sensor'))

@app.route('/relay')
def relay():
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template('relay.html', relays=query_db('select * from relay'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Logs the user in.
    if g.user:
        return redirect(url_for('index'))

    error = None
    if request.method == 'POST':
        user = query_db('''select * from user where
            username = ?''', [request.form['username']], one=True)
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['pw_hash'], request.form['password']):
            error = 'Invalid password'
        else:
            flash('You were logged in')
            session['user_id'] = user['user_id']
            return redirect(url_for('index'))

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """Logs the user out."""
    flash('You were logged out')
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5050
    )

