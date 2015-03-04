import sqlite3
from flask import Flask
from flask import g
from string import join

DATABASE = './ctron.db'

app = Flask(__name__)

# DB handling
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Routes
@app.route('/')
def index():
    cur = get_db().execute("select count(*)")
    count = cur.fetchone()
    cur.close()
    resp = join(("Hello, World! (", str(count), ")"))
    return resp

if __name__ == '__main__':
    app.run(
        debug=True,
   #     host="0.0.0.0",
   #     port=5080
    )

