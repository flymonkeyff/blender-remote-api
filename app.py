from flask import Flask, request, jsonify

app = Flask(__name__)
status_data = {
    "frame": 0,
    "total": 0,
    "is_rendering": False
}
command_queue = []

@app.route('/')
def hello():
    return "Blender Remote API is running!"

@app.route('/status', methods=['POST'])
def update_status():
    data = request.json
    status_data.update(data)
    return jsonify({"message": "status updated"})

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(status_data)

@app.route('/command', methods=['POST'])
def send_command():
    command = request.json.get("command")
    if command:
        command_queue.append(command)
        return jsonify({"message": f"command '{command}' queued"})
    return jsonify({"error": "no command provided"}), 400

@app.route('/poll', methods=['GET'])
def poll_command():
    if command_queue:
        return jsonify({"command": command_queue.pop(0)})
    return jsonify({"command": None})
