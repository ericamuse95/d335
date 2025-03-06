
#Write a program whose input is a word or phrase that outputs whether the input is a palindrome.
user_input = input("Word: ")
word = user_input

if word == word[::-1]:
    print("true")
else:
    print("false")
