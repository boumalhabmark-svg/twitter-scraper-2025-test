import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

# Query for MTVLebanon mentions, hashtags, and tweets
query = "MTVLebanon OR #MTVLebanon OR @MTVLebanon since:2025-10-01"

tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= 500:
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url])

df = pd.DataFrame(tweets, columns=["Date","User","Text","URL"])
df.to_csv("tweets.csv", index=False)
print(f"✅ Saved {len(df)} tweets to tweets.csv")
