# 🏎️ Counter Flow

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PyGame](https://img.shields.io/badge/PyGame-%3E%3D_2.6.1-green?style=flat-square)](https://www.pygame.org/)

Projeto acadêmico desenvolvido para a disciplina de **Linguagem de Programação**. O *Counter Flow* é um jogo 2D vertical de desvio de tráfego em alta velocidade (corrida infinita) com sistema de pontuação progressiva.

---

## 🛠️ Instalação e Execução

Abra o terminal na pasta raiz do projeto dentro do VSCode e escolha uma das abordagens abaixo para instalar as dependências listadas no arquivo `requirements.txt`:

### 🔹 Opção 1: Instalação Isolada (Localmente - Recomendado)
Esta opção cria um ambiente virtual (`venv`) para isolar o PyGame dentro da pasta do projeto, evitando conflitos com outras instalações do Python no seu computador.

1. **Criar o ambiente virtual:**
    Execute o código abaixo no seu terminal para instalar o ambiente virtual local:
        python -m venv venv
---
2. **Ativar o ambiente virtual:**
    No Windows (PowerShell):
    Execute o código abaixo no seu terminal:
        .\venv\Scripts\Activate.ps1

    Ou no Mac/Linux (Terminal):
    Execute o código abaixo no seu terminal:
        source venv/bin/activate

(Você saberá que deu certo quando o prefixo (venv) aparecer na linha do terminal)

3. **Instalar as dependências via requirements.txt:**
    Execute o código abaixo no seu terminal:
        pip install -r requirements.txt

---

🔹 Opção 2: Instalação Global
Esta opção instala o PyGame diretamente no escopo global do seu usuário do sistema operacional, tornando a biblioteca acessível de qualquer local do computador, sem necessidade de ativação de ambiente.

Instalar as dependências via requirements.txt diretamente:
    Execute o código abaixo no seu terminal:
        pip install -r requirements.txt

🚀 Inicialização
Independentemente do método de instalação escolhido, execute o arquivo principal para iniciar o jogo:
    python main.py


👤 Autor
Victor (Villex) — GitHub