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
        "ROE%": info.get("returnOnEquity"),
        "ROA%": info.get("returnOnAssets"),
        "DividendYield%": info.get("dividendYield"),
        "MargemLiquida%": info.get("profitMargins"),

        "EV_EBITDA": info.get("enterpriseToEbitda"),
        "MargemOperacional%": info.get("operatingMargins"),
        "LiquidezCorrente": info.get("currentRatio"),
        "Divida_Patrimonio": info.get("debtToEquity"),
        "LPA": info.get("trailingEps")
    }

    listaIndicadores.append(dadosFundamentalistas)

dataFrameIndicadores = pd.DataFrame(listaIndicadores)

if historicos_lista:
    db_historico_precos = pd.concat(historicos_lista).reset_index()
    dataFrameConsolidade = pd.merge(db_historico_precos, dataFrameIndicadores, on="Ticker")
    dataFrameConsolidade.to_csv("db_historico_precos.csv", index=False)

print("\nSucesso! Arquivo 'db_historico_precos.csv' gerado.")
