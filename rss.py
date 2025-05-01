import feedparser
from datetime import datetime, timezone, timedelta
import time

feed_url = "https://www.hukukihaber.net/rss"


feed = feedparser.parse(feed_url)



#sytem time
now = datetime.now(timezone.utc)
#before 24 hour ago
yesterday = now - timedelta(days=1)




for entry in feed.entries:
    if hasattr(entry, 'published_parsed'):
        published = datetime.fromtimestamp(time.mktime(entry.published_parsed), tz=timezone.utc)         # RSS time to datetime
        if published > yesterday:
            title = entry.title
            link = entry.link
            category = entry.get('category', 'There is no category')
            print(category)
            print(title)
            print(link)
            print(published)


