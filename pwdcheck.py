import re

def check(password):
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digits = bool(re.search(r'\d', password))
    special_chars = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = 0

    if length >= 8:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if digits:
        score += 1
    if special_chars:
        score += 1

    if score == 5:
        return "Strong password"
    elif score >= 3:
        return "Moderate password"
    elif score >= 1:
        return "Weak password"
    else:
        return "Very weak password"

def main():
    while True:
        password = input("Enter your password: ")
        strength = check(password)
        print("Password strength:", strength)
        
        another = input("Do you want to assess another password? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
