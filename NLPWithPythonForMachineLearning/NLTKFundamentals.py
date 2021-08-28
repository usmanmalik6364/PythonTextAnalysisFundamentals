# Read in SemiStructured Data.
import pandas as pd
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Read in the raw text
rawData = open("SMSSpamCollection.tsv").read()

# print(rawData[0:500])

parsedData = rawData.replace('\t', '\n').split('\n')
# starts in the 0th position, take every second element and go untill the end.
labelList = parsedData[0::2]
textList = parsedData[1::2]

fullCorpus = pd.DataFrame({
    # Grab everything except last one because its empty.
    'label': labelList[:-1],
    'body_list': textList
})
# print(fullCorpus)

# Raw datasets does not have any headers so we need to specify that header = None
# sep ='\t' specifies that the data is delimited by \t
dataset = pd.read_csv('SMSSpamCollection.tsv', sep='\t', header=None)
dataset.columns = ['label', 'body_text']

# Analyzing the Shape of our data
print(
    f"Input data has {len(dataset)} rows and {len(dataset.columns)} columns.")

# How many spam/ham are there. Categorizing the dataset.
print(
    f"Out of {len(dataset)} rows, {len(dataset[dataset['label']=='spam'])} are spam, {len(dataset[dataset['label']=='ham'])} are ham")

# How much missing data is there?
# Sum all the nulls in the label
print(f"Number of null in label: {dataset['label'].isnull().sum()}")
print(f"Number of null in text: {dataset['body_text'].isnull().sum()}")
