import yfinance as yf
import pandas as pd

empresas = ["TOTS3.SA", "KLBN11.SA", "POSI3.SA", "MGLU3.SA", "LREN3.SA"]
preco = yf.download(empresas, period="3y")

if preco is not None and preco is not preco.empty:
    preco = preco.reset_index()
