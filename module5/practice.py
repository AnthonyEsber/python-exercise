VOWELS:set[str] = {'a', 'e', 'i', 'o', 'u'}

'''
Function to check even numbers
'''
def is_even(number: int) -> bool:
    if number % 2 == 0: return True
    return False

user_input = input("Enter a number: ")

if user_input.isdigit() == False:
    print("Characters not allowed")
    exit()
else: user_input = int(user_input)

result:bool = is_even(number=user_input)

print(result)

'''
Function to return the max of two numbers
'''
def max_num(number: int) -> int:
    decimal:int = number % 10
    tens:int = number // 10

    if decimal > tens:
        return decimal 
    return tens

user_input = input("Enter a number: ")
user_input.strip()

if user_input.isdigit() == False or len(user_input) > 2 or len(user_input) < 1:
    print("Characters not allowed, 2 digit number only!")
    exit()
else: user_input = int(user_input)

result_max:int = max_num(user_input)

print(result_max)

'''
Count vowels in a string
'''

def count_vowels(input:str) -> int:
    counter:int = 0
    for c in input:
        if c in VOWELS:
            counter += 1
    return counter

user_input = input("Enter a word: ")
user_input.strip()

if user_input.isalpha() == False:
    print("Numbers or special characters not allowed")
    exit()

print(count_vowels(user_input))

'''
Take list and return sum of the numbers in list
'''

def sum_list(number:list[int]) -> int:
    sum:int = 0
    for x in number:
        sum += x
    return sum
        

user_input = None
num_list:list[int] = []
while (user_input != ''):
    user_input = input("Enter number for list, enter empty to stop: ")
    if user_input.isnumeric():
        int_input = int(user_input)
        num_list.append(int_input)
    elif user_input == '':
        break
    else:
        print("Must be a number! \n")

print(sum_list(num_list))

'''
Take list and a number return true if the number is in list
'''

def check_number_list(number_list:list[int], number_check:int) -> bool:
    if number_check in number_list:
        return True
    return False


user_input = input("Enter a number to check if it is present in the previous list: ")

if user_input.isdigit() == False:
    print("Characters not allowed")
    exit()
else: user_input = int(user_input)

print(check_number_list(num_list, user_input))