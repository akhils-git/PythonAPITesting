
from flask import Flask, jsonify, request, send_file
from datetime import datetime
from core.file_manage import FileController
from project_constents.globel_locations import GlobelLocations, Project
from zipfile import ZipFile
import os
from core.error import not_found_error, method_not_allowed_error, internal_server_error
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
file_controller = FileController()
base_path = GlobelLocations()
project_details = Project()

app.register_error_handler(404, not_found_error)
app.register_error_handler(405, method_not_allowed_error)

# Configure JWT settings
# Change this to a strong, secret key
app.config['JWT_SECRET_KEY'] = '1234abcA'
jwt = JWTManager(app)

# Mock user data for demonstration (replace with your user data)
users = {
    'admin': {
        'password': '1234',
        'id': 1
    }, 'user': {
        'password': '6789',
        'id': 1
    }
}

print(f"Api Test Engine {project_details.version} Running...")
print(f"System Path: {base_path.root_path}")


@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and password == users[username]['password']:
        response = jsonify({"token": create_access_token(
            identity=username), "Username": username})
        return response
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@app.route("/")
def hello():
    api_log_save("Homepage", "Running Good")
    return open('./pages/home.html', 'r')


@app.route('/api/getname/<name>', methods=['GET'])
@jwt_required()
def getname(name):
    api_log_save("getname", "Get name")
    response = jsonify("Hi " + name + " Called at " + str(datetime.now()))
    response.status_code = 200
    response.headers['Location'] = "test"
    return response


@app.route('/api/getlog', methods=['GET'])
def getlog():
    api_log_save("getlog", "Log Saved")
    logFile = open(base_path.upload_path+"log_file.txt", "r")
    response = jsonify(logFile.read())
    response.status_code = 200  # Created status code
    response.headers['Location'] = "test"
    return response


@app.route('/api/fileupload', methods=['POST'])
def upload_file():
    # print(request.files)
    response = file_controller.upload_file(request)
    response.status_code = 200  # Created status code
    api_log_save("fileupload", "Called")
    return response


@app.route('/api/filelist', methods=['GET'])
def filelist():
    responce = file_controller.list_files()
    api_log_save("filelist", "Called")
    return responce


@app.route('/api/filedownload/<file_name>', methods=['GET'])
def filedownload(file_name):
    file_path = os.path.dirname(os.path.abspath(
        __file__)) + "\\" + base_path.upload_path + file_name
    file_path = os.path.normpath(file_path)
    client_filename = file_name
    return send_file(file_path, as_attachment=True, download_name=client_filename)

# @app.route('/api/filesdownload', methods=['GET'])
# def filedownload():
#    # Replace 'path_to_your_file' with the actual path to the file you want to send
#     file_path = 'storage/uploads/Car2.png'

#     # You can specify a custom filename for the client to save the file as (optional)
#     client_filename = 'Car2.png'

#     # Use send_file to send the file as a response
#     return send_file(file_path, as_attachment=True, download_name=client_filename)
#     return responce


@app.route('/api/downloadallfromstorage')
def download_all_from_storage():
    # Create a temporary zip file to store the files
    file_paths = os.listdir('storage/uploads/')
    zip_filename = 'downloaded_files.zip'
    with ZipFile(zip_filename, 'w') as zipf:
        for file_path in file_paths:
            # Add each file to the zip archive
            zipf.write('storage/uploads/'+file_path,
                       os.path.basename(file_path))
    # Send the zip file as a response
    return send_file(zip_filename, as_attachment=True, download_name='multiple_files.zip')


def api_log_save(api_name, message):
    logFile = open(base_path.log_path+"log_file.txt", "a")  # append mode
    logFile.write(f"{api_name}|{message}|{str(datetime.now())}\n")
    logFile.close()


# app.run(debug=True, port=5000)
app.run(host='0.0.0.0', port=5000)
