from flask import Flask, jsonify
import os, platform, datetime

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "status": "Online",
        "environment": "Docker Container",
        "system_info": {
            "os": platform.system(),
            "node": platform.node(),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "devops_check": "CI/CD Pipeline is working!"
    }

@app.route('/health')
def health():
    return jsonify(status="UP"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
