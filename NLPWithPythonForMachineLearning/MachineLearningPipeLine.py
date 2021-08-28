### STEPS------###
# Raw text - model can't distinguish words
# Tokenize - tell the model what to look at .
# Clean text- remove stop words/punctuation, stemming etc.
# Stemming-  tells python that learn, learnt, learning are basically of same semantic meaning. It greatly helps in optimizing our data.
# Vectorize- Convert textual data to numeric form, numeric matrix.
# Machine learning algorithm - fit/train model.
# Example Spam FIlter- to filer spam emails from emails.
########################################################

# Pre-Processing Text Data
# Tokenization
from os import write
import string
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')
pd.set_option('display.max_colwidth', 100)
nltk.download('wordnet')
data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header=None)
data.columns = ['label', 'body_text']
data.head()
# string.punctuation contains punctuations


def remove_punct(text):
    # Insert only characters that are not a punctuation such as ',;.#$ etc'
    # Join the characters with ''(nothing) because the list returned is of characters
    text_nopunct = "".join(
        [char for char in text if char not in string.punctuation])
    return text_nopunct


# lambda function that will apply the function to each character.
data['body_text_clean'] = data['body_text'].apply(lambda x: remove_punct(x))


def tokenize(text):
    # W+ means it will split wherever it'll see one or more non word characters.
    tokens = re.split('\W+', text)
    return tokens


data['body_text_tokenized'] = data['body_text_clean'].apply(
    lambda x: tokenize(x.lower()))

# For better read i'll write this data to a csv file.
# data.to_csv('test_data.csv')

# Remove stop words from the text to limit the number of tokens,
#  and optimize the model's performance.

stopword = nltk.corpus.stopwords.words('english')


def remove_stopwords(tokenized_list):
    text = [word for word in tokenized_list if word not in stopword]
    return text


data['body_text_nostop'] = data['body_text_tokenized'].apply(
    lambda x: remove_stopwords(x))


# Stemming => Process of reducing inflected
#  (or sometimes derived words to their word stem or root).
ps = nltk.PorterStemmer()
# print(dir(ps))
print(ps.stem('grows'))
print(ps.stem('growing'))
print(ps.stem('grow'))
# All the above three words will be reduced to grow which means
#  that basically they mean the same thing.
# The process of stemming allows us to reduce memory usage and
#  optimizing resources for our models.

# clean_text combines the process of cleaning the text in one function.


def clean_text(text):
    text = "".join([word.lower()
                    for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [ps.stem(word) for word in tokens if word not in stopword]
    return text


data['body_text_nostop'] = data['body_text'].apply(
    lambda x: clean_text(x.lower()))


# Stem Text
def stemming(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text]
    return text


data['body_text_stemmed'] = data['body_text_nostop'].apply(
    lambda x: stemming(x))

# data.to_csv('test_data.csv')


# Lemmatizing
# Process of grouping together the inflected forms of a word
#  so they can be analyzed as a single term, identified by the word's lemma.

# Stemming is fatser but can reduce accuracy.
# Lemmatizing is computationally expensive and always return the word from a dictionary.

wn = nltk.WordNetLemmatizer()
ps = nltk.PorterStemmer()
print(ps.stem('meanness'))  # both return mean
print(ps.stem('meaning'))  # both return mean

print(wn.lemmatize('meanness'))  # meanness
print(wn.lemmatize('meaning'))  # meaning


def lemmatizing(tokenized_text):
    text = "".join(
        [wn.lemmatize(word) for word in tokenized_text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopword]
    return text


data['body_text_Lemmatized'] = data['body_text_nostop'].apply(
    lambda x: lemmatizing(x))

# Vectorizing
# Process of encoding text as integers to create feature vectors.

# Feature Vector
# An n-dimenstional vector of numerical features that represent some object.

# Count Vectorization
count_vect = CountVectorizer(analyzer=clean_text)
X_counts = count_vect.fit_transform(data['body_text'])
# print(X_counts.shape)  # 5567 rows and 8104 unique text messages.
# print(count_vect.get_feature_names())
data_sample = data[0:20]
count_vect_sample = CountVectorizer(analyzer=clean_text)
X_counts_sample = count_vect_sample.fit_transform(data_sample['body_text'])
# print(X_counts_sample.shape)
# print(count_vect_sample.get_feature_names())

# Vectorizers output sparse matrices.
# Sparse Matrix

X_counts_df = pd.DataFrame(X_counts_sample.toarray())
# print(X_counts_df)


# N-Grams
# Creates a document-term matrix where counts still occupy the cell but instead the columns representing single terms,
# they represent all combinations of adjacent words of length n in your text.
def clean_text_ngrams(text):
    text = "".join([word.lower()
                    for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    # Because n-gram requires a string so we are just concatenating the tokenized string back with spaces in between them
    text = " ".join([ps.stem(word) for word in tokens if word not in stopword])
    return text


data['cleaned_text'] = data['body_text'].apply(lambda x: clean_text(x))
# print(data.head())
CountVectorizer(ngram_range=(2, 2))  # we're only interested in bigrams
X_counts = ngram_vect.fit_transform(data['cleaned_text'])
# print(X_counts.shape)
# print(ngram_vect.get_feature_names())
data_sample = data[0:20]
ngram_vect_sample = CountVectorizer(ngram_range=(2, 2))

X_counts_sample = ngram_vect_sample.fit_transform(data_sample['cleaned_text'])
print(X_counts_sample.shape)
print(ngram_vect.get_feature_names())
X_counts_df = pd.DataFrame(X_counts_sample.toarray())
X_counts_df.columns = ngram_vect_sample.get_feature_names()
# print(X_counts_df)
