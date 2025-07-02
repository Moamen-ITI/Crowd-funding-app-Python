import json
import os
from datetime import datetime
import re

def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def validate_egyptian_phone(phone):
    return re.match(r"^01[0-2,5]{1}[0-9]{8}$", phone)

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

users = load_data("users.json")
projects = load_data("projects.json")

print("🎉 Welcome to the CrowdFunding App 🎉")
print("1. Register")
print("2. Login")

choice = input("Enter choice: ")
logged_in_user = None

if choice == "1":
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    confirm = input("Confirm Password: ")

    if password != confirm:
        print("❌ Passwords do not match.")
        exit()

    phone = input("Egyptian Mobile Number: ")
    if not validate_egyptian_phone(phone):
        print("❌ Invalid Egyptian phone number.")
        exit()

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users.append(user)
    save_data("users.json", users)
    logged_in_user = user
    print("✅ Registered successfully!")

elif choice == "2":
    email = input("Email: ")
    password = input("Password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            logged_in_user = user
            break

    if not logged_in_user:
        print("❌ Login failed.")
        exit()
    else:
        print(f"✅ Welcome {logged_in_user['first_name']}!")

print("\nWhat would you like to do?")
print("1. Create Project")
print("2. View All Projects")

choice2 = input("Enter choice: ")

if choice2 == "1":
    title = input("Project title: ")
    details = input("Project details: ")
    target = input("Target amount (EGP): ")

    try:
        target = float(target)
    except:
        print("❌ Invalid amount.")
        exit()

    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")

    if not (validate_date(start_date) and validate_date(end_date)):
        print("❌ Invalid date format.")
        exit()

    project = {
        "owner": logged_in_user["email"],
        "title": title,
        "details": details,
        "target": target,
        "start": start_date,
        "end": end_date
    }

    projects.append(project)
    save_data("projects.json", projects)
    print("✅ Project created!")

elif choice2 == "2":
    print("\n📋 All Projects:")
    for p in projects:
        print(f"🔸 Title: {p['title']}")
        print(f"   Details: {p['details']}")
        print(f"   Target: {p['target']} EGP")
        print(f"   Duration: {p['start']} to {p['end']}")
        print(f"   Owner: {p['owner']}")
        print("-" * 40)
