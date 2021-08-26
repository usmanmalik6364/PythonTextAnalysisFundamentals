from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
# Instantiate Model.
tokenizer = AutoTokenizer.from_pretrained(
    'nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained(
    'nlptown/bert-base-multilingual-uncased-sentiment')


# Encode And Calculate Sentiment
tokens = tokenizer.encode(
    'The day has been terrible', return_tensors='pt')  # Converts into list of numbers.

result = model(tokens)
result.logits
# Sentiment rating for this text is 1. Which means the least rating one can get.
print(f" Sentiment Rating for text is: {int(torch.argmax(result.logits)+1)}")

token2 = tokenizer.encode(
    'I had the best day of my life ever', return_tensors='pt')
result_2 = model(token2)
# Sntiment rating for this text is 5. As the rating is between 1-5, 5 means best rating.
print(f" Sentiment Rating for text is: {int(torch.argmax(result_2.logits)+1)}")

# Grabbing reviews from yelp and performing sentimantal analysis on that text.
# Web Scrapping
r = requests.get('https://www.yelp.com/biz/social-brew-cafe-pyrmont')
soup = BeautifulSoup(r.text, 'html.parser')
regex = re.compile('.*comment.*')
results = soup.find_all('p', {'class': regex})
reviews = [result.text for result in results]

# Load Reviews into DataFrame And Score
df = pd.DataFrame(np.array(reviews), columns=['review'])
df['review'].iloc[0]


def sentiment_score(review):
    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1


sentiment_score(df['review'].iloc[1])
# apply lambda function to go through all the reviews and apply sentiment analysis to that.
# specifying a token limit of 512
df['sentiment'] = df['review'].apply(lambda x: sentiment_score(x[:512]))
print(df)
