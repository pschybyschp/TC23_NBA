# Import libraries
import pandas as pd
from collections import Counter 
import string
import re
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

stop_words = stopwords.words('english')
# Limit to 7000 rows of data

df = (pd.DataFrame(_arg1))

#df = df[:7000]
def clean_tweets(tweets):
   
  # Remove http from tweets
  tweets = re.sub('http', '', tweets)
  tweets = re.sub('https', '', tweets)
   
  # tokenize and lowercase
  tweets = word_tokenize(tweets)
  tweets = [w.lower() for w in tweets]
   
  # remove punctuation from tweets
  table = str.maketrans('', '', string.punctuation)
  remove_punct = [t.translate(table) for t in tweets]
  words = [word for word in remove_punct if word.isalpha()]
   
  # remove stopwords from tweets
  stop_words = set(stopwords.words('english'))
  return [w for w in words if not w in stop_words]
# Apply clean_tweets to Tweets column
df['Clean_Tweets'] = df['text'].apply(clean_tweets)

# create word count function
def counter(tweets):
  cnt = Counter()
  for words in tweets:
    for word in words:
      cnt[word] += 1
  return cnt
word_cnt = counter(df['Clean_Tweets'])
most_common_words = word_cnt.most_common()

# create word count dataframe
twitter_word_counts = pd.DataFrame(most_common_words, columns = ['Words', 'Counts'])
# sort word count dataframe
twitter_word_counts = twitter_word_counts.sort_values(by='Counts', ascending=False)
twitter_word_counts = twitter_word_counts[:250]

# compute sentiment scores (polarity) and labels
sentiment_scores = [round(TextBlob(tweet).sentiment.polarity, 3) for tweet in twitter_word_counts['Words']]
sentiment_category = ['positive' if score > 0 else 'negative' if score < 0 else 'neutral' for score in sentiment_scores]
twitter_word_counts['Sentiment'] = sentiment_category

return twitter_word_counts.to_dict(orient='list')