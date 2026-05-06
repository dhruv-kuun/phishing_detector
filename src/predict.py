import joblib
import os

def predict_email(email_text, model_path="models/phishing_model.pkl"):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}. Please train the model first.")
        
    model = joblib.load(model_path)
    prediction = model.predict([email_text])[0]
    
    return "Phishing" if prediction == 1 else "Safe"

if __name__ == "__main__":
    sample_text = "Urgent: Please verify your account to avoid suspension. Click http://verify-now.com"
    
    if os.path.exists("models/phishing_model.pkl"):
        result = predict_email(sample_text)
        print(f"Sample Email: '{sample_text}'")
        print(f"Prediction: {result}")
    else:
        print("Model not found. Run 'python src/train.py' to generate it first.")
