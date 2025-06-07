import requests
import time
import json
from bs4 import BeautifulSoup
from datetime import datetime

# ------------------ CONFIG ------------------
BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_PATH = "/c/courses/tds-kb/34"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "_forum_session=ZlcKwhRzxKh%2F6NoyKfscME1mZYaC8h30IcYqQFQ0x%2FWzVS8Ahy%2FL0QDPx1UCfs3oteQI1RI4MZmRqM6cnJoeFXxia%2B%2FT5posDWSajAAojgFgnFHjTLZWwryhEyijlViRUgKC%2FQW8ULTNUUNJ3zZOHPPoW%2FEs%2FzResq7vaDIkXIKQomgli6RtjncxA4L2uTcnClVVNDHNgu3tSg5rCHmOFK%2BONoHU9Ou3szwvHpp7CfxlTgFW7NqlLGOKbCFmbN7Jm2sjpYe1EowbMQzQCt2kJysG%2FjuZvw%3D%3D--%2BrG2sdF1JqdAXPPs--fgeykwZPDX%2BpLsUMsxeWxQ%3D%3D"
}

DATE_START = datetime(2025, 1, 1)
DATE_END = datetime(2025, 4, 14)

# ------------------ SCRAPER ------------------

def get_topic_ids():
    url = BASE_URL + CATEGORY_PATH + ".json"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    topic_list = data.get("topic_list", {}).get("topics", [])
    topic_ids = [t["id"] for t in topic_list]

    print(f"✅ Found {len(topic_ids)} topic IDs")
    return topic_ids


def get_posts(topic_id):
    url = f"{BASE_URL}/t/{topic_id}.json"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    data = r.json()

    posts = data.get("post_stream", {}).get("posts", [])
    filtered = []

    for post in posts:
        created_at = datetime.strptime(post["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if DATE_START <= created_at <= DATE_END:
            filtered.append({
                "topic_id": topic_id,
                "topic_title": data.get("title"),
                "created_at": post["created_at"],
                "username": post["username"],
                "content": post["cooked"],
                "url": f"{BASE_URL}/t/{topic_id}"
            })

    return filtered

def scrape_all():
    topic_ids = get_topic_ids()
    all_posts = []

    for tid in topic_ids:
        try:
            posts = get_posts(tid)
            all_posts.extend(posts)
            print(f"📄 Got {len(posts)} posts from topic {tid}")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ Error in topic {tid}: {e}")

    with open("tds_discourse_posts.json", "w", encoding="utf-8") as f:
        json.dump(all_posts, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved {len(all_posts)} posts to tds_discourse_posts.json")

# ------------------ RUN ------------------

if __name__ == "__main__":
    scrape_all()