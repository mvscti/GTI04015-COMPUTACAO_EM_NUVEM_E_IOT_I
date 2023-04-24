[Retornar a Tabela de Conteúdos](./)
# REST
Presente desde o início dos anos 90, o protocolo HTTP é atualmente o principal protocolo utilizado para comunicação entre sistemas Web.

Nos anos 2000, Roy Fielding, um dos principais autores deste protocolo, sugeriu o uso de novos métodos. Estes métodos pretendiam resolver problemas relacionados a semântica durante as requisições. As sugestões permitiram o uso do HTTP de uma forma muito aproximada da utilização atual, dando sentido às requisições. Para melhor percepção, segue os exemplos da proposta de Fielding:
1. ```GET``` http://www.meudominio.com/alunos
2. ```DELETE``` http://www.meudominio.com/alunos/patrick
3. ```POST``` http://www.meudominio.com/alunos –data {nome: Marcus}

No exemplo 1, utilizamos o método (ou verbo) ```GET``` para obter todos os <strong>recursos</strong> daquela página (no exemplo, a página ```http://www.meudominio.com/alunos```). Entenda recurso como algo que uma determinada página pode oferecer (conteúdo HTML, documento PDF, arquivos de formatação, etc). Já no segundo exemplo, o verbo ```DELETE``` é utilizado para para remover um recurso da mesma página. No exemplo, é solicitado a remoção de um aluno de nome <i>patrick</i>. Já o método ```POST```, do terceiro exemplo, demonstra a criação de um novo aluno na base de dados do servidor ```www.meudominio.com```.

Os princípios apresentados fazem parte da API (<i>Application Programing Interface</i> - Interface de Programação de Aplicação) REST (<i>Representational State Transfer</i> - Transferência de estado representacional). A REST (ou RESTFul) é uma arquitetura de software que impõe condições sobre como uma API deve funcionar. Ou seja, a API concede a <strong>interoperabilidade</strong> entre usuários e aplicações.

![api_rest_aplicação](https://raw.githubusercontent.com/mvscti/GTI04015-COMPUTACAO_EM_NUVEM_E_IOT_I/main/REST/1623804399333.png)

Em suma, os principais verbos HTTP utilizados nas API REST são (se quiser conhecer sobre todos os métodos, leia mais [aqui](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods)):

| Método/Verbo HTTP| Descrição |
| -------- | ------- |
| GET | Obtém um recurso |
| POST | Adiciona um novo recurso |
|PUT | Atualiza um recurso |
|DELETE | Remove um recurso |
|PATCH | Parcialmente atualiza um recurso em uma coleção |

## Representações
Sabemos que uma API perimite com que sistemas sejam  interoperáveis. É importante que o intercâmbio de mensagens seja padronizado e se possível, facilmente compreendido por máquinas e humanos. Vamos analisar três exemplos muito utilizados nas API's:

* Mensagem em XML:
```xml
<endereco>
   <cep>156112-651</cep>
   <cidade>Belo Horizonte</cidade>
   <numero>126</numero>
   <rua>Avenida Amazonas</rua>
</endereco>
```
* Mensagens em JSON:
```json
{
  "endereco" : {
    "rua" : "Avenida Amazonas",
    "numero" : "126",
    "cidade" : "Belo Horizonte",
    "cep": "156112-651" 
  }
}
```
* Mensagens em YAML:
```yaml
endereco:
  rua: 'Avenida Amazonas'
  numero: '126'
  cidade: 'Belo Horizinte'
  cep: '156112-651'
```

## HTTP e IoT
Em diversas situações, HTTP não é o protocolo ideal para aplicações IoT. A latência não pode ser previsível. É um protocolo baseado em texto, o que pode tornar o tamanho das mensagens muito grande (isso pode exigir grande consumo de energia por parte dos dispositivos). No entanto, o protocolo já é maduro o suficiente para ter vasto uso. O protocolo também atua sob TCP (entrega confiável).

Algumas vantagens no emprego do HTTP para IoT:
* Confiável: Entrega da mensagem é garantida
* Onipresença: HTTP é usado em diversos cenários e é facilmente implementado
* Fácil de ser implementado: Se você se conceta à Internet, pode-se usar o HTTP em qualquer lugar do mundo (não há necessidade de software ou hardware adcional).

Algumas desvantagens no emprego do HTTP para IoT:
* Consumo alto de carga: o processo de "ir e voltar" na comunicação é comum para manter as conexões, o que faz o consumo energético ser maior. O tamanho das mensagens também é um dificultador.
* Complexidade dos dispositivos IoT: dispositivos IoT são muito heterogêneos, o que significa que nem todos podem possuir memória e CPU suficientes para suportar o HTTP e uma API REST





