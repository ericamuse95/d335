#Given an integer representing a 10-digit phone number
#output the area code, prefix, and line number using the format (800) 555-1212.

num = int(input("Enter in 10 digits for a phone number: "))
area_code = num // 10000000
prefix = (num // 10000) % 1000
line_num = num % 10000
print(f'({area_code}){prefix}-{line_num}')