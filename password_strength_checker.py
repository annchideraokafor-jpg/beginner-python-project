import re

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: password must be at least 8 characters long."
    
    # Check for uppercase, lowercase, digits, and special characters
    if not re.search(r"[A-Z]", password):
        return "Weak: add at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Weak: add at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Weak: add at least one number."
    if not re.search(r"[@$!%*?&]", password):
        return "Weak: add at least one special character (@, $, !, %, *, ?, &)."
    
    return "Strong password!"

# Get input from user
user_password = input("Enter your password: ")
print(check_password_strength(user_password))
