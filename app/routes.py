
from flask import Blueprint, jsonify, request

main = Blueprint("main", __name__)

MAX_MESSAGE_LENGTH = 500


@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@main.route("/api/chat", methods=["POST"])
def chat():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    message = data.get("message")

    if not isinstance(message, str):
        return jsonify({"error": "Message must be a string"}), 400

    message = message.strip()

    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    if len(message) > MAX_MESSAGE_LENGTH:
        return jsonify({"error": "Message is too long"}), 400

    return jsonify({
        "response": f"Mock financial assistant response: {message}"
    }), 200
