import pytest
import pandas as pd
from io import StringIO
import os
import main

# Test 1: Ensure data is loaded correctly
def test_data_loading():
    stock = pd.read_csv('NASDAQ_100_Data_From_2010.csv',sep='\t')
    stock_AAPL = stock.loc[stock['Name'] == 'AAPL']
    assert not stock_AAPL.empty, "Data loading failed: No AAPL data found."

# Test 2: Check if README is generated
def test_readme_generation():
    if os.path.exists("README.md"):
        with open("README.md", 'r') as f:
            content = f.read()
            assert "Statistics" in content, "README may miss statistics"
    else:
        pytest.fail("README.md not found")

# Test 3: Check if plot image is generated
def test_plot_generation():
    assert os.path.exists("plot.png"), "plot.png not generated"
