from paho.mqtt import client as mqtt_client
from random import randint
import sys, logging, signal

# Inicializa Logging
logging.basicConfig(level=logging.WARNING)  # configuração global de logging
logger = logging.getLogger("main")  
logger.setLevel(logging.INFO) 

broker = 'localhost'
porta = 1883
topico='/iot/cpu-utilization/'
id_cliente = f'python-mqtt-{randint(0, 1000)}'
cliente = mqtt_client.Client(id_cliente)

#função utilizada pela biblioteca PAHO para determinar o comportamento ao se conectar ao broker
def on_connect(cliente, dados, flags, codigo_resultado):
    global topico
    if codigo_resultado == 0:
        print("Conectado ao Broker MQTT!")
    else:
        print("Erro ao conectar, código de retorno %d\n", codigo_resultado)
    cliente.subscribe(topico) #se increve no tópico '/iot/led/'

# Função utilizada quando uma message de PUBLISH é recebida do servidor
def on_message(cliente, dados, mensagem):
    print(f"Recebido do tópico '{mensagem.topic}'': {mensagem.payload.decode()}")

def manipula_sinal(sig, frame):
    """Captura Control+C e desconecta do Broker."""
    global cliente
    logger.info("Você presionou Control + C. Desligando, aguarde...")

    cliente.disconnect() #  Desconecta de forma 'graciosa' do Broker
    sys.exit(0)


def mqtt_init():
    """Conecta ao broker MQTT"""
    global cliente, broker, porta
    cliente.enable_logger() #Roteia as mensagens de logging do Paho para o logging do Python        
    cliente.on_connect = on_connect
    cliente.on_message = on_message
    cliente.connect(broker, porta)

mqtt_init()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, manipula_sinal)  # captura Control + C   
    logger.info("Escutando mensagens no tópico '" + topico + "'. Pressione Control + C para sair.")
    cliente.loop_start()
    signal.pause()
