# This was the day 3 task for: TOTAL Python: Become an Advanced Python Developer in 16 days
# This challenge did not allow error handling, user input validation, and use of loops or if/then statments


user_text = input("Please enter any text:").lower()
print("Text Set")
user_letters = input("Please provide three letters to search for: ").lower().split()
print("Letters Set")

print("\nTASK 1 - LETTER CHECK:")
print("The letter: " + user_letters[0] + " was found: " + str(user_text.count(user_letters[0])) + " times")
print("The letter: " + user_letters[1] + " was found: " + str(user_text.count(user_letters[1])) + " times")
print("The letter: " + user_letters[2] + " was found: " + str(user_text.count(user_letters[2])) + " times")

print("\nTASK 2 - TOTAL WORDS:")
convert_text = list(user_text.split())
print("The total number of words in the user provided text is: " + str(len(convert_text)))

print("\nTASK 3 - FIRST AND LAST LETTERS")
print("The first letter of the user provided text is: " + user_text[0])
print("The last letter of the user provided text is: " + user_text[-1])

print("\nTASK 4 - INVERT TEXT AND JOIN TEXT")
invert_text = ' '.join(convert_text[::-1])
print("The inverted user provided text is: ")
print(invert_text)

print("\nTASK 5 - SEARCH FOR THE WORD PYTHON")
target_word = 'python'
search_text = target_word in convert_text
bool_finder = {True: "The word 'python' is in the user provide text", False: "The word 'python' is not in the user provided text"}
print(bool_finder.get(search_text))
