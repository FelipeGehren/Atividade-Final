# Buscador de Notícias com NewsAPI

Este é um programa em Python que permite buscar notícias em tempo real usando a [NewsAPI](https://newsapi.org/), baseado em temas como **tecnologia**, **política**, **investimentos** e **criminalidade**.

## Funcionalidades

- Buscar notícias por tema
- Escolher a quantidade de notícias (máximo de 5 por vez)
- Visualizar histórico de buscas realizadas
- Interface simples via terminal

---

## Tecnologias utilizadas

- Python 3
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [NewsAPI](https://newsapi.org/)

---

## Configuração da API Key

Para utilizar o programa, é necessário obter uma chave de API (API Key) gratuita em: [https://newsapi.org/register](https://newsapi.org/register)

Depois, crie um arquivo `.env` no mesmo diretório do script com o seguinte conteúdo:

API_KEY_NEWS=SuaApiKeyAqui
