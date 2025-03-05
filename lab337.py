#Write a program whose inputs are three integers
#output the smallest of the three values

num1 = int(input("Number: "))
num2 = int(input("Number: "))
num3 = int(input("Number: "))

nums = []
nums.append(num1)
nums.append(num2)
nums.append(num3)

print(min(nums))