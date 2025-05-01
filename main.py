import feedparser
from datetime import datetime, timedelta, timezone
from scrapper import extract_full_text
from summary import generate_summaries, split_summaries
from postreSql import save_to_db
import time

#RSS feed
feed_url = "https://www.hukukihaber.net/rss"
feed = feedparser.parse(feed_url)

#time interval: last 24 hours
now = datetime.now(timezone.utc)
yesterday = now - timedelta(days=1)

print("The News are checking...")

#news iteration
for entry in feed.entries:
    if hasattr(entry, "published_parsed"):
        published = datetime.fromtimestamp(time.mktime(entry.published_parsed), tz=timezone.utc)
        
        if published > yesterday:
            title = entry.title
            link = entry.link
            if not link.startswith("http"):
                print(f"Unvalid link is skipped: {link}") #some of the link tags were invalid when i tried
                continue

            category = entry.get("category", "No category")

            #scrap the news text
            text = extract_full_text(link)


            #create summary
            summary_text = generate_summaries(text)
            short, medium, long_ = split_summaries(summary_text)

            #article format for storing to db
            article = {
                "title": title,
                "link": link,
                "category": category,
                "published": published
            }

            save_to_db(article, (short, medium, long_))
