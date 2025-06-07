import json

# Read the one-line JSON file
with open("tds_discourse_posts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Write pretty-printed JSON with indentation
with open("tds_discourse_posts_pretty.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Reformatted JSON saved as tds_discourse_posts_pretty.json")
