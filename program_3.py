def calculate_total_purchase():
    item1 = float(input("Enter the price of item 1: $"))
    item2 = float(input("Enter the price of item 1: $"))
    item3 = float(input("Enter the price of item 1: $"))
    item4 = float(input("Enter the price of item 1: $"))
    item5 = float(input("Enter the price of item 1: $"))

    subtotal = item1 + item2 + item3 + item4 + item5 
    tax = subtotal * 0.07
    total = subtotal + tax 

    print("----- Receipt -----")
    print("Subtotal: $", format(subtotal, ".2f"), sep="")
    print("Sales Tax 7%: $", format(tax, ".2f"), sep="")
    print("Total: $", format(total, ".2f"), sep="")


calculate_total_purchase() 