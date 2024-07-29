import json

with open("vals.json") as f:
    data = json.load(f)

print(data['name'])  # Output: John Doe
print(data['age'])   # Output: 30
print(data['city'])  # Output: New York
