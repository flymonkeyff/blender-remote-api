from flask import Flask, request, jsonify
import os

app = Flask(__name__)

status_data = {
    "frame": 0,
    "total": 0,
    "is_rendering": False
}
command_queue = []

@app.route('/')
def home():
    return "✅ Blender Remote API is live!", 200

@app.route('/status', methods=['POST'])
def update_status():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    status_data.update(data)
    return jsonify({"message": "Status updated"}), 200

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(status_data), 200

@app.route('/command', methods=['POST'])
def send_command():
    command = request.json.get("command")
    if not command:
        return jsonify({"error": "No command provided"}), 400
    command_queue.append(command)
    return jsonify({"message": f"Command '{command}' queued"}), 200

@app.route('/poll', methods=['GET'])
def poll_command():
    if command_queue:
        return jsonify({"command": command_queue.pop(0)}), 200
    return jsonify({"command": None}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

