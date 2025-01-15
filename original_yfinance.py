import yfinance as yf
import pandas as pd


# Lista de tickers
tickers = ["LEN", "AAPL", "GOOG", "MSFT", "TSLA", "KBH", "NVDA", "AMD" ,"SAN", "MELI", "META", "YPF", "NFLX", "DIS"] #Super Micro Computer

# Crear un archivo Excel con múltiples hojas
with pd.ExcelWriter("yahoo_finance_multiple_tickers.xlsx") as writer:
    for ticker in tickers:
        # Descargar los datos históricos
        data = yf.download(ticker, start="2024-01-01", end="2025-12-31")
        
        # Guardar cada ticker en una hoja separada
        data.to_excel(writer, sheet_name=ticker)
        
        print(f"Datos de {ticker} exportados.")

print("Exportación completa a 'yahoo_finance_multiple_tickers.xlsx'")