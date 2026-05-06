# Phishing Email Detector

A machine learning project built with Python and Scikit-learn to classify emails as either "Phishing" or "Safe" based on their textual content and extracted features (like URLs and suspicious keywords).

## Project Structure

```
phishing_detector/
├── data/
│   └── email_dataset.csv       # Raw phishing/safe dataset used for training
├── models/
│   ├── phishing_model.pkl      # Saved Scikit-learn model after training
│   └── confusion_matrix.png    # Visualization of the model's performance
├── notebooks/
│   └── exploration.ipynb       # Jupyter Notebook for Exploratory Data Analysis (EDA)
├── src/
│   ├── __init__.py
│   ├── feature_extraction.py   # Logic to parse URLs and keywords from text
│   ├── train.py                # Script to train the model and output metrics
│   └── predict.py              # Script to classify a single new email
├── .gitignore                  # Git ignore file to prevent pushing venv/
├── requirements.txt            # Python dependencies (scikit-learn, pandas, joblib)
└── main.py                     # Command Line Interface (CLI) to run the detector
```

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dhruv-kuun/phishing_detector.git
   cd phishing_detector
   ```

2. **Create and activate a virtual environment:**
   - **Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

This project includes a convenient CLI script (`main.py`) to easily interact with the model.

### 1. Train the Model
To train the model on the dataset and generate the classification report, accuracy score, and confusion matrix:
```bash
python main.py train
```
*Note: This will save the trained model to `models/phishing_model.pkl`.*

### 2. Predict a Single Email
To test the model on a new piece of text or email, run the `predict` command followed by the text string:
```bash
python main.py predict "Urgent: Update your account details immediately at http://secure-update-bank.com"
```
```bash
# Example Output
Email Text: Urgent: Update your account details immediately at http://secure-update-bank.com
Prediction: Phishing
```

## Features Analyzed
While the main classification pipeline uses **TF-IDF Vectorization** on the raw text content to capture natural language context, additional manual feature extractors are provided in `src/feature_extraction.py`:
- `count_urls(text)`: Identifies and counts HTTP/HTTPS links inside the text.
- `count_suspicious_keywords(text)`: Flags common phishing keywords (e.g., "urgent", "verify", "account", "restricted", "lottery").
