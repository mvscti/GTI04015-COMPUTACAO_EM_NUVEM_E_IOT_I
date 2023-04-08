import socketio

sio = socketio.Client()
nome= sio.sid #Para informar seu nome, basta alterar o valor desta variavel
@sio.on('connect')
def on_connect():
    sio.send(f"\nCliente {nome} connectado...\n")

@sio.on('message')
def receive_custom(msg):
    print(f'Mensagem recebida do servidor: {msg}')


sio.connect('http://localhost:5000')
sio.sleep(5)
print('Desconectando..')
sio.disconnect()
