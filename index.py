
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

print("Python Api Running...")


@app.route("/")
def hello():
    # print('Base called')
    api_log_save("Base", "Running Good")
    return "Hello, World!"


@app.route('/api/getname/<name>', methods=['GET'])
def getname(name):
    api_log_save("getname", "Get name")
    return jsonify("Hi " + name + " Called at " + str(datetime.now()))


@app.route('/api/getlog', methods=['GET'])
def getlog():
    api_log_save("getlog", "Log Saved")
    logFile = open("log_file.txt", "r")
    return jsonify(logFile.read())


def api_log_save(api_name, message):
    logFile = open("log_file.txt", "a")  # append mode
    logFile.write(f"{api_name}|{message}|{str(datetime.now())}\n")
    logFile.close()


# app.run(debug=True, port=5000)
app.run(host='0.0.0.0', port=9000)
