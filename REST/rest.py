from flask import Flask, jsonify
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/<int:numero>/')
def incrementer(numero):
    return "Número incrementado é " + str(numero+1)

@app.route('/<string:nome>/')
def hello(nome):
    return "Olá " + nome

@app.route('/matricula/<int:matricula>/', methods=['POST'])
def matricula(matricula):
    return jsonify({'matricula': matricula}), 201 #retorna resposta em formato JSON



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')