#Write a program whose input is two integers
#Output the first integer
#and subsequent increments of 5 as long as the value is <= to the second integer.
#End with a newline.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 > num2:
    print("Second integer can't be less than the first.")
else:
    current_value = num1
    while current_value <= num2:
        print(current_value, end=" ")
        current_value +=5