# SecureLink: Machine Learning-Based Phishing URL Detection System

## Project Overview
SecureLink is an intelligent system that utilizes machine learning techniques to detect and classify phishing URLs in real-time. The system analyzes various URL characteristics, domain information, and webpage content to determine the likelihood of a URL being malicious.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)

## Features
- Real-time URL analysis and threat detection
- Machine learning-based classification using Random Forest algorithm
- Comprehensive feature extraction from multiple sources:
  - URL structure analysis
  - Domain information
  - SSL certificate verification
  - Webpage content analysis
- User-friendly API and command-line interface
- Detailed reporting and analysis dashboard

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone the repository
```bash
git clone https://github.com/Mahmoud-Ossama/ML-Based-Phishing-URL-Detection-System.git
cd securelink
```

2. Create and activate virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure
```
phishing_detection/
├── data/
│   ├── legitimate_urls.csv
│   └── phishing_urls.csv
├── utils.py          # Helper functions
├── features.py       # Feature extraction
├── model.py          # Model training and prediction
└── main.py          # Main execution script
```

## Usage

### Basic Usage
```python
from securelink import PhishingDetector

# Initialize detector
detector = PhishingDetector()

# Check a single URL
result = detector.check_url("https://example.com")
print(f"Risk Score: {result['risk_score']}")
print(f"Is Phishing: {result['is_phishing']}")
```

### Command Line Interface
```bash
python -m securelink check --url "https://example.com"
python -m securelink batch --file urls.txt
```

### Web API
```bash
# Start the API server
python -m securelink.api

# Example API request
curl -X POST http://localhost:5000/api/check \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```

## Model Training

### Using Provided Dataset
```bash
python -m securelink.train --data data/processed/training_data.csv
```

### Using Custom Dataset
```bash
python -m securelink.train --data your_dataset.csv --model-output models/custom_model.pkl
```

## Testing
Run the test suite:
```bash
pytest tests/
```

## Performance Metrics
- Accuracy: 92.5%
- Precision: 94.3%
- Recall: 91.8%
- F1 Score: 93.0%

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors
- Mahmoud Osama - *Initial work* - (https://github.com/Mahmoud-Ossama)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Dataset provided by PhishTank
- Inspired by research on ML-based phishing detection
- Thanks to Delta University/Faculty of AI - Cybersecurity Department for project support

## Contact
Mahmoud Osama - vip.m.osama@gmail.com
Project Link: https://github.com/Mahmoud-Ossama/ML-Based-Phishing-URL-Detection-System

## Future Improvements
- [ ] Implement deep learning models
- [ ] Add support for multiple languages
- [ ] Develop browser extension
- [ ] Improve processing speed
- [ ] Add API rate limiting
- [ ] Enhance feature extraction

## Citation
If you use this project in your research, please cite:
```
@misc{securelink2024,
  author = {Mahmoud Osama},
  title = {SecureLink: Machine Learning-Based Phishing URL Detection System},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/Mahmoud-Ossama/ML-Based-Phishing-URL-Detection-System}
}
```
