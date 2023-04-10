import csv
import requests
import re
from collections import Counter

def get_text_info(filepath):
    with open(filepath, 'r') as f:
        text = f.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        for word, count in word_counts.items():
            print(f"{word} - {count}")

def download_csv(urlpath):
    response = requests.get(urlpath)
    with open('source_data/username.csv', 'wb') as f:
        f.write(response.content)
    with open('source_data/username.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open('source_data/username.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data[:-1])