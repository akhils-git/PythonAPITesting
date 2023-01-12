from flask import Flask
from datetime import datetime

app = Flask(__name__)

print("Python Api Running...")


@app.route("/")
def hello():
    # print('Base called')
    api_log("Base called")
    return "Hello, World!"


@app.route("/api/getname/<name>")
def getname(name):
    api_log("Getname called")
    return "Hi" + name


def api_log(text):
    logFile = open("log_file.txt", "a")  # append mode
    logFile.write(text+" "+str(datetime.now())+"\n")
    logFile.close()


# app.run(debug=True, port=5000)
app.run(host='0.0.0.0', port=5000)
