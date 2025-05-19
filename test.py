import requests

user_id = "user123"
response = requests.get(f"http://localhost:5056/api/progress/{user_id}")

print("Status code:", response.status_code)
print("Raw response:", response.text)  # Add this line

goals = response.json()
for goal in goals:
    print(f"{goal['goal_name']}: {goal['progress']}% complete")
