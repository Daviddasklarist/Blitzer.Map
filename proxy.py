from flask import Flask, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Aktiviert CORS für alle Routen

@app.route('/proxy')
def proxy():
    url = "http://direct.blitzer.de/export/v3/xml/?key=94b8b000-7f1f-483c-8f7f-2e75cecb7eb1"
    response = requests.get(url)
    return Response(response.content, content_type="application/xml")

if __name__ == "__main__":
    app.run(port=5000)
