__version__ = "3.1.0"

import os
from flask import Flask, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:path>")
def files(path):
    # Serve the existing web app (HTML/CSS/JS/assets) from the app bundle.
    full = os.path.join(BASE_DIR, path)
    if os.path.isfile(full):
        return send_from_directory(BASE_DIR, path)
    return ("Not Found", 404)

if __name__ == "__main__":
    # python-for-android's WebView bootstrap opens the configured local port.
    # Debug/reloader must stay disabled on Android.
    app.run(host="127.0.0.1", port=5000, debug=False, threaded=True, use_reloader=False)
