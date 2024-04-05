from flask import Flask, request, render_template
from tinydb import TinyDB
from datetime import datetime

app = Flask(__name__)
db = TinyDB('web-app/database.json')

resposta_pong = '{"resposta": "pong"}'

@app.route('/ping')
def ping():

    hora = str(datetime.now())
    db.insert({"hora": hora, "tipo_de_requisicao": request.method})
    return render_template('ping.html')

@app.route('/pong')
def pong():
    return f'<p>{resposta_pong}</p>'

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    return render_template('echo.html')

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')