
# Core libraries
from . import features
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# ML Models
from sklearn.ensemble import RandomForestClassifier
# from sklearn.xgboost import XGBClassifier  # Optional alternative

class PhishingDetector:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.scaler = StandardScaler()
        self.feature_extractor = features.FeatureExtractor()

    def prepare_features(self, urls):
        """Extract features from URLs"""
        features_list = []
        for url in urls:
            features = self.feature_extractor.extract_features(url)
            features_list.append(features)

        return pd.DataFrame(features_list)

    def train(self, urls, labels):
        """Train the model"""
        # Extract features
        X = self.prepare_features(urls)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, labels, test_size=0.2, random_state=42
        )

        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Train model
        self.model.fit(X_train_scaled, y_train)

        # Evaluate
        y_pred = self.model.predict(X_test_scaled)
        report = classification_report(y_test, y_pred)

        return report

    def predict(self, url):
        """Predict for a single URL"""
        features = self.feature_extractor.extract_features(url)
        features_df = pd.DataFrame([features])

        # Scale features
        features_scaled = self.scaler.transform(features_df)

        # Predict
        probability = self.model.predict_proba(features_scaled)[0][1]
        is_phishing = probability > 0.5

        return {
            'is_phishing': is_phishing,
            'probability': probability,
            'features': features
        }





