# Initialize order list
order_list = []

# Display greeting message
print("Welcome to the variety food truck.")

# Define menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Continuous loop for ordering
place_order = True
while place_order:
    print("From which menu would you like to order? ")

    # Display menu categories
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Prompt user for menu selection
    menu_selection = input("Type menu number: ")
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)
        if menu_selection in menu_items.keys():
            menu_category_name = menu_items[menu_selection]
            print(f"You selected {menu_category_name}")

            # Display sub-menu
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            sub_menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        sub_menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    sub_menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Prompt user for item selection and quantity
            menu_selection = input("Please make your selection from the menu: ")
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)
                if menu_selection in sub_menu_items:
                    selected_item = sub_menu_items[menu_selection]
                    item_name = selected_item["Item name"]
                    item_price = selected_item["Price"]
                    quantity = input(f"How many of '{item_name}' would you like to order? ")
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)
                    order_list.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })
                else:
                    print("That selection is not valid. Please try again.")
        else:
            print("Please enter a valid number for your selection.")
    else:
        print("That menu category does not exist. Please try again.")

    # Prompt user if they want to continue ordering
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").upper()
        if keep_ordering == "Y":
            break
        elif keep_ordering == "N":
            place_order = False
            break
        else:
            print("Please try again, that was not a valid input.")

# Print order receipt
print("\nOrder Receipt")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
total_cost = 0
for item in order_list:
    item_name = item["Item name"]
    item_price = item["Price"]
    quantity = item["Quantity"]
    num_name_spaces = 25 - len(item_name)
    name_spaces = " " * num_name_spaces
    price_str = f"${item_price:.2f}"
    num_price_spaces = 7 - len(price_str) + 1
    price_spaces = " " * num_price_spaces
    print(f"{item_name}{name_spaces}| {price_str}{price_spaces}| {quantity}")
    total_cost += item_price * quantity

print(f"\nTotal cost: ${total_cost:.2f}")
