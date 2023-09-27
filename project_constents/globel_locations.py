import os


class GlobelLocations:
    upload_path = 'storage/uploads/'
    log_path = 'storage/logs/'
    root_path = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(
        __file__))))


class Project:
    version = '1.0'
