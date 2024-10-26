from utils import load_data
from model import PhishingDetector

def main():
    # Load data
    urls, labels = load_data(
        'data/legitimate_urls.csv',
        'data/phishing_urls.csv'
    )

    # Initialize and train model
    detector = PhishingDetector()
    report = detector.train(urls, labels)

    # Print results
    print("Model Performance:")
    print(report)

    # Example prediction
    test_url = "https://meet.google.com/hrj-jchj-ixm?pli=1&authuser=2"
    result = detector.predict(test_url)
    print(f"\\nPrediction for {test_url}:")
    print(f"Is Phishing: {result['is_phishing']}")
    print(f"Probability: {result['probability']:.2f}")

if __name__ == "__main__":
    main()
