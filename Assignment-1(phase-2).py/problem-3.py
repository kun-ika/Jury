def process_orders(o1, o2, o3):
    print(f"\nPreparing Your Order_1 - ({o1})")
    print(f"Preparing Your Order_2 - ({o2})")
    print(f"Preparing Your Order_3 - ({o3})\n")
    print(f"The following order has been dispatched")
    print(f"Order_1 : {o1}")
    print(f"Order_2 : {o2}")
    print(f"Order_3 : {o3}")

order1 = input("Enter an order 1: ")
order2 = input("Enter an order 2: ")
order3 = input("Enter an order 3: ")

process_orders(order1, order2, order3)