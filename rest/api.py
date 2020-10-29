import flask
from flask import request, jsonify
from datetime import datetime
from datetime import timedelta
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Mock API Service</h1>
<p>A simple REST API to performance test strange Tower use cases.</p>'''


@app.route('/api/v1/jobs/submit_short', methods=['POST'])
def api_submit_short():
    conn = sqlite3.connect('requests.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    current_time = datetime.now()
    termination = current_time + timedelta(seconds=2)
    sql_statement = "INSERT INTO requests(request_duration,request_timestamp,request_termination) VALUES (?,?,?);"
    data_tuple = (100, current_time, termination)
    insert_row = cur.execute(sql_statement, data_tuple)
    conn.commit()
    conn.close()
    return jsonify({'id': insert_row.lastrowid})


@app.route('/api/v1/jobs/submit_long', methods=['POST'])
def api_submit_long():
    conn = sqlite3.connect('requests.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    current_time = datetime.now()
    termination = current_time + timedelta(seconds=60)
    sql_statement = "INSERT INTO requests(request_duration,request_timestamp,request_termination) VALUES (?,?,?);"
    data_tuple = (100, current_time, termination)
    insert_row = cur.execute(sql_statement, data_tuple)
    conn.commit()
    conn.close()
    return jsonify({'id': insert_row.lastrowid})


@ app.route('/api/v1/jobs/query', methods=['GET'])
def api_get_status():
    request_id = request.args.get('id')
    conn = sqlite3.connect('requests.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    select_row = cur.execute(
        "SELECT request_termination FROM requests WHERE id=?", (request_id,))
    row = cur.fetchone()
    conn.close()
    if (row != None):
        current_time = datetime.now()
        termination_time = datetime.fromisoformat(row['request_termination'])
        if (current_time < termination_time):
            return_status = 'pending'
        else:
            return_status = 'finished'
    else:
        return_status = 'empty'
    return jsonify(status=return_status)
