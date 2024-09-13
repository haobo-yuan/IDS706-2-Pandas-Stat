# Dataset from https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data/data

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

# Read the data
stock = pd.read_csv('NASDAQ_100_Data_From_2010.csv',sep='\t')

# Only use AAPL stock data
stock_AAPL = stock.loc[stock['Name'] == 'AAPL']
# print(stock_AAPL.shape)

# Replace the index with the Date
stock_AAPL.Date = pd.to_datetime(stock_AAPL.Date)
stock_AAPL.set_index('Date', inplace=True)
# print(stock_AAPL)

# Add a new column 'Year'
stock_AAPL['Year'] = stock_AAPL.index.year

# sorted by 'Year', use 'Close' to calculate mean, median, std
yearly_stats = stock_AAPL.groupby('Year')['Close'].agg(['mean', 'median', 'std'])
print(yearly_stats)

# Plotting the statistics
plt.figure(figsize=(15, 6))
plt.plot(yearly_stats.index, yearly_stats['mean'], label='Mean', marker='o')
plt.plot(yearly_stats.index, yearly_stats['median'], label='Median', marker='x')
plt.plot(yearly_stats.index, yearly_stats['std'], label='Standard Deviation', marker='s')
plt.grid(True)

plt.title('AAPL Close Price Statistics (2010-2021)')
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend()
plt.savefig('plot.png')
