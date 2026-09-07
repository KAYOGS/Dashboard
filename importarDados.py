import yfinance as yf
import pandas as pd

empresas = ["TOTS3.SA", "KLBN11.SA", "POSI3.SA", "MGLU3.SA", "LREN3.SA"]

print("Coletando historico de precos e indicadores dos ultimos 3 anos")

historicos_lista = []
listaIndicadores = []

for e in empresas:
    ticker = yf.Ticker(e)
    info = ticker.info

    historico_preco = ticker.history(period="3y")
    historico_preco.insert(0, "Ticker", e)
    historicos_lista.append(historico_preco)
    dadosFundamentalistas = {
        "Ticker": e,
        "Nome": info.get("longName"),
        "PL": info.get("trailingPE"),
        "PVP": info.get("priceToBook"),
        "ROE%": info.get("returnOnEquity", 0) * 100 if info.get("returnOnEquity") else None,
        "ROA%": info.get("returnOnAssets", 0) * 100 if info.get("returnOnAssets") else None,
        "DividendYield%": info.get("dividendYield", 0) * 100 if info.get("dividendYield") else 0,
        "MargemLiquida%": info.get("profitMargins", 0) * 100 if info.get("profitMargins") else None,

        "EV_EBITDA": info.get("enterpriseToEbitda"),
        "MargemOperacional%": info.get("operatingMargins", 0) * 100 if info.get("operatingMargins") else None,
        "LiquidezCorrente": info.get("currentRatio"),
        "Divida_Patrimonio": info.get("debtToEquity"),
        "LPA": info.get("trailingEps")
    }

    listaIndicadores.append(dadosFundamentalistas)

dataFrameIndicadores = pd.DataFrame(listaIndicadores)
dataFrameIndicadores.to_csv("indicadores.csv", index=False)

if historicos_lista:
    db_historico_precos = pd.concat(historicos_lista).reset_index()
    db_historico_precos.to_csv("db_historico_precos.csv", index=False)

print("\nSucesso! Arquivos 'indicadores.csv' e 'db_historico_precos.csv' gerados.")
