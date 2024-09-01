import re

def validate_password(password):
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
        
    if not re.search("[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
        
    if not re.search("[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
        
    if not re.search("[0-9]", password):
        errors.append("Password must contain at least one number.")
        
    if errors:
        return "\n".join(errors)
    else:
        return "valid"

while True:
    password = input("Enter your password: ")
    result = validate_password(password)
    
    if result == "valid":
        print("Password is valid.")
        break
    else:
        print(result)
        print("Please try again.\n")
        