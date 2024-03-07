import string


def generate_password(lenth, use_uppercase, use_lowercase, use_number, use_special_chars):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_number:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Please select at least one charactor set.")
        return None
    

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    import secrets

    print("Welcom to the Password Generator!")

#user input 
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_number = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special charecters? (y/n): ").lower() == 'y'
#Genarat password 
    password = generate_password(length, use_uppercase, use_lowercase, use_number, use_lowercase)

    if password: 
        print(f"You generated password is: {password}")
