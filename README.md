# Desafio-Back-end

Documentação - Projeto de Coleta de Dados e Integração com Banco de Dados

Este documento descreve como rodar o projeto de coleta de dados das APIs públicas Dummyjson e Chuck Norris e integração com banco de dados utilizando a linguagem Python. O projeto utiliza as bibliotecas Requests, Googletrans e SQLAlchemy. 

Pré-requisitos

VS Code instalado no seu sistema.
Python 3 instalado no seu sistema.
As bibliotecas requests, googletrans e sqlalchemy instaladas. Você pode instalar as bibliotecas executando os comandos abaixo no terminal:
pip install requests 
pip install sqlalchemy
pip install googletrans==4.0.0-rc1 

Passo a Passo

1.	Abra o VS Code.
2.	Crie um novo arquivo e copie o código-fonte do projeto para o arquivo.
3.	Salve o arquivo com uma extensão .py. Por exemplo, você pode salvar o arquivo como projeto.py.
4.	Execute o código apertando as teclas de atalho Ctrl + F5
5.	Aguarde o processamento do projeto. Ele realizará as seguintes etapas:
•	Coletará os dados da API pública https://dummyjson.com/products.
•	Calculará a média dos preços dos produtos da categoria "smartphones".
•	Criará um banco de dados SQLite chamado "products.db" e armazenará os produtos coletados.
•	Imprimirá no terminal do VS Code o resultado da coleta de dados, mostrando a média dos preços dos smartphones.
•	Imprimirá uma piada aleatória sobre Chuck Norris em português.
6.	Após a execução do projeto, você verá o resultado no terminal do VS Code.

Observações

•	Certifique-se de que as bibliotecas necessárias estejam instaladas corretamente.
•	Certifique-se de que você esteja conectado à internet, pois o projeto depende do acesso à API pública.
•	O projeto utiliza um banco de dados SQLite, que será criado automaticamente durante a execução do programa.

Conclusão

A documentação acima fornece um guia básico sobre como rodar o projeto de coleta de dados da API e integração com banco de dados em Python. Siga as instruções passo a passo e aproveite os resultados apresentados no terminal.
