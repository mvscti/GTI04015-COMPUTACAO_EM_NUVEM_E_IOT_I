"""
Um servidor HTTP RESTFul API para controlar um LED utilizando Flask-RESTFul
A HTTP RESTFul API server to control an LED built using Flask-RESTful.
Créditos: https://github.com/PacktPublishing/Practical-Python-Programming-for-IoT/blob/master/chapter03/flask_api_server.py

"""
import logging
from flask import Flask, request, render_template                                    
from flask_restful import Resource, Api, reqparse, inputs                           
from gpiozero import PWMLED, Device                                                  
from gpiozero.pins.pigpio import PiGPIOFactory
from flask_socketio import SocketIO

# Inicializa Logging
logging.basicConfig(level=logging.WARNING)  # configuração Global de logging
logger = logging.getLogger('main')  
logger.setLevel(logging.INFO) 


# Inicializa GPIOZero
Device.pin_factory = PiGPIOFactory() # "seta" GPIOZero para usar PiGPIO por padrão

# Variáveis de Instância do Flask e Flask-RESTful
app = Flask(__name__) # Core Flask app.                                              
api = Api(app)                               
socketio = SocketIO(app)

# variáveis globais
LED_GPIO_PIN = 21
led = None # Instância de PWMLED (olhar init_led())
estado = {                                                                            
    'level': 50 # % de brilho do LED.
}

"""
Funções de controle da GPIO
"""
def init_led():
    """Cria e inicializa um objeto PWMLED"""
    global led
    led = PWMLED(LED_GPIO_PIN)
    led.value = estado['level'] / 100                                                 


"""
Funções para Flask e Flask-Restful
"""


@app.route('/', methods=['GET'])                                                     
def index():
    """Garanta que o arquivo index_cliente_api_pwm.html esteja no diretório "templates" """
    return render_template('index_cliente_api_pwm.html', pin=LED_GPIO_PIN)                


# Defições de recursos do Flask-restful
# Um 'recurso' é tratado como uma classe Python
class LEDControl(Resource):  

    def __init__(self):
        self.args_parser = reqparse.RequestParser()                                  

        self.args_parser.add_argument(
            name='level',  # Nome do argumento
            required=True,  # Argumento obrigatório
            type=inputs.int_range(0, 100),  # 'Range' varia de 0 a 100
            help='\'Seta\' o nível de brilho do LED {error_msg}',
            default=None)


    def get(self):
        """ Trata as requisições HTTP GET para retonar o estado atual do LED"""
        return estado 


    def post(self):
        """Trata requsioções HTTP POST para 'seta' o brilho do nível do LED"""
        global estado                                                                 

        args = self.args_parser.parse_args()                                         

        # 'Seta' o PWM duty cycle para ajustar o nível de brilho
        estado['level'] = args.level                                                  
        led.value = estado['level'] / 100                                             
        logger.info("O nível de brilho do LED brightness é " + str(estado['level']))

        return estado                                                                 



init_led()
# Registra o recurso Flask-RESTful e habilita o endpoint /led
api.add_resource(LEDControl, '/led')                                                 

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port='5000')