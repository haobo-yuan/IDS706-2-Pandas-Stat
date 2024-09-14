import pytest
import pandas as pd
import os
import main

# Test 1: Ensure data is loaded correctly
def test_data_loading():
    yearly_stats = main.preprocess_data()
    assert not yearly_stats.empty, "Data loading failed: No data found."

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
