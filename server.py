from flask import Flask

app = Flask(__name__, template_folder = "frontend/templates", static_folder = "frontend/static", static_url_path="")

from routes.route import *

if __name__ == "__main__":
    host = "172.31.46.55"
    port = "80"
    app.run(host, port, debug=True)
    
    