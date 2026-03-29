
import re

def clean_text(text):
    text = re.sub(r'@\w+', '', str(text))
    text = re.sub(r'http\S+', '', text)
    text = text.replace('&amp;', '&')
    return text.lower()

def clean_text(text):
    text = re.sub(r'@\w+', '', str(text))
    text = re.sub(r'http\S+', '', text)
    text = text.replace('&amp;', '&')
    return text.lower()

