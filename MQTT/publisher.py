from paho.mqtt import client as mqtt_client
from random import randint
from time import sleep
import sys, logging, signal, psutil

# Inicializa Logging
logging.basicConfig(level=logging.WARNING)  # configuração global de logging
logger = logging.getLogger("main")  
logger.setLevel(logging.INFO) 

##Alguns brokers públicos: mqtt.eclipseprojects.io, broker.hivemq.com
broker = 'localhost'
porta = 1883
topico='/iot/cpu-utilization/'
id_cliente = f'python-mqtt-{randint(0, 1000)}'
cliente = mqtt_client.Client(id_cliente)

def publish():
    global cliente, topico
    count_msg=1
    try:
        while True:
            msg= psutil.cpu_percent(interval=3) #recebe a procentagem de utilização da CPU
            result = cliente.publish(topico, msg)
            # resultado: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Enviando `{msg}` ao tópico `{topico}` - Mensagens enviadas: {count_msg}")
                count_msg +=1
            else:
                print(f"Falha ao enviar mensagem ao tópico {topico}") 
    except KeyboardInterrupt:
        print('Você presionou Control + C. Desligando, aguarde..')
        cliente.disconnect() #  Desconecta de forma 'graciosa' do Broker      
        exit(0) 


def mqtt_init():
    """Conecta ao broker MQTT"""
    global cliente, broker, porta     
    try:
        cliente.connect(broker, porta)
        publish() 
    except:
        sys.exit(f"Erro ao conectar ao broker {broker}, porta {porta}")    


if __name__ == "__main__":
    mqtt_init()