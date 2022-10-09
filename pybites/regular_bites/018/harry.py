import os
import string
from typing import Counter
import urllib.request

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():
    with open(harry_text) as f:
        harry = f.read().lower()
    with open(stopwords_file) as f:
        stopwords = f.read().lower().split()

    words = [
        word.strip(string.punctuation)
        for word in harry.split()
        if word not in stopwords and word.strip(string.punctuation)
    ]

    count = Counter(words)
    return count.most_common(1)[0]
