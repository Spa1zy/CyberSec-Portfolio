import re

def check_password_strength(password):
    # Weak if length<6
    if len(password)<6:
        return "Weak (too short)"

    # Medium if only letters or only numbers
    if password.isdigit() or password.isalpha():
        return "Medium (use mix of letters, numbers, symbols)"

    # Strong if it has mix of upper, lower, numbers, symbols
    if (re.search("[a-z]",password) and 
        re.search("[A-Z]",password) and
        re.search("[0-9]",password) and
        re.search("[!@#$%^&*()_+]", password)):
        return "Strong"

    return "Good (add more variety for stronger security)"

if __name__=="__main__":
    print("🔐 Password Strength Checker")
    pwd=input("Enter a password to test: ")
    result=check_password_strength(pwd)
    print("Result: ", result)
