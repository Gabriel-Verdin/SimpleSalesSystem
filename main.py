from input_handler import get_sales
from calculations import calculate_total, calculate_average, calculate_highest, calculate_lowest
from report import show_report

def main():
    sales = get_sales()

    if len(sales) > 0:
        total = calculate_total(sales)
        average = calculate_average(sales)
        highest = calculate_highest(sales)
        lowest = calculate_lowest(sales)

        show_report(total, average, highest, lowest)

    else:
        print("No sales registered!")

if __name__ == "__main__":
    main()