# 📖 Diário Secreto em Python

Este é um projeto simples de **manipulação de arquivos** desenvolvido em Python. O objetivo principal é praticar a leitura e escrita de dados de forma persistente em arquivos de texto (`.txt`).

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 📋 Sobre o Projeto
Diferente de programas que perdem os dados ao serem fechados, este Diário salva cada entrada do usuário em um arquivo local. Isso permite que você mantenha um histórico de pensamentos ou notas que podem ser lidos posteriormente.

## 🚀 Funcionalidades
* **Escrita Persistente:** Utiliza o modo `append` (`a`) para adicionar novas linhas sem apagar o conteúdo anterior.
* **Leitura de Histórico:** Lê e exibe no terminal todo o conteúdo armazenado no arquivo `diario.txt`.
* **Tratamento de Exceções:** * Captura erros de entrada (letras em vez de números).
    * Gerencia o erro de "Arquivo não encontrado" (`FileNotFoundError`) caso o usuário tente ler o diário antes de criar sua primeira nota.
* **Codificação UTF-8:** Garante que emojis e acentuação da língua portuguesa sejam salvos corretamente.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Manipulação de Arquivos (Built-in I/O)**

## 🔧 Como Rodar
1. Clone o repositório ou baixe o arquivo `.py`.
2. Execute o programa:
   ```bash
   python diario.py
