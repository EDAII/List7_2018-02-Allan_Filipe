## Lista 7 - Programação Dinâmica
### Problema da Mochila e Maior Subsequência Crescente.

##### Alunos

| Matrícula | Nome | GitHub |
|--|--|--|
| 15/0029624 | Allan Jefrey Pereira Nobre | @AllanNobre |
| 15/0059213 | Filipe Coelho Hilário Barcelos | @FilipeKN4 |

##### Para executar
O ambiente deve ser configurado para a utilização do framework Django na versão 2.1. Após a configuração, deve-se executar o comando abaixo: 

```sh
$ python3 manage.py runserver
```

Após a execução abra o link do servidor em http://127.0.0.1:8000/.

##### Descrição

Escolhe-se qual algoritmo deseja-se e executar entre Dynamic Programming - Knapsack iterativo e Dynamic Programming - Maior Subsequência Crescente.
Lê-se um arquivo ".csv" de registros, nos quais são executados nos dois algoritmos. No Dynamic Programming - Knapsack iterativo é executado o algoritmo que soluciona o knapsack problem(problema da mochila) e retorna a tabela de resolução do valores e uma tabela com os itens selecionados. No Dynamic Programming - Maior Subsequência Crescente obtém-se os valores da maior subsequência de números possível.

##### Visualização

Para a visualização dos resultados foi utilizado o Framework Django da linguagem de programação Python, de modo que foi possível criar uma interface Web estilizada por meio do framework Bootstrap.  

##### Dynamic Programming - Knapsack iterativo

São indicados na tela o maior valor possível, tempo de execução, além de duas tabelas para visualização de valores, sendo que, a primeira mostra os valores e respectivios pesos dos itens, indicando quais foram selecionados, e a segunda mostra a resolução do problema indicando os valores para cada peso.

##### Dynamic Programming - Maior Subsequência Crescente

São indicados na tela o tempo de execução do algorítmo, o valor da maior subsequência e uma tabela com o cálculo da maior subsequência possível dentro da lista fornecida, além dos dados de entrada iniciais adquiridos do ".csv".

##### Observações

Seguem três ".csv's" de exemplo de entrada para a aplicação de Maior Subsequência Crescente, com o objetivo de testar os tempos de execução e um para Knapsack iterativo.