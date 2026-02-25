# If the user digits 0 = ERROR
'''
sales = []

lenght = int(input("how much sales do you will register: "))

print()
for i in range(lenght):
    sale = int(input(f"Enter the {i+1}º sale: "))
    sales.append(sale)

total = sum(sales)
average = total / len(sales)
higher = max(sales)
lower = min(sales)

print(f"\nThe total of sales is: {total}")
print(f"The avarage of sales is: {average:.2f}")
print(f"The higher sale is: {higher}")
print(f"The lower sale is: {lower}")
'''

# Solucion

sales = []

lenght = int(input("how much sales do you will register: "))

print()
for i in range(lenght):
    sale = int(input(f"Enter the {i+1}º sale: "))
    sales.append(sale)

if len(sales) > 0:

    total = sum(sales)
    average = total / len(sales)
    higher = max(sales)
    lower = min(sales)

    print(f"\nThe total of sales is: {total}")
    print(f"The avarage of sales is: {average:.2f}")
    print(f"The higher sale is: {higher}")
    print(f"The lower sale is: {lower}")
else:
    print("No sales registered!")