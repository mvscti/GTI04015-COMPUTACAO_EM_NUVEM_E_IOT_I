[Retornar a Tabela de Conteúdos](./)
# Introdução a GPIO

Neste diretório se encontram os códigos utilizados nas práticas sobre portas GPIO da Raspberry PI. Todas as práticas são realizadas utilizando Raspberry PI modelo 4B e todos os scritps foram escritos em Python 3. A relação segue abaixo:
*   [requeriments](requeriments.txt) - Dependências Python necessárias para executar os scripts
*   [gpio_led_buzzer](gpio_led_buzzer.py) 
*   [check_requisitos](check_requisitos.py) - Verifica se as bibliotecas necessárias a execução dos scripts se encontram instaladas

## Descrição dos scripts
Para entender todos os scripts, é imortante conhecer o esquema pinout GPIO da Raspberry PI. Cortesia da imagem: [Raspberry PI Foundation](https://www.raspberrypi.org/)
![GPIO pinout Raspberry PI](gpio-pinout-diagram.png)

### gpio_led_buzzer

Script que aciona um LED e um buzzer por cinco segundos, cada um. A imagem a seguir demonstra como o protótipo deve ser feito para executar o código. 
![Esquema LED e Buzzer](esquema_basico.png)

Para exercutar o código:
```
$ python3 gpio_led_buzzer.py 
```


## ✔️ Técnicas e tecnologias utilizadas

- ``Python 3``
- ``Visual Studio Code``