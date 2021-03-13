from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from threading import Timer
import sys

from flask import Flask, render_template
app = Flask(__name__)

data = [
    {
        'Database_Name': 'brm_ods',
        'table_name': 'item_t',
        'row_count': 200,
        'is_having_special_ch_table_name': False,
        'primary_keys_columns': ['pk_1', 'pk_2'],
        'date_pulled': 'March 12, 2021'
    },
    {
        'Database_Name': 'brm_ods',
        'table_name': 'item_t_incremental',
        'row_count': 220,
        'is_having_special_ch_table_name': False,
        'primary_keys_columns': ['pk_3', 'pk_4'],
        'date_pulled': 'March 12, 2021'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', data = data)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


def ui(location):
    qt_app = QApplication(sys.argv)
    web = QWebEngineView()
    web.setWindowTitle("Automation App")
    web.resize(900, 800)
    web.setZoomFactor(1.5)
    web.load(QUrl(location))
    web.show()
    sys.exit(qt_app.exec_())

if __name__ == "__main__":
    # Timer(1, lambda: ui("http://127.0.0.1:5000/")).start()
    app.run(debug=True)