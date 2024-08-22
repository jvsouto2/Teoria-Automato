# Simulador de Autômatos

Este projeto é um simulador de autômatos finitos que permite criar, converter, minimizar e testar autômatos finitos não determinísticos (AFN) e determinísticos (AFD). Ele é construído em Python usando Flask para o backend e Graphviz para visualização dos autômatos.

## Funcionalidades

- Criar e visualizar AFN.
- Converter AFN para AFD.
- Minimizar AFD.
- Simular palavras em AFD.
- Verificar a equivalência entre AFN e AFD utilizando palavras geradas aleatoriamente.

## Requisitos

- Python 3.7 ou superior
- Flask
- Graphviz

## Instalação

### 1. Clone o repositório

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

#### Windows


python -m venv venv
venv\Scripts\activate


#### macOS e Linux


python3 -m venv venv
source venv/bin/activate


### 3. Instale as dependências


pip install -r requirements.txt


### 4. Instale o Graphviz

O Graphviz é usado para gerar visualizações dos autômatos. Dependendo do seu sistema operacional, siga as instruções abaixo para instalar:

#### Windows

Baixe e instale o Graphviz a partir do [site oficial](https://graphviz.gitlab.io/_pages/Download/Download_windows.html). Certifique-se de adicionar o Graphviz ao PATH durante a instalação.

#### macOS


brew install graphviz


#### Linux


sudo apt-get install graphviz


### 5. Execute o projeto

No terminal, execute:

python main.py


O servidor Flask será iniciado em \`http://127.0.0.1:5001\`.


  - \`visualizar.html\`: Página para visualizar os autômatos gerados e interagir com as funcionalidades adicionais.
  - \`simulacao.html\`: Página que mostra o resultado da simulação de palavras.
  - \`equivalencia.html\`: Página que mostra o resultado da verificação de equivalência.

