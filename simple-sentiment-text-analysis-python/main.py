from textblob import TextBlob
# from newspaper import Article

# url = 'https://www.bbc.com/news/world-europe-68853490'

# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)

# blob = TextBlob(text)
# sentiment = blob.sentiment.polarity # -1 to 1

# print(sentiment)

with open('mytext.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)