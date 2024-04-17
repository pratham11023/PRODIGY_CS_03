#Pratham Koturwar
#Provide feedback to users on the password's strength.
import re


def check_password_strength(password):
    length_ok = len(password) >= 8
    uppercase_ok = any(char.isupper() for char in password)
    lowercase_ok = any(char.islower() for char in password)
    digit_ok = any(char.isdigit() for char in password)
    special_char_ok = re.search(r"[!@#$%^&*()-+=]", password) is not None

    if length_ok and uppercase_ok and lowercase_ok and digit_ok and special_char_ok:
        return "Strong"
    elif length_ok and (uppercase_ok or lowercase_ok) and digit_ok:
        return "Moderate"
    else:
        return "Weak"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
