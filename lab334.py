#Driving is expensive.
#Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input
# #output the gas cost for 20 miles, 75 miles, and 500 miles.
#output each floating-point value with two digits after the decimal point
gas_mileage_input = float(input("Gas milage: "))
cost_per_gallon_input = float(input("Cost of gas (dollars/gallon): "))

twenty_miles = 20 / gas_mileage_input * cost_per_gallon_input
seventy_five_miles = 75 / gas_mileage_input * cost_per_gallon_input
five_hundred_miles= 500 / gas_mileage_input * cost_per_gallon_input

print(f'{twenty_miles:.2f} {seventy_five_miles:.2f} {five_hundred_miles:.2f}')