from transformers import pipeline
# The pipeline that we'll be using to perform sentiment analysis
classifier = pipeline("sentiment-analysis")
result = classifier(["My Name is Usman"])
# Let's assume we have a string of data coming from a web crawler and we want
# to perform sentiment analysis on it.
data = ["The restaurant was nice and i loved it",
        "The app has a decent menu but can be improved",
        "The developers of the app do not care for the user's privacy",
        "The developers of the app should improve their privacy settings but overall the app is nice to use",
        "The app was great to use but can be improved",
        "I don't like the app at all and would not recommend it to anyone"]

# The nice thing about huggingface is that it provides us with sentimental analysis in the same order we pass the data in
# There is a label which represents the sentiment which is either negative or positive
# There is also a score which represents the confidence
result_sentimental_analysis = classifier(data)
for analysis in result_sentimental_analysis:
    print(analysis)
