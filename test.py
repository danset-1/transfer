from flask import Flask, url_for, render_template, jsonify, request
import webbrowser
#import pymongo
import csv
import json
import var
import importlib
import hm

# Creates Flask application named "app" and pass it the __name__,  which holds the name
# of the current python module, flask needs it for some work behind the scenes
app = Flask(__name__) 

# var.a = 0
# b = var.b
# y = var.y

####

@app.route('/') # Tells python it will work with a web browser (HTTP client)
def index():
    return render_template("index.html", newA = var.a, newB = var.b, newY = var.y )

@app.route('/data')
def data():
    hm.run_task()
    # Always return the *current* values from var.py
    importlib.reload(hm)
    return jsonify({
        "a": var.a,
        "b": var.b,
        "y": var.y,
        "t1": var.t1,
        "t2": var.t2
    })

@app.route('/r')
def r():
    hm.reset_task()
    return jsonify({
        "a": var.a,
        "b": var.b,
        "y": var.y,
        "t1": var.t1,
        "t2": var.t2
    })

@app.route('/stop')
def stop(id):
    hm.stop_task()
    return jsonify({
        "a": var.a,
        "b": var.b,
        "y": var.y,
        "t1": var.t1,
        "t2": var.t2
    })

@app.route('/signal_stop', methods=['POST'])
def signal_stop():
    data = request.get_json()
    id = data.get("id")
    #print(id)
    hm.stop_task(int(id))
    return jsonify({
        "a": var.a,
        "b": var.b,
        "y": var.y,
        "t1": var.t1,
        "t2": var.t2
    })

htmlLocation = 'http://127.0.0.1:5000'
webbrowser.open_new_tab(htmlLocation)

app.run()