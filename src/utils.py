"""
Docstring for src.utils
"""

import pandas as pd
def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)