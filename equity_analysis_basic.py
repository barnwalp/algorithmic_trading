# %%
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option("display.max_columns", None)  # show all columns
pd.set_option("display.width", None)

# import yfinance as yf

plt.style.use("seaborn-v0_8")


# %%
df = yf.download(
    tickers="HDFCBANK.NS",
    auto_adjust=False,
    actions=True,
    interval="1d",
    multi_level_index=False,
)
# df = yf.download(tickers = "HDFCBANK.NS", start="2020-07-01", end="2025-07-01", interval="1d", multi_level_index=False)
# df = yf.download(tickers = "HDFCBANK.NS", period="1mo") # last one month
# df = yf.download(tickers = "HDFCBANK.NS", period="1y") # last one year
# df = yf.download(tickers = "HDFCBANK.NS", period="1y", interval="1h")
# df = yf.download(tickers = "HDFCBANK.NS", period="1y", interval="1m")
# df = yf.download(tickers = "HDFCBANK.NS", period="5d", interval="1m")
# df = yf.download(tickers = "HDFCBANK.NS", period="max")
df.index = pd.to_datetime(df.index.date)
df

# %%
df2 = pd.read_csv("apple.csv")
print(df2)
with open("df_output.txt", "w") as f:
    f.write(df2.to_string())


# %%
df2.loc[:, "Volume"].plot(figsize=(12, 8))
plt.ylabel("Volume (Shares)")
plt.title("Apple Trading Volume (daily)", fontsize=15)
plt.show()


# %%
df.loc[:, "Close"].plot(figsize=(12, 8))
plt.ylabel("Price in Rupee")
plt.xlabel("Year")
plt.title("HDFC Bank Share Price")
plt.show()


# %%
# Plotting volume of shares traded
df.loc["2025", "Volume"].plot(figsize=(12, 8), kind="bar")
plt.ylabel("Volume (Shares)")
plt.title("HDFC Bank Trading Volume (daily)", fontsize=15)
plt.show()


# %%
df.Dividends.sum()


# %%
df.loc[df.Dividends != 0].Dividends.plot()
plt.ylabel("Dividends issued per share")
plt.show()
