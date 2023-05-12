from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)
CORS(app)
status = False
LED_PIN = 17
def setup():
    global status
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT)
    
    if (status==True):
        GPIO.output(LED_PIN, GPIO.HIGH)

@app.route('/', methods=['GET'])                                                     
def index():
    """Garanta que o arquivo index_cliente_api.html esteja no diretório "templates" """
    return render_template('index_cliente_api.html')      

@app.route('/altera/', methods=['PUT'])
def altera_led():
    global status, LED_PIN
    if (status):
        GPIO.output(LED_PIN, GPIO.LOW)
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)
    status=not(status)
    status_led_pin={True: 'ligado', False: 'desligado'}[status]
    return make_response(jsonify({'status': status_led_pin})), 200 #retorna resposta em formato JSON

@app.route('/led/status/', methods=['GET'])
def led():
    global status
    status_led_pin={True: 'ligado', False: 'desligado'}[status]
    return jsonify({'status': status_led_pin}), 200 #retorna resposta em formato JSON

if __name__ == '__main__':
    setup()
    socketio.run(app, host='0.0.0.0', port='5000')