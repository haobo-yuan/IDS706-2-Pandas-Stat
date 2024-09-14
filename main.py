# Dataset from https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data/data

import pandas as pd
import matplotlib.pyplot as plt

# Data Preprocessing
def preprocess_data():
    stock = pd.read_csv('NASDAQ_100_Data_From_2010.csv',sep='\t')
    stock_AAPL = stock.loc[stock['Name'] == 'AAPL']  # Only use AAPL stock data

    # Extract "Year" info from "Date" Column
    stock_AAPL.Date = pd.to_datetime(stock_AAPL.Date)
    stock_AAPL.set_index('Date', inplace=True)  
    stock_AAPL['Year'] = stock_AAPL.index.year  # Add a new column 'Year'

    # Sort by 'Year', use 'Close' to calculate its stock's mean, median, std data
    yearly_stats = stock_AAPL.groupby('Year')['Close'].agg(['mean', 'median', 'std'])
    return yearly_stats

# Plotting the statistics
def generate_plot(yearly_stats):
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

# Generate README.md
def generate_readme(yearly_stats):
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('# AAPL Price Statistics (2010-2021)\n')
        f.write('This is a IDS-706 homework project that calculates the mean, median,' \
                'and standard deviation of AAPL stock close prices from 2010 to 2021.\n\n')
        
        f.write('![Logo Nasdaq](Logo_Nasdaq.png)')
        f.write('![Logo AAPL](Logo_AAPL.png)\n\n')

        f.write('The data is from the everyday close price of <NASDAQ 100 Data From 2010> dataset on Kaggle.\n')
        f.write('>https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data/data \n\n')

        f.write('The statistics are as follows:\n')
        f.write(yearly_stats.to_markdown())

        f.write('## Description and Conclusion:\n')
        f.write('\n\n')
        f.write('![Plot](plot.png)')
        f.write('\n\n')
        f.write('''Apple Inc.'s stock performance from 2010 to 2021 shows significant growth, with the average
                price rising from $9.28 to $134.34. The company saw consistent increases in stock value, 
                particularly in 2020 and 2021, likely driven by strong demand for electronics during the pandemic
                and its market leadership in innovation. While volatility increased in the later years, especially
                in 2020 with the standard deviation peaking at 21.81, Apple's overall performance was robust,
                reflecting its resilience and growth in the global tech industry.\n''')


if __name__ == '__main__':
    data = preprocess_data()
    generate_plot(data)
    generate_readme(data)