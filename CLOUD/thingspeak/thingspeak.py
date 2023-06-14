'''
Conecta ao serviço Matlab ThinkSpeak para enviar dados do uso da CPU.
Para mais informações, ler: https://nothans.com/thingspeak-tutorials/update-a-thingspeak-channel-using-mqtt-on-a-raspberry-pi
'''

from paho.mqtt import client as mqtt_client
from time import sleep
import sys, logging, signal, psutil, configparser


# Inicializa Logging
logging.basicConfig(level=logging.WARNING)  # configuração global de logging
logger = logging.getLogger("main")  
logger.setLevel(logging.INFO) 


config = configparser.ConfigParser()
#Lê arquivo com as configurações
config.read('config.ini')


broker = config['broker']
porta = config['porta'] #Estaremos conectando ao broker MQTT através do protocolo websocket
topico=f"channels/{config['id_canal']}/publish"
username=config['id_cliente']
password=config['senha']
id_cliente = config['id_cliente']
cliente = mqtt_client.Client(id_cliente, transport='websockets') #método de transporte: websocket

def publish():
    global cliente, topico
    count_msg=1
    try:
        while True:
            msg= psutil.cpu_percent(interval=3) #recebe a procentagem de utilização da CPU
            msg=f'field1={msg}'
            result = cliente.publish(topico, msg)
            status = result[0]
            sleep(20)
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
    global cliente, broker, porta, username, password    
    try:
        cliente.username_pw_set(username, password)
        cliente.connect(broker, porta)
        publish() 
    except:
        sys.exit(f"Erro ao conectar ao broker {broker}, porta {porta}")    


if __name__ == "__main__":
    mqtt_init()
