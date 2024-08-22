from flask import Flask, g, jsonify
import sqlite3
import sys
sys.path.append('./api')
from home import get_company_data, get_student_data # type: ignore
from insights import get_branchwise_insights, get_net_insights, get_bracketwise #type: ignore
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

@app.route('/api/students',methods=["GET"])
def get_student_list():
    return jsonify(get_student_data())

@app.route('/api/insights/branchwise',methods=["GET"])
def get_branchwise():
    return jsonify(get_branchwise_insights())

@app.route('/api/insights/cummulative',methods=["GET"])
def get_cummulative():
    return jsonify(get_net_insights())

@app.route('/api/insights/bracketwise',methods=["GET"])
def get_bracket_wise():
    return jsonify(get_bracketwise())
if __name__ == '__main__':
    app.run()
