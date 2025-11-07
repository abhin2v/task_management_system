import requests
import json

BASE_URL = "http://localhost:8000"

# 1. CREATE TASK - POST /tasks/   => status should be 201
print("\n1. CREATE TASK (POST /tasks/)")
print("-" * 60)

task_data = {
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "status": "pending"
}
response = requests.post(f"{BASE_URL}/tasks/", json=task_data)
if response.status_code != 201:
    print(f"\tFailed/Already Exist, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    task_id = response.json().get("id")
    print(f"\tCreated task_id: {task_id}")
    print("\tPassed")


# 2. CREATE SECOND TASK
print("\n2. CREATE SECOND TASK (POST /tasks/)")
print("-" * 60)

task_data2 = {
    "title": "Complete project",
    "description": "Finish the API",
    "status": "in_progress"
}
response = requests.post(f"{BASE_URL}/tasks/", json=task_data2)
if response.status_code != 201:
    print(f"\tFailed/Already Exist, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    task_id2 = response.json().get("id")
    print(f"\tCreated task_id: {task_id2}")
    print("\tPassed")


# 3. GET ALL TASKS - GET /tasks/   => status should be 200
print("\n3. GET ALL TASKS (GET /tasks/)")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/")
if response.status_code != 200:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTotal tasks: {response.json().get('total')}")
    print(f"\tItems count: {len(response.json().get('items', []))}")
    print("\tPassed")


# 4. GET TASKS WITH PAGINATION - GET /tasks/?skip=0&limit=1   => status should be 200
print("\n4. GET TASKS WITH PAGINATION (GET /tasks/?skip=0&limit=1)")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/?skip=0&limit=1")
if response.status_code != 200:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTotal tasks: {response.json().get('total')}")
    print(f"\tItems count: {len(response.json().get('items', []))}")
    print(f"\tLimit: {response.json().get('limit')}")
    print("\tPassed")


# 5. GET TASKS BY STATUS - GET /tasks/?status=pending   => status should be 200
print("\n5. GET TASKS BY STATUS (GET /tasks/?status=pending)")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/?status=pending")
if response.status_code != 200:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTotal tasks: {response.json().get('total')}")
    print(f"\tItems count: {len(response.json().get('items', []))}")
    print("\tPassed")


# 6. GET SINGLE TASK - GET /tasks/{task_id}   => status should be 200
print(f"\n6. GET SINGLE TASK (GET /tasks/{task_id})")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/{task_id}")
if response.status_code != 200:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTask ID: {response.json().get('id')}")
    print(f"\tTask Title: {response.json().get('title')}")
    print(f"\tTask Status: {response.json().get('status')}")
    print("\tPassed")


# 7. UPDATE TASK - PUT /tasks/{task_id}   => status should be 200
print(f"\n7. UPDATE TASK (PUT /tasks/{task_id})")
print("-" * 60)

update_data = {
    "status": "completed",
    "description": "Updated description"
}
response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
if response.status_code != 200:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTask ID: {response.json().get('id')}")
    print(f"\tUpdated Status: {response.json().get('status')}")
    print(f"\tUpdated Description: {response.json().get('description')}")
    print("\tPassed")


# 8. GET UPDATED TASK - GET /tasks/{task_id}   => status should be 200
print(f"\n8. GET UPDATED TASK (GET /tasks/{task_id})")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/{task_id}")
if response.status_code != 200:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTask ID: {response.json().get('id')}")
    print(f"\tTask Status: {response.json().get('status')}")
    print(f"\tTask Description: {response.json().get('description')}")
    print("\tPassed")


# 9. DELETE TASK - DELETE /tasks/{task_id}   => status should be 204
print(f"\n9. DELETE TASK (DELETE /tasks/{task_id})")
print("-" * 60)

response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
if response.status_code != 204:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tDeleted successfully")
    print("\tPassed")


# 10. GET DELETED TASK - GET /tasks/{task_id}   => status should be 404
print(f"\n10. GET DELETED TASK - SHOULD 404 (GET /tasks/{task_id})")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/{task_id}")
if response.status_code != 404:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTask not found (404)")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    print("\tPassed")


# 11. CREATE DUPLICATE TASK - POST /tasks/   => status should be 409
print("\n11. CREATE DUPLICATE TASK - SHOULD 409 (POST /tasks/)")
print("-" * 60)

duplicate_data = {
    "title": "Complete project",
    "description": "Duplicate task",
    "status": "pending"
}
response = requests.post(f"{BASE_URL}/tasks/", json=duplicate_data)
if response.status_code != 409:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tDuplicate title rejected (409)")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    print("\tPassed")


# 12. GET NON-EXISTENT TASK - GET /tasks/99999   => status should be 404
print("\n12. GET NON-EXISTENT TASK - SHOULD 404 (GET /tasks/99999)")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/99999")
if response.status_code != 404:
    print(f"\tFailed, got status code as {response.status_code}")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    input("\tpress enter to test further")
else:
    print(f"\tTask not found (404)")
    print(f"\tresponse = {json.dumps(response.json(), indent=2)}")
    print("\tPassed")


print("\n" + "=" * 60)
print("ALL TESTS COMPLETED!")
print("=" * 60)

# 3. GET ALL TASKS - GET /tasks/
print("\n3. GET ALL TASKS (GET /tasks/)")
print("-" * 60)

response = requests.get(f"{BASE_URL}/tasks/")


print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Retrieved all tasks")

# 4. GET ALL TASKS WITH PAGINATION - GET /tasks/?skip=0&limit=1
print("\n4. GET TASKS WITH PAGINATION (GET /tasks/?skip=0&limit=1)")
print("-" * 60)
response = requests.get(f"{BASE_URL}/tasks/?skip=0&limit=1")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Retrieved tasks with pagination")

# 5. GET TASKS BY STATUS FILTER - GET /tasks/?status=pending
print("\n5. GET TASKS BY STATUS (GET /tasks/?status=pending)")
print("-" * 60)
response = requests.get(f"{BASE_URL}/tasks/?status=pending")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Retrieved tasks filtered by status")

# 6. GET SINGLE TASK - GET /tasks/{id}
print(f"\n6. GET SINGLE TASK (GET /tasks/{task_id})")
print("-" * 60)
response = requests.get(f"{BASE_URL}/tasks/{task_id}")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Retrieved single task")

# 7. UPDATE TASK - PUT /tasks/{id}
print(f"\n7. UPDATE TASK (PUT /tasks/{task_id})")
print("-" * 60)
update_data = {
    "status": "completed",
    "description": "Updated description"
}
response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Updated task")

# 8. GET UPDATED TASK
print(f"\n8. GET UPDATED TASK (GET /tasks/{task_id})")
print("-" * 60)
response = requests.get(f"{BASE_URL}/tasks/{task_id}")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Verified update")

# 9. DELETE TASK - DELETE /tasks/{id}
print(f"\n9. DELETE TASK (DELETE /tasks/{task_id})")
print("-" * 60)
response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text if response.text else 'No content (204)'}")
print(f"Deleted task")

# 10. GET DELETED TASK (should return 404)
print(f"\n10. GET DELETED TASK - SHOULD 404 (GET /tasks/{task_id})")
print("-" * 60)
response = requests.get(f"{BASE_URL}/tasks/{task_id}")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Verified task is deleted (404 error)")

# 11. CREATE DUPLICATE TASK (should return 409)
print("\n11. CREATE DUPLICATE TASK - SHOULD 409 (POST /tasks/)")
print("-" * 60)
duplicate_data = {
    "title": "Complete project",  # Same title as task_id2
    "description": "Duplicate task",
    "status": "pending"
}
response = requests.post(f"{BASE_URL}/tasks/", json=duplicate_data)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Verified duplicate title rejection (409 error)")

# 12. GET NON-EXISTENT TASK (should return 404)
print("\n12. GET NON-EXISTENT TASK - SHOULD 404 (GET /tasks/99999)")
print("-" * 60)
response = requests.get(f"{BASE_URL}/tasks/99999")
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
print(f"Verified 404 for non-existent task")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED!")
print("=" * 60)