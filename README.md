# Robô de Consulta e Download de Versões do Python

Este projeto automatiza a consulta de versões do Python no site oficial, realiza o download do instalador e instala a versão desejada em sistemas Windows. Ele utiliza o Playwright para navegação e automação de tarefas no navegador, e registra eventos e erros em um banco de dados MongoDB.

## Funcionalidades

1. Realiza uma busca no Google para encontrar o link de download do Python.
2. Navega pela página do Python.org para encontrar a versão desejada.
3. Realiza o download do instalador da versão do Python.
4. Instala a versão do Python no sistema Windows.
5. Registra eventos e erros em um banco de dados MongoDB.

## Tecnologias Utilizadas

* [Python](https://www.python.org/) 3.12.6
* [Playwright](https://playwright.dev/python/) - Automação de navegadores web
* [MongoDB](https://www.mongodb.com/) - Banco de dados para registro de eventos e erros
* [Subprocess](https://docs.python.org/3/library/subprocess.html) - Para execução de processos do sistema

## Pré-requisitos

Certifique-se de ter alguma versão do Python para execução e Playwright instalados na sua máquina.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/VictorHaddad/robot-download-python
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    * No Windows:
        ```sh
        venv\Scripts\activate
        ```

    * No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

5. Instale o Playwright e seus navegadores:
    ```sh
    python -m playwright install
    ```

## Configuração

1. **Configuração do MongoDB**: O projeto utiliza o MongoDB para registrar eventos e erros. Certifique-se de ter o MongoDB configurado e acessível.
2. **Configuração de versão**: No código, a versão desejada do Python é configurada pela constante `MAIN_VERSION`. Altere essa variável conforme necessário para o seu caso de uso.

## Uso/Exemplo

Para iniciar a coleta de dados, realizar o download e instalação da versão do Python, execute o seguinte comando:

```sh
python main.py
