from flask import Flask, g, jsonify
import sqlite3
import sys
sys.path.append('./api')
from home import get_company_data
DB_PATH = 'database/data.db'

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return "hello"
    # db = get_db()
    # cursor = db.cursor()
    # cursor.execute('SELECT * FROM my_table')
    # rows = cursor.fetchall()
    # return str(rows)

@app.route('/api/companies',methods=["GET"])
def get_company_list():
    return jsonify(get_company_data())

if __name__ == '__main__':
    app.run()
