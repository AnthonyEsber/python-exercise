VOWELS:set[str] = {'a', 'e', 'i', 'o', 'u'}

def analyze_word(word:str) -> tuple[int, int, str]:
    word_lenght:int = len(word)
    vowels_count:int = 0
    uppsercase_word:str = ''

    for c in word:
        if c in VOWELS: vowels_count += 1
    
    uppsercase_word = word.upper()

    return word_lenght, vowels_count, uppsercase_word

user_input = input("Enter a word to analyze: ")
if user_input.isalpha == False:
    print("No special characters allowed!")
    exit()


count, vowel, upper = analyze_word(user_input)

print(f"Length: {count} \
Vowels: {vowel} \
Uppercase: {upper}")
    
    


