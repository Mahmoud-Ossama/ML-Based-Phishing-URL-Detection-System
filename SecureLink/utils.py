from urllib.parse import urlparse
import pandas as pd

def preprocess_url(url):
    """Clean and standardize URL"""
    url = url.lower().strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url

def load_data(legitimate_path, phishing_path):
    """Load and combine datasets"""
    # Since we have an Excel file, use read_excel
    data = pd.read_excel("data/data_bal - 20000.xlsx")
    
    # Using correct column names from the Excel file
    urls = data['URLs'].tolist()  # Changed from 'URL' to 'URLs'
    labels = data['Labels'].tolist()

    return urls, labels
