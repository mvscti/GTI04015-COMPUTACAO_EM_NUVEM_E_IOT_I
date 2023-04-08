from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)
 
@socketio.on('connect')
def on_connect():
    print('Servidor recebeu uma conexão')
    
@socketio.on('message')
def on_message(msg):
    #Mensagem recebida do cliente
    print(msg)
    socketio.emit('message', 'Olá')
 

if __name__=="__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
