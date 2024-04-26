import pandas as pd
import yfinance as yf
import datetime as dt
import warnings
warnings.filterwarnings('ignore')

tickers = pd.read_csv('sp500_companies.csv')['Symbol'].to_list()

start = dt.datetime.now() - dt.timedelta(days=365)
end = dt.datetime.now()

sp500_df = yf.download('^GSPC', start, end)
sp500_df['Pct Change'] = sp500_df['Adj Close'].pct_change()
sp500_return = (sp500_df['Pct Change'] + 1).cumprod()[-1]

return_list = []
final_df = pd.DataFrame(columns=['Ticker', 'Latest_Price', "Score", "SMA_150", "SMA_200", "52_Week_Low", "52_Week_High"])

# counter = 0
for ticker in tickers:
    df = yf.download(ticker, start, end)
    df.to_csv(f'stock_data/{ticker}.csv')
    df['Pct Change'] = df['Adj Close'].pct_change()
    stock_return = (df['Pct Change'] + 1).cumprod()[-1]

    returns_compared = round((stock_return / sp500_return), 2)
    return_list.append(returns_compared)
    # counter += 1
    # if counter >= 10:
    #     break

best_performers = pd.DataFrame(list(zip(tickers, return_list)), columns=['Ticker', 'Returns Compared'])
best_performers['Score'] = best_performers['Returns Compared'].rank(pct=True) * 100
best_performers = best_performers[best_performers['Score'] >= best_performers['Score'].quantile(0.7)]

for ticker in best_performers['Ticker']:
    try:
        df = pd.read_csv(f'stock_data/{ticker}.csv', index_col=0)
        moving_averages = [150,200]
        for ma in moving_averages:
            df['SMA_' + str(ma)] = round(df['Adj Close'].rolling(window=ma).mean(), 2)
        latest_price = df['Adj Close'][-1]
        moving_average_150 = df['SMA_150'][-1]
        moving_average_200 = df['SMA_200'][-1]
        low_52week = round(min(df['Low'][-(52*5):]), 2)
        high_52week = round(max(df['High'][-(52*5):]), 2)
        score = round(best_performers[best_performers['Ticker'] == ticker]['Score'].tolist()[0])

        condition_1 = latest_price > moving_average_150 > moving_average_200
        condition_2 = latest_price >= (1.3 * low_52week)
        condition_3 = latest_price >= (0.75 * high_52week)

        if condition_1 and condition_2 and condition_3:
            final_df = pd.concat([final_df, pd.DataFrame({'Ticker': ticker,
                                        "Latest_Price": latest_price,
                                        "Score": score,
                                        "SMA_150": moving_average_150,
                                        'SMA_200': moving_average_200,
                                        '52_Week_Low': low_52week,
                                        '52_Week_High': high_52week}, index=[0])])
    except Exception as e:
        print(f"{e} for {ticker}")


final_df.sort_values(by="Score", ascending=False)
pd.set_option('display.max_columns', 10)
print(final_df)
final_df.to_csv('final.csv')
