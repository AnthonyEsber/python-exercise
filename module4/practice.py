
user_input = input("Enter a number: ")

if user_input.isdigit() == False:
    print("[BAD INPUT] A number is required!")
    exit()
else:
    user_input = int(user_input)

# pozitiv sau negativ

if user_input > 0:
    print("positive number")
elif(user_input < 0 ):
    print("negative number")
else:
    print("zero")

# par sau impar

if user_input % 2 == 0:
    print("even number")
else:
    print("odd number")

# vocala sau consoana

user_input = input("Enter a letter: ")

if user_input.isalpha() == False or len(user_input) > 1:
    print("[BAD INPUT] A 1-char letter is required!")
    exit()

VOCALS = 'aeiou'

if user_input.lower() in VOCALS:
    print("input is a vocal")
else:
    print("input is a consonant")

# age check

user_input = input("Enter your age: ")

if user_input.isdigit() == False:
    print("[BAD INPUT] A number is required!")
    exit()
else:
    user_input = int(user_input)

if user_input < 18 or user_input > 65:
    print("reducere!!!")
else:
    print("fara reducere =(")


# an bisect

user_input = input("Enter a year: ")

if user_input.isdigit() == False:
    print("[BAD INPUT] A number is required!")
    exit()
else:
    user_input = int(user_input)

if user_input % 4 == 0:
    print("An bisect.")
else:
    print("Nu e bisect")