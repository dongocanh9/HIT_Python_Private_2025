students = [
    {"id": 1, "name": "An", "score": 8.5},
    {"id": 2, "name": "Bình", "score": 7.2},
    {"id": 3, "name": "Chi", "score": 9.0}
]

def find_id(data, id):
    for s in data:
        if s["id"] == id:
            return s
    return None

def filter_score(data, min_score):
    return [s for s in data if s["score"] >= min_score]

def sort_score(data, rev=False):
    return sorted(data, key=lambda x: x["score"], reverse=rev)

def add(data, s_dict):
    if all(k in s_dict for k in ["id","name","score"]):
        data.append(s_dict)

def remove(data, id):
    for i, s in enumerate(data):
        if s["id"] == id:
            data.pop(i)
            return

def stats(data):
    if not data:
        return (0, None, None)
    scores = [s["score"] for s in data]
    mean = sum(scores)/len(scores)
    high = max(data, key=lambda x:x["score"])
    low = min(data, key=lambda x:x["score"])
    return (mean, high, low)

print(find_id(students, 2))
print(filter_score(students, 8.0))
print(sort_score(students))
add(students, {"id":4,"name":"Dũng","score":8.0})
remove(students, 1)
print(stats(students))
