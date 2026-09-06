# Unisales Dashboard

Script Python para obter dados de empresas do Ibovespa usando o Yahoo Finance (`yfinance`).

## O que o script faz

O [indice-generator.py](indice-generator.py):

1. Sorteia 10 tickers aleatórios de uma lista de empresas listadas no Ibovespa.
2. Busca um resumo de cada empresa (nome, setor, preço atual e market cap).
3. Baixa o histórico de preços (1 mês) de cada empresa.
4. Salva o histórico de cada empresa em um arquivo CSV (`<TICKER>_historico.csv`).

## Requisitos

- Python 3.10+
- Dependências: `yfinance`, `pandas`

## Instalação

Crie e ative um ambiente virtual, depois instale as dependências:

```bash
python3 -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/macOS

pip install yfinance pandas
```

## Uso

```bash
python3 indice-generator.py
```

A saída no terminal mostra os tickers sorteados e uma tabela resumo. Os históricos de preços são salvos como arquivos CSV no diretório atual.

## Observações

- Alguns tickers podem não estar disponíveis no Yahoo Finance (ex.: empresas que mudaram de código ou foram deslistadas). Nesses casos, o script exibe um aviso e continua com as demais empresas.
- Os dados dependem da disponibilidade da API pública do Yahoo Finance.
