from logging import info

import yfinance as yf
import pandas as pd

empresas = ["TOTS3.SA", "KLBN11.SA", "POSI3.SA", "MGLU3.SA", "LREN3.SA"]
preco = yf.download(empresas, period="3y")

if preco is not None and not preco.empty:
    preco = preco.reset_index()

listaIndicadores = []

for e in empresas:
    ticker = yf.Ticker(e)
    info = ticker.info

    dadosFundamentalistas = {
        "Ticker": e,
        "Nome": info.get("longName"),
        "PL": info.get("trailingPE"),
        "PVP": info.get("priceToBook"),
        "ROE%": info.get("returnOnEquity", 0) * 100 if info.get("returnOnEquity") else None,
        "ROA%": info.get("returnOnAssets", 0) * 100 if info.get("returnOnAssets") else None,
        "DividendYield%": info.get("dividendYield", 0) * 100 if info.get("dividendYield") else 0,
        "MargemLiquida%": info.get("profitMargins", 0) * 100 if info.get("profitMargins") else None
    }
    listaIndicadores.append(dadosFundamentalistas)

dataFrame = pd.DataFrame(listaIndicadores)
dataFrame.to_csv("indicadores.csv", index=False)

if preco is not None and not preco.empty:
    preco.to_csv("db_historico_precos.csv", index=False)
