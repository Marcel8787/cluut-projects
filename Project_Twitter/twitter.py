import json
import seaborn as sns
from textblob import TextBlob

sns.set_theme()

with open("data.json", "r") as file:
    data = json.load(file)

obama_tweets = list(filter(lambda x: x["topic"] == "obama", data))
print(obama_tweets)

for entry in obama_tweets:
    tweet = entry["tweet"]
    text = TextBlob(tweet)
    polar = text.sentiment.polarity
    
    if polar < -0.2:
      entry["sentiment"] = "negative"
    elif polar > 0.2:
      entry["sentiment"] = "positive"
    else:
      entry["sentiment"] = "neutral"
     
with open("data_obama.json", "w") as file:
    json.dump(obama_tweets, file)
    
sents = [tweet["sentiment"] for tweet in obama_tweets]
sns_plot = sns.histplot(x = sents)
sns_plot.figure.savefig("sentiment_tweet.png")


