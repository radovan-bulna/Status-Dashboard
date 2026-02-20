import os
import platform
import logging
import signal
import sys
from flask import Flask, jsonify

# 1. Nastavenie logovania (DevOps Standard)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 2. Načítanie konfigurácie z ENV (alebo default)
APP_NAME = os.getenv("APP_NAME", "SkyWatch-Default")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

@app.route('/')
def home():
    logger.info("Hlavná stránka bola navštívená")
    return {
        "app_name": APP_NAME,
        "status": "Online",
        "container_metadata": {
            "os": platform.system(),
            "release": platform.release(),
            "hostname": platform.node()
        },
        "message": "Vítajte v produkčnej verzii dashboardu!"
    }

@app.route('/health')
def health():
    # Tu by mohla byť reálna kontrola (napr. pripojenie k DB)
    return jsonify(status="UP", database="connected"), 200

# 3. Graceful Shutdown handler
def signal_handler(sig, frame):
    logger.info("Prijatý signál na ukončenie. Čistím zdroje...")
    # Tu by si zatváral DB spojenia
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == '__main__':
    logger.info(f"Štartujem aplikáciu {APP_NAME}...")
    app.run(host='0.0.0.0', port=5000, debug=DEBUG_MODE)
