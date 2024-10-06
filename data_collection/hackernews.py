import requests
from ai_radio.config import HACKERNEWS_API_URL

def get_top_stories():
    response = requests.get(f"{HACKERNEWS_API_URL}/topstories.json")
    story_ids = response.json()[:10]  # Get top 10 stories
    stories = []
    for story_id in story_ids:
        story_response = requests.get(f"{HACKERNEWS_API_URL}/item/{story_id}.json")
        story = story_response.json()
        stories.append({
            'title': story['title'],
            'url': story.get('url', ''),
            'score': story['score']
        })
    return stories