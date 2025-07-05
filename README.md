# Crowd-funding Console App

Welcome to the Crowd-funding Console App! This is a simple Python project that allows users to register, log in, and create or view crowdfunding projects—all from the command line.

## Features

- **User Registration:** Sign up with your name, email, password, and Egyptian phone number.
- **User Login:** Secure login using your email and password.
- **Project Creation:** After logging in, create new crowdfunding projects with a title, details, target amount, and start/end dates.
- **View Projects:** See a list of all existing projects with their details.

## How It Works

1. **Start the App:**  
   Run `python app.py` in your terminal.

2. **Register or Login:**  
   Choose to register as a new user or log in if you already have an account.

3. **Create or View Projects:**  
   - After logging in, you can create a new project or view all projects.

## Data Storage

- User and project data are stored in simple JSON files:  
  - `users.json` for user information  
  - `projects.json` for project details

## Requirements

- Python 3.x

## Example

```
🎉 Welcome to the CrowdFunding App 🎉
1. Register
2. Login
Enter choice: 1
First Name: Moamen
Last Name: yasser
Email: moamen@example.com
Password: ****
Confirm Password: ****
Egyptian Mobile Number: 01234567890
✅ Registered successfully!
```

## Notes

- Phone numbers are validated for Egyptian formats.
- Dates must be entered in `YYYY-MM-DD` format.
- All actions are performed via the terminal.

---

Enjoy using the Crowd-funding Console