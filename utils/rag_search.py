import json
import os
from typing import List, Dict

# Load data from files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

with open(os.path.join(DATA_DIR, "tds_course_content.txt"), "r", encoding="utf-8") as f:
    course_text = f.read()

with open(os.path.join(DATA_DIR, "tds_discourse_posts_pretty.json"), "r", encoding="utf-8") as f:
    discourse_data = json.load(f)

posts = discourse_data.get("posts", [])

# --- Search Functions ---

def search_course(question: str) -> List[str]:
    lines = course_text.split('\n')
    question_keywords = [word.lower() for word in question.split() if len(word) > 3]
    
    matches = []
    for line in lines:
        if any(word in line.lower() for word in question_keywords):
            matches.append(line)
        if len(matches) >= 3:
            break

    return matches

def search_discourse(question: str) -> List[Dict[str, str]]:
    question_keywords = [word.lower() for word in question.split() if len(word) > 3]
    
    links = []
    for post in posts:
        text = post.get("cooked") or post.get("raw") or ""
        if any(word in text.lower() for word in question_keywords):
            link = {
                "url": f"https://discourse.onlinedegree.iitm.ac.in/t/{post.get('topic_slug', 'discussion')}/{post.get('topic_id', 0)}/{post.get('post_number', 1)}",
                "text": text[:180] + "..." if len(text) > 180 else text
            }
            links.append(link)
        if len(links) >= 2:
            break

    return links

# --- Main Interface ---

def answer_question(question: str, image: str = None) -> Dict[str, object]:
    course_hits = search_course(question)
    discourse_hits = search_discourse(question)

    answer_parts = []
    if course_hits:
        answer_parts.append("From course content:\n" + "\n".join(course_hits))
    if discourse_hits:
        answer_parts.append("From Discourse posts:\n" + "\n".join([link["text"] for link in discourse_hits]))

    answer = "\n\n".join(answer_parts) if answer_parts else "Sorry, I couldn't find an answer to your question."

    return {
        "answer": answer,
        "links": discourse_hits
    }