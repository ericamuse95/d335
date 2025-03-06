#Write a program with total change amount as an integer input
#output the change using the fewest coins, one coin type per line.
#The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
#Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.


amount = int(input("Change:"))

if amount <= 0:
    print("No change")
else:
    coins = [(1, "Penny"), (5, "Nickel"), (10, "Dime"), (25, "Quarter"), (100, "Dollar")]

    for value, name in reversed(coins):
        coin_count = amount // value
        if coin_count > 0:
            if coin_count == 1:
                print(f"1 {name}")
            else:
                print(f"{coin_count} {name}s")
            amount -= coin_count * value  # Subtract the equivalent value from the total



