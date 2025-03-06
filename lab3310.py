#Write a program that takes in a line of text as input
#outputs that line of text in reverse.
#The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

while True:
    user_input = input("Input: ")

    if user_input.lower() in ["done","d"]:
        break
    print(user_input[::-1])