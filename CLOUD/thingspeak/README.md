[Retornar a Tabela de Conteúdos](./)
# Conectando as "coisas" à Nuvem utilizando o ThingSpeak
Dentre as formas de conectar dispositivos de Internet das Coisas à Nuvem, temos como opção a plataforma [ThingSpeak](https://www.mathworks.com/products/thingspeak.html). Com ela, até um certo limite, podemos conectar nossos sensores IoT e acompanhar, através de *dashboards* customizáveis, sendo possível também a aplicação de inteligência analítica (*analytics*). A plataforma trabalha com o protocolo MQTT, que você já aprendeu.


# Práticas com a Plataforma ThingSpeak
Neste diretório, se encontra um código de exemplo que demonstra como utilizar a (já conhecida) biblioteca ```paho mqtt```, para conectar nossos dispositivos à Plataforma ThingSpeak. Todos os scritps foram escritos em Python 3. A relação segue abaixo:
* [Conectando um "sensor" à Plataforma ThingSpeak](thingspeak.py)

## Preparando o ambiente
**IMPORTANTE:** Antes de rodar os scripts, é necessário resolver as dependências dos projetos. O primeiro passo é criar um [ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html) **para cada projeto que iremos executar**. Fazendo isso, podemos usar diferentes versões de uma biblioteca para um projeto em especifico, sem existir a necessidade de instalar elas em nosso Sistema Operacional (as bibliotecas são instaladas no diretório do seu projeto e só ficam disponíveis para ele). Para criar um ambiente virtual em Python:

```
$ python3 -m venv /diretório/para/ambiente_virtual
```

Após criar o ambiente virtual, precisamos ativá-lo:


```
$ source /diretório/para/ambiente_virtual/bin/activate
```

E finalmente podemos instalar nossas dependências (o comando a seguir deve ser executado dentro do diretório de seu projeto):

```
$ pip3 install -r requeriments.txt 
```

Para desativar (sair) do ambiente virtual de um projeto (para ativar outros, talvez), basta digitar:
```
$ deactivate
```

## Descrição dos scripts

### [Conectando um "sensor" à Plataforma ThingSpeak](thingspeak.py)
*Script* que faz a leitura da carga de uso da CPU em um dado instante (em %) e envia à plataforma ThingSpeak, a cada 20 segundos (este tempo pode ser alterado na linha ```39```). É necessário completar os dados no arquivo ```confing.ini.exemplo``` (todos os dados pode ser obtidos no momento em que você se conectar à Plataforma) e depois, **renomear o arquivo** para ```config.ini```. Depois de criar um "channel" e um "device" na sua interface de acesso na plataforma e informar os dados no arquivo mencionado anteriormemte, ao executar o *script* , você perceberá um gráfico referentes aos dados recebidos. Para executar:

```
$ python3 thingspeak.py 
```
