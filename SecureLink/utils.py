
from urllib.parse import urlparse
import pandas as pd

data = pd.read_csv("data/data_bal - 20000.xlsx")

def preprocess_url(url):
    """Clean and standardize URL"""
    url = url.lower().strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url

def load_data(legitimate_path, phishing_path):
    """Load and combine datasets"""
    legitimate_urls = pd.read_csv(legitimate_path)
    phishing_urls = pd.read_csv(phishing_path)

    # Combine datasets
    urls = pd.concat([legitimate_urls, phishing_urls])
    labels = [0] * len(legitimate_urls) + [1] * len(phishing_urls)

    return urls, labels
