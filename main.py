import argparse
import sys
from src.train import train_model
from src.predict import predict_email

def main():
    parser = argparse.ArgumentParser(description="Phishing Email Detector")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Train command
    train_parser = subparsers.add_parser("train", help="Train the phishing detection model")
    
    # Predict command
    predict_parser = subparsers.add_parser("predict", help="Predict if an email is phishing or safe")
    predict_parser.add_argument("text", type=str, help="The email text to classify")
    
    args = parser.parse_args()
    
    if args.command == "train":
        train_model()
    elif args.command == "predict":
        try:
            result = predict_email(args.text)
            print(f"\nEmail Text: {args.text}")
            print(f"Prediction: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
