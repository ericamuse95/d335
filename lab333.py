#Given four values representing counts of quarters, dimes, nickels and pennies
#output the total amount as dollars and cents.
#output each floating-point value with two digits after the decimal point

quarter = .25
dime = .10
nickel = .05
penny = .01

quarters_input = int(input("Number of quarters: "))
dimes_input = int(input("Number of dimes: "))
nickels_input = int(input("Number of nickles: "))
pennies_input = int(input("Number of pennies: "))

quarters_total = quarters_input * quarter
dimes_total = dimes_input * dime
nickels_total = nickels_input * nickel
pennies_total = pennies_input * penny

total = quarters_total + dimes_total + nickels_total + pennies_total
print(f'{total:.2f}')
