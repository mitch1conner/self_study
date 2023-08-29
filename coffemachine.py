import sys
from coffee import Coffee
from storage import *

water_level = 3000
coffee_weight = 1000
milk_level = 2000

while True:
    choice = input("What would you like? (espresso/latte/cappuccino/off/Show storage/Check storage):").lower()
    
    if choice == "off":
        sys.exit()  # Programı kapat
    elif choice in ["espresso", "latte", "cappuccino"]:
        pay = input("Enter your change as quarters,dimes,nickels,pennies:")
        values = [float(value.strip()) if value.strip() else 0 for value in pay.split(',')]
        
        while len(values) < 4:
            values.append(0)
        total_price = values[0]*0.25 + values[1]*0.10 + values[2]*0.05 + values[3]*0.01
        
        if choice == "espresso":
            espresso = Coffee("Espresso", 18, 50, 0, 1.5)
            espresso.report_product()
            espresso.pay_method(total_price_class=total_price)
            print("☕")
            water_level -= espresso.water
            coffee_weight -= espresso.coffee
            milk_level -= espresso.milk
        elif choice == "latte":
            latte = Coffee("Latte", 24, 200, 150, 2.5)
            latte.report_product()
            latte.pay_method(total_price_class=total_price)
            print("☕")
            water_level -= latte.water
            coffee_weight -= latte.coffee
            milk_level -= latte.milk
        elif choice == "cappuccino":
            cappuccino = Coffee("Cappuccino", 24, 250, 100, 3.5)
            cappuccino.report_product()
            cappuccino.pay_method(total_price_class=total_price)
            print("☕")
            water_level -= cappuccino.water
            coffee_weight -= cappuccino.coffee
            milk_level -= cappuccino.milk
    elif choice == "show storage":
        show_storage(milk_level, coffee_weight, water_level)
    elif choice == "check storage":
        check_storage(milk_level, coffee_weight, water_level)
