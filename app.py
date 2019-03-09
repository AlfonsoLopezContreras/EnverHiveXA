from flask import Flask
from flask import render_template
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('firstpage.html', log = log[0])


@app.route('/report/<hive_id>')
def read_report(hive_id):
    print('Report from from: ' + str(hive_id))
    return 'HOLA'


@app.route('/notify/<hive_id>')
def run_notification(hive_id):
    print('Notification from: ' + str(hive_id))
    log.append('notification' + str(hive_id))
    return 'HOLA'


log = []
client = MongoClient('localhost', 27017)
db = client.test_database
if __name__ == '__main__':
    app.run()
