```markdown
# Flask Login Authentication System

A secure and simple login system with GUI interface, built with Python Flask backend and Tkinter frontend. Provides basic user registration and authentication functionality with password hashing.

## Key Features

🔐 **Secure Authentication**
- Password hashing using Werkzeug security utilities
- HTTP API endpoints for authentication operations
- Error handling for common authentication scenarios

📋 **User Management**
- New user registration system
- Duplicate username prevention
- In-memory user storage (for demonstration purposes)

🖥️ **Desktop GUI**
- Clean interface for login/registration
- Responsive design with error feedback
- Separate dashboard window on successful login

## System Requirements

- Python 3.7+
- pip package manager
- Internet browser (for API calls)
- 500MB available disk space

## Installation Guide

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Application
```bash
python main.py
```

The system will automatically:
- Launch Flask backend server on port 5000
- Start the desktop GUI interface
- Handle server-client communication

## User Guide

### First-Time Setup
1. Register a new user account using the registration window
2. Remember your credentials for future logins

### Login Process
1. Enter registered username and password
2. Successful login redirects to dashboard
3. Failed attempts show specific error messages

![GUI Workflow](https://via.placeholder.com/600x400.png?text=Login+→+Register+→+Dashboard)

### Registration Workflow
1. Click "Register" from login window
2. Choose unique username and password
3. Immediate feedback on registration status

### Dashboard Features
- Welcome message display
- Basic user session management
- Simple interface for future feature expansion

## Security Notes

🔒 **Password Protection**
- All passwords stored as secure hashes
- No plaintext password storage
- Uses Werkzeug's generate_password_hash (PBKDF2-HMAC-SHA256)

⚠️ **Important Considerations**
- Demo uses in-memory storage - users reset on app restart
- Not recommended for production use without:
  - Persistent database storage
  - SSL/TLS encryption
  - Session management
  - Brute-force protection

## Troubleshooting

**Common Issues**              | **Solutions**
-------------------------------|--------------
"Port 5000 unavailable"        | Close other apps using port 5000 or restart computer
"Connection failed" errors     | Verify Flask server is running in background
Username already exists        | Choose different username or restart app to clear memory
Invalid credentials            | Check caps lock and re-enter carefully

## License

This project is provided as open-source software for educational purposes. Free to modify and redistribute under MIT License. Not recommended for production environments.

---

> **Note:** This is a demonstration system. Always consult security professionals before implementing authentication systems in production environments.
```