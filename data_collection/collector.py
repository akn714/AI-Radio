from . import hackernews, twitter, reddit

def collect_data():
    """
    Collect data from various sources
    """
    hn_data = hackernews.get_top_stories()
    twitter_data = twitter.get_trending_tech()
    reddit_data = reddit.get_tech_news()
    
    return {
        "hackernews": hn_data,
        "twitter": twitter_data,
        "reddit": reddit_data
    }