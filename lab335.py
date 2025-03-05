#Given input characters for an arrowhead and arrow body, print a right-facing arrow.

arrow_head = input("Arrow head: ")
arrow_body = input("Arrow body: ")

row1 = "      " + arrow_head
row2 = arrow_body * 6 + arrow_head * 2
row3 = arrow_body * 6 + arrow_head * 3

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)