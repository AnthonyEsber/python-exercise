user_input = input("Enter a password: ")
user_input.strip()

if(len(user_input) >= 8 and any(x.isupper() for x in user_input) and any(x.isdigit() for x in user_input)):
    print("Strong password!")
else:
    print("Weak password!")

user_input = input("Enter a word: ")
user_input.strip()

if user_input.isalpha() == False or len(user_input) < 1:
    print("[BAD INPUT] A word with no whitespace or numbers is required!")
    exit()

VOWEL = ['a', 'e', 'i', 'o', 'u']

for c in user_input:
    if c.lower() in VOWEL:
        print(c)