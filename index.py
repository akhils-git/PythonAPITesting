
from flask import Flask, jsonify, request
from datetime import datetime
# from calibration_predictor import calibrationController
from core.calibration_predictor import calibrationController
from file_manage import FileController

app = Flask(__name__)
cal = calibrationController()
file_controller = FileController()

print("Python Api Running...")


@app.route("/")
def hello():
    api_log_save("Homepage", "Running Good")
    return open('./pages/home.html', 'r')


@app.route('/api/getname/<name>', methods=['GET'])
def getname(name):
    api_log_save("getname", "Get name")
    return jsonify("Hi " + name + " Called at " + str(datetime.now()))


@app.route('/api/getlog', methods=['GET'])
def getlog():
    api_log_save("getlog", "Log Saved")
    logFile = open("./storage/log_file.txt", "r")
    return jsonify(logFile.read())


@app.route("/api/getcalibration/<min_sensor>/<min_weight>/<max_weight>")
def getcalibration(min_sensor, min_weight, max_weight):
    api_log_save("getcalibration", "Max value generated")
    return jsonify(cal.predict_max_value(min_sensor, min_weight, max_weight))


@app.route('/api/fileupload', methods=['POST'])
def upload_file():
    print(request.files)
    responce = file_controller.upload_file(request)
    api_log_save("fileupload", "Called")
    return responce


def api_log_save(api_name, message):
    logFile = open("./storage/log_file.txt", "a")  # append mode
    logFile.write(f"{api_name}|{message}|{str(datetime.now())}\n")
    logFile.close()


# app.run(debug=True, port=5000)
app.run(host='0.0.0.0', port=5000)
