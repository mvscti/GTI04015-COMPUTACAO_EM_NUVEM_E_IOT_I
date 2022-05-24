import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Leia mais detalhes aqui (https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/)
GPIO.setwarnings(False) #desabilita mensagens de Warning
LED_PIN = 17 #pino conectado ao LED
BUZZER_PIN = 27 #pino conectado ao buzzer
#Configurando entradas e saídas
GPIO.setup(LED_PIN, GPIO.OUT) #define que o pino LED_PIN será como saída
GPIO.setup(BUZZER_PIN, GPIO.OUT) #define que pino BUZZER_PIN será como saída
#Acionando os componentes ligados na placa
GPIO.output(LED_PIN, GPIO.HIGH) #acende o led
GPIO.output(BUZZER_PIN, GPIO.HIGH) #buzzer emite som
time.sleep(5)
# "Desligando" os componentes ligados na placa
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.output(BUZZER_PIN, GPIO.LOW)
GPIO.cleanup() #libera a utilização da placa (permite que outros scripts possam utilizar a placa)