import yfinance as yf
import pandas as pd

def deannualise(annual_rate, periods=365):
    return (1 + annual_rate) ** (1/periods) - 1

def get_risk_free_rate():
    annualised_rate = yf.download("^IRX")["Adj Close"]
    daily_rate = annualised_rate.apply(deannualise)
    return pd.DataFrame({"annualised rate": annualised_rate, "daily rate": daily_rate})

rates = get_risk_free_rate()