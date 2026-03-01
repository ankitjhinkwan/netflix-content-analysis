"""
Generate a realistic Twitter sentiment dataset.
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)
N = 3000

TOPICS = ["Technology", "Politics", "Sports", "Entertainment",
          "Climate", "Economy", "Health", "Gaming",
          "Music", "Movies", "Fashion", "Food"]

HASHTAGS = {
    "Technology": ["#AI", "#Tech", "#Python", "#MachineLearning", "#ChatGPT"],
    "Politics":   ["#Election", "#Democracy", "#Government", "#Policy", "#Vote"],
    "Sports":     ["#Cricket", "#FIFA", "#NBA", "#Olympics", "#Football"],
    "Entertainment": ["#Netflix", "#Bollywood", "#Hollywood", "#OTT", "#Series"],
    "Climate":    ["#ClimateChange", "#SaveEarth", "#Green", "#Sustainability", "#COP28"],
    "Economy":    ["#Economy", "#Inflation", "#Stock", "#Bitcoin", "#Finance"],
    "Health":     ["#Health", "#Fitness", "#Wellness", "#MentalHealth", "#Covid"],
    "Gaming":     ["#Gaming", "#PS5", "#Xbox", "#Minecraft", "#Esports"],
    "Music":      ["#Music", "#NewSong", "#Spotify", "#Playlist", "#Concert"],
    "Movies":     ["#Movies", "#BoxOffice", "#Oscars", "#Review", "#Cinema"],
    "Fashion":    ["#Fashion", "#Style", "#OOTD", "#Trends", "#Designer"],
    "Food":       ["#Food", "#Recipe", "#Foodie", "#Restaurant", "#Cooking"],
}

SENTIMENTS = ["Positive", "Negative", "Neutral"]
LANGUAGES  = ["English", "Hindi", "Spanish", "French", "Portuguese"]
DEVICES    = ["Mobile", "Web", "Desktop", "API"]
SOURCES    = ["iPhone", "Android", "Twitter Web", "TweetDeck", "Buffer"]

START = datetime(2023, 1, 1)

records = []
for i in range(N):
    topic     = np.random.choice(TOPICS)
    sentiment = np.random.choice(SENTIMENTS, p=[0.42, 0.33, 0.25])
    date      = START + timedelta(days=np.random.randint(0, 365))
    hashtag   = np.random.choice(HASHTAGS[topic])
    language  = np.random.choice(LANGUAGES, p=[0.55, 0.15, 0.12, 0.10, 0.08])
    device    = np.random.choice(DEVICES,   p=[0.55, 0.25, 0.15, 0.05])
    source    = np.random.choice(SOURCES,   p=[0.30, 0.25, 0.25, 0.12, 0.08])

    # Engagement based on sentiment
    base_likes    = 50 if sentiment == "Positive" else 30 if sentiment == "Negative" else 15
    likes         = max(0, int(np.random.exponential(base_likes)))
    retweets      = max(0, int(likes * np.random.uniform(0.1, 0.4)))
    replies       = max(0, int(likes * np.random.uniform(0.05, 0.25)))
    impressions   = max(likes + retweets, int(np.random.exponential(500)))

    # Sentiment score -1 to 1
    if sentiment == "Positive":
        score = round(np.random.uniform(0.1, 1.0), 3)
    elif sentiment == "Negative":
        score = round(np.random.uniform(-1.0, -0.1), 3)
    else:
        score = round(np.random.uniform(-0.1, 0.1), 3)

    records.append({
        "TweetID":        f"TW{100000+i}",
        "Date":           date.strftime("%Y-%m-%d"),
        "Month":          date.strftime("%b %Y"),
        "DayOfWeek":      date.strftime("%A"),
        "Hour":           np.random.randint(0, 24),
        "Topic":          topic,
        "Hashtag":        hashtag,
        "Sentiment":      sentiment,
        "SentimentScore": score,
        "Language":       language,
        "Device":         device,
        "Source":         source,
        "Likes":          likes,
        "Retweets":       retweets,
        "Replies":        replies,
        "Impressions":    impressions,
        "Verified":       np.random.choice([0, 1], p=[0.85, 0.15]),
        "FollowerCount":  max(10, int(np.random.exponential(1000))),
    })

df = pd.DataFrame(records)
df.to_csv("twitter_data.csv", index=False)
print(f"✅ Dataset saved: {len(df)} tweets")
print(f"   Positive: {(df['Sentiment']=='Positive').sum()} ({(df['Sentiment']=='Positive').mean():.1%})")
print(f"   Negative: {(df['Sentiment']=='Negative').sum()} ({(df['Sentiment']=='Negative').mean():.1%})")
print(f"   Neutral:  {(df['Sentiment']=='Neutral').sum()} ({(df['Sentiment']=='Neutral').mean():.1%})")
