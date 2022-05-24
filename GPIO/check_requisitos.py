"""
Este script em Python checa a disponibilidade de bibliotecas. Créditos:
(https://github.com/PacktPublishing/Practical-Python-Programming-for-IoT)

Dependências:
  pip3 install gpiozero pigpio
Construído e testado com Python 3.7 em Raspberry Pi 4 Modelo B
"""
try:
    import gpiozero
    print('GPIOZero   indisponível')
except:
    print('GPIOZero indisponível. Instale com "pip install gpiozero"')

try:
    import pigpio
    print('PiGPIO Disponível')
except:
    print('PiGPIO Indisponível. Instale com "pip install pigpio"')