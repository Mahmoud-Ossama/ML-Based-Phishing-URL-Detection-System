import utils
from model import PhishingDetector

def main():
    # Load data
    urls, labels = utils.load_data(None, None)

    # Initialize and train model
    detector = PhishingDetector()
    
    # Train model (store report but don't print)
    report = detector.train(urls, labels)
    
    # New interactive interface
    while True:
        url = input("\nEnter URL (or 'quit' to exit): ")
        if url.lower() == 'quit':
            break
            
        print("-------------------")
        result = detector.predict(url)
        print(f"Is it phishing: {result['is_phishing']}")
        print(f"Probability: {result['probability']:.2f}")

if __name__ == "__main__":
    main()
