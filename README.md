# Trabalho de Análise Sintática da Linguagem Algorítmica (LA)

Alexandra Floriano - 761771

## Pré-requisitos

Python 3.x

ANTLR

## Descrição

Este é um projeto que implementa um analisador sintático para a linguagem LA (Linguagem Algorítmica), utilizando a ferramenta ANTLR (ANother Tool for Language Recognition).

O analisador sintático desenvolvido é capaz de identificar erros sintáticos no código fonte em LA, fornecendo mensagens de erro detalhadas para facilitar a correção por parte do usuário.

## Estrutura do Projeto

* 'output_dir': Pasta onde contém os analisadores léxico e sintático em Python.
* 'LAParser.g4': Arquivo contendo a gramática do analisador sintático em formato ANTLR.
* 'LALexer.g4': Arquivo contendo as regras do analisador léxico em formato ANTLR.
* 'main.py': Script Python para executar o analisador sintático.
* 'entrada.txt': Arquivo de exemplo contendo um código fonte em LA para ser analisado.
* 'saida.txt': Arquivo de saída onde serão registradas as mensagens de erro sintático.
* 'tes.py': Arquivos para imprimir todos as saídas dos casos-testes.
* 'casos_testes_t2': Pasta com os arquivos de entrada casos-testes.
* 'saida': Pasta contendo a saida dos casos-testes.

## Como Executar

1. Instale o ANTLR seguindo as instruções em [antlr](https://www.antlr.org/).
2. Execute no seu terminal para poder utilizar em Python.

```Python3
pip install antlr4-python3-runtime
```

4. Execute o comando para gerar os analisadores léxico e sintático em Python.

```Python3
antlr4 -Dlanguage=Python3 -o output_dir LAParser.g4 LALexer.g4
```

3. Execute o analisador sintático com o comando, onde entrada.txt é o arquivo contendo o código fonte em LA a ser analisado e saida.txt é o arquivo de saída onde serão registradas as mensagens de erro.

```Python3
Python3 main.py entrada.txt saida.txt
```

## Casos de teste

O trabalho possui 62 casos de teste, para automatizar o processo de testar as saidas,o arquivo tes.py faz os arquivos saida.txt para todos casos de teste, como utilizar:

```Python3
Python3 tes.py
```
