number_list = ['hi', 1, 2, 4, 'test', 4, 'hi']


'''
Remove duplicates
'''
def remove_duplicates(number_list):
    set_list = set(number_list)

    return list(set_list)

print(remove_duplicates(number_list))

persons = [('John Doe', 67),('Anthony Esber', 23),('John Appleseed', 42)]

'''
Oldest person
'''

def oldest_person(persons):
    oldest = persons[0]
    for name, age in persons:
        if age > oldest[1]:
            oldest = (name, age)
    return oldest

print(oldest_person(persons))

numbers = (1, 2, 4, 4, 4, 5, 5, 2, 1, 6, 4, 7, 2, 2, 2)

def fecvent_tuple(numbers):
    max_frequency = 0
    most_frequent = numbers[0]

    for x in numbers:
        if numbers.count(x) > max_frequency:
            max_frequency = numbers.count(x)
            most_frequent = x
    return most_frequent

print(fecvent_tuple(numbers))


def words(string):
    word_list = string.lower().split()

    max_frequency = 0
    most_frequent = None

    for x in word_list:
        if word_list.count(x) > max_frequency:
            max_frequency = word_list.count(x)
            most_frequent = x

    print(most_frequent)
    print(max_frequency)

text = "apple banana apple orange banana apple"

words(text)

