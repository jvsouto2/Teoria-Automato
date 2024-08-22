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

\`\`\`bash
git clone https://github.com/seuusuario/simulador-automatos.git
cd simulador-automatos
\`\`\`

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

#### Windows

\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`

#### macOS e Linux

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Instale as dependências

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Instale o Graphviz

O Graphviz é usado para gerar visualizações dos autômatos. Dependendo do seu sistema operacional, siga as instruções abaixo para instalar:

#### Windows

Baixe e instale o Graphviz a partir do [site oficial](https://graphviz.gitlab.io/_pages/Download/Download_windows.html). Certifique-se de adicionar o Graphviz ao PATH durante a instalação.

#### macOS

\`\`\`bash
brew install graphviz
\`\`\`

#### Linux

\`\`\`bash
sudo apt-get install graphviz
\`\`\`

### 5. Execute o projeto

No terminal, execute:

\`\`\`bash
python main.py
\`\`\`

O servidor Flask será iniciado em \`http://127.0.0.1:5001\`.

### 6. Usando o Simulador

- **Criar AFN**: Preencha os campos no formulário principal e clique em \"Processar\".
- **Visualizar AFN e AFD**: Após criar e converter o AFN, você verá a visualização dos autômatos gerados.
- **Minimizar AFD**: Na página de visualização, clique em \"Minimizar AFD\" para gerar e visualizar o AFD minimizado.
- **Simular Palavras**: Insira uma palavra na página de visualização e clique em \"Simular Palavra\" para verificar se a palavra é aceita pelo AFD.
- **Verificar Equivalência**: Clique em \"Verificar Equivalência entre AFN e AFD\" para verificar se ambos os autômatos aceitam as mesmas palavras.

## Estrutura do Projeto

- \`main.py\`: Arquivo principal que executa o servidor Flask e lida com as rotas.
- \`automato_finito.py\`: Classe base que define a estrutura de um autômato finito.
- \`afn.py\`: Classe que herda de \`AutomatoFinito\` e implementa as funcionalidades de um AFN.
- \`afd.py\`: Classe que herda de \`AutomatoFinito\` e implementa as funcionalidades de um AFD.
- \`templates/\`: Contém os templates HTML usados pelo Flask para renderizar as páginas.
  - \`index.html\`: Formulário inicial para criar o AFN.
  - \`visualizar.html\`: Página para visualizar os autômatos gerados e interagir com as funcionalidades adicionais.
  - \`simulacao.html\`: Página que mostra o resultado da simulação de palavras.
  - \`equivalencia.html\`: Página que mostra o resultado da verificação de equivalência.

