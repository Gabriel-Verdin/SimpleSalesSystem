def get_sales():
    sales = []
    lenght = int(input("How much sales do you want to register: "))

    for i in range(lenght):
        sale = float(input(f"Enter the {i + 1}º sale: "))
        sales.append(sale)
        
    return sales