"""
Programa que aciona o serviço dweet.io e recupera as últimas postagens.
Adaptação de código disponível do livro "Practical Python Programming for IoT". 
Repositório disponivel em:
https://github.com/PacktPublishing/Practical-Python-Programming-for-IoT

Dependências:
  pip3 install requests
Construído e testado em Python 3.7
"""
import signal
import sys
import logging
from time import sleep
import requests                                                                    


# Variáveis Globais
NOME_COISA = ''  # O nome da 'coisa'
URL = 'https://dweet.io'            # Dweet.io service API


# Initialize Logging
logging.basicConfig(level=logging.WARNING)  # Global logging configuration
logger = logging.getLogger('main')  # Logger for this module
logger.setLevel(logging.INFO)  # Debugging for this file.                           

def recebe_ultimo_dweet():
    global NOME_COISA
    """Recebe os últimos dweets da 'coisa'."""
    recurso = URL + '/get/latest/dweet/for/' + NOME_COISA                         
    logger.debug(f'Recebendo último dweet da url {recurso}')

    r = requests.get(recurso)                                                     

    #código de retorno foi bem sucedido?
    if r.status_code == 200:                                                       
        dweet = r.json()  # retorna um dicionário Python
        logger.debug(f"Último dweet para a coisa foi {dweet}")

        conteudo_dweet = None

        if dweet['this'] == 'succeeded':                                           
            # Nosso interesse [e apenas na propriedade conteúdo
            conteudo_dweet = dweet['with'][0]['content']                           

        return conteudo_dweet

    else:
        logger.error(f'Falha ao obter o último dweet com status http {r.status_code}')
        return {}


def poll_dweets_forever(delay_secs=2):
    """Loop interminável que verifica os últimos dweets para a 'coisa'"""
    while True:
        dweet = recebe_ultimo_dweet()                                                 
        if dweet is not None:
            processa_dweet(dweet)                                                   
            sleep(delay_secs)                                                      


def imprime_instrucoes():
    """Imprime as instruções no terminal"""
    global NOME_COISA
    print("Acesse o seu browser. Exemplos:")
    print("  On    : " + URL + "/dweet/for/" + NOME_COISA + "?state=on")


def processa_dweet(dweet):
    """Informa o dweet recebido para a 'coisa'"""
    logger.info(f'Mensagem recebida {dweet}')

def manipula_sinal(sig, frame):
    """Libera os recursos."""
    print('Você pressionou Control+C')
    sys.exit(0)

# Função principal
if __name__ == '__main__':
    signal.signal(signal.SIGINT, manipula_sinal)  # Captura CTRL + C
    imprime_instrucoes()                                                           
    ultimo_dweet = recebe_ultimo_dweet()                                               
    if (ultimo_dweet):
        processa_dweet(ultimo_dweet)
    print('Esperando por dweets. Pressione Control+C para sair.')
    poll_dweets_forever()  # Get dweets by polling a URL on a schedule.           