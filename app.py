import json
import os

def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

users = load_data("users.json")
projects = load_data("projects.json")

print("🎉 Welcome to the CrowdFunding App 🎉")
print("1. Register")
print("2. Login")

choice = input("Enter choice: ")

if choice == "1":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter password: ")

    user = {"name": name, "email": email, "password": password}
    users.append(user)
    save_data("users.json", users)
    logged_in_user = user  
    print("✅ Registered successfully!")


elif choice == "2":
    email = input("Enter your email: ")
    password = input("Enter password: ")

    logged_in_user = None
    for user in users:
        if user["email"] == email and user["password"] == password:
            logged_in_user = user
            break

    if not logged_in_user:
        print("❌ Login failed.")
        exit()
    else:
        print(f"✅ Welcome {logged_in_user['name']}!")

print("\nWhat would you like to do?")
print("1. Create Project")
print("2. View All Projects")

choice2 = input("Enter choice: ")

if choice2 == "1":
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    target = input("Enter target amount (EGP): ")

    project = {
        "owner": logged_in_user["email"],
        "title": title,
        "details": details,
        "target": target
    }

    projects.append(project)
    save_data("projects.json", projects)
    print("✅ Project created!")

elif choice2 == "2":
    print("\n--- All Projects ---")
    for p in projects:
        print(f"Title: {p['title']} | Details: {p['details']} | Target: {p['target']} EGP | By: {p['owner']}")
