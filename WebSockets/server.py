import logging
from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit                                      
from gpiozero import PWMLED, Device
from gpiozero.pins.pigpio import PiGPIOFactory
#import pigpio


# Inicializa Logging
logging.basicConfig(level=logging.WARNING)  # Configuração Global de logging
logger = logging.getLogger('main')  # Logger deste módulo
logger.setLevel(logging.INFO) # Debugging for this file.


# Inicializa GPIO
Device.pin_factory = PiGPIOFactory() # "seta" gpiozero para usar pigio por padrão


# Variáveis globais do Flask e Flask Restful
app = Flask(__name__) # Núcleo de uma aplicação Flask
socketio = SocketIO(app)                 


# Variáveis globais
LED_GPIO_PIN = 21
led = None # Instância PWMLED Instance. See inicia_led()
estado = {
    'level': 50 # 0..100 % de brilho do LED
}

"""
Funções da GPIO
"""
def inicia_led():
    """Cria e inicializa um objeto PWMLED"""
    global led
    led =  PWMLED(LED_GPIO_PIN)
    led.value = estado['level'] / 100


"""
Funções do Flask e Flask-SocketIO
"""

# Servindo os dados para nossa página HTML.
@app.route('/', methods=['GET'])
def index():
    """Garanta que index.html está no diretório templates """
    return render_template('index.html', pin=LED_GPIO_PIN)                 


# Manipuladores de Callback do Flask-SocketIO
@socketio.on('connect')                                                              
def handle_connect():
    """Chamado quando um cliente web socket remoto conecta a este servidor"""
    logger.info(f"Cliente {request.sid} conectado.")                          

    # Envia data iniciais ao novo cliente conectado.
    emit("led", estado)                                                               


@socketio.on('disconnect')                                                           
def handle_disconnect():
    """Chamado quando um cliente desconecta"""
    logger.info(f"Cliente {request.sid} desconetctado.")


@socketio.on('led')                                                                  
def handle_state(data):                                                              
    """Manipula mensagens 'led' para controlar o LED"""
    global state
    logger.info(f"Atualização do LED pelo cliente {request.sid}: {data} ")

    if 'level' in data and data['level'].isdigit():                                  
        new_level = int(data['level']) # data é uma string

        # Validaçáo do "range" de valores de porcentagem
        if new_level < 0:                                                            
            new_level = 0
        elif new_level > 100:
            new_level = 100

        # Seta a função do ciclo PWM para ajustar o brilho do LED.
        # Fazendo mapeamento de valores de entrada entre 0-100 para 0-1
        led.value = new_level / 100                                                  
        logger.info(f"Nível do brilho do LED é {str(new_level)}")

        estado['level'] = new_level

    # Envia um Broadcast do novo estado de brilho para todos que estão conectados ao servidor.
    emit("led", estado, broadcast=True)                                               


# Inicializa LED
inicia_led()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
