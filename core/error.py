
from flask import jsonify


def not_found_error(error):
    return jsonify({"error": "Api Not Found"}), 404


def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405


def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500


def signature_verification_failed(error):
    return jsonify({"error": "Signature verification failed"}), 422
