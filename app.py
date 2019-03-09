from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('firstpage.html')

@app.route('report/<hive_id>')
def read_report(hive_id):


@app.route('/notify/<hive_id')
def run_notification(hive_id):
    print('Notification from: ' + str(hive_id))


if __name__ == '__main__':
    app.run()
