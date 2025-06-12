import requests
import json
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

with open("eval_dataset.json", "r") as f:
    dataset = json.load(f)

results = []

for sample in dataset:
    question = sample["question"]
    expected = sample["expected_answer"]

    response = requests.post(
        "http://127.0.0.1:8000/api/",
        json={"question": question}
    ).json()

    actual = response.get("answer", "")
    score = similarity(expected, actual)

    results.append({
        "question": question,
        "expected": expected,
        "actual": actual,
        "similarity": round(score, 2)
    })

with open("evaluation_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Evaluation complete. Saved to evaluation_results.json")