import re
import pandas as pd

def extract_features(df):
    """
    Given a pandas DataFrame with a 'text' column,
    extracts URL and keyword features.
    """
    df_features = df.copy()
    
    # Simple URL extraction
    def count_urls(text):
        if not isinstance(text, str):
            return 0
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        return len(urls)
        
    def count_suspicious_keywords(text):
        if not isinstance(text, str):
            return 0
        keywords = ['urgent', 'verify', 'account', 'restricted', 'won', 'lottery', 'prize', 'bank', 'password']
        text_lower = text.lower()
        return sum(1 for k in keywords if k in text_lower)
        
    df_features['url_count'] = df_features['text'].apply(count_urls)
    df_features['keyword_count'] = df_features['text'].apply(count_suspicious_keywords)
    
    return df_features
