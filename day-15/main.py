MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


dict = {
    "money": 0
}


def coins():
    print("Please input coins?: ")
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total = (quarter * quarters) + (dime * dimes) + (nickle * nickles) + (penny * pennies)
    return total


def drink_choice(drink):
    if resources["water"] < all_choice["water"]:
        print("Sorry there isn't enough water")
        exit()
    elif resources["milk"] < all_choice["milk"]:
        print("Sorry there isn't enough milk.")
        exit()
    elif resources["coffee"] < all_choice["coffee"]:
        print("Sorry there isn't enough coffee")
        exit()


def total_cost():
    total = float(coins())
    esp_cost = MENU[choice]["cost"]
    if total < esp_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif total > esp_cost:
        change = round(total - esp_cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice} ☕️. Enjoy! ")


def whats_left(all_choice, money_choice):
    resources["water"] -= all_choice["water"]
    resources["milk"] -= all_choice["milk"]
    resources["coffee"] -= all_choice["coffee"]
    dict["money"] += money_choice


# TODO 1 What would you like to order
end_of_coffee_machine = False
while not end_of_coffee_machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso":
        esp_choice = MENU[choice]["ingredients"]
        if resources["water"] < esp_choice["water"]:
            print("Sorry there isn't enough water")
            exit()
        elif resources["coffee"] < esp_choice["coffee"]:
            print("Sorry there isn't enough coffee")
            exit()
        resources["water"] -= esp_choice["water"]
        resources["coffee"] -= esp_choice["coffee"]
        dict["money"] += MENU[choice]["cost"]
        total_cost()
    elif choice == "latte":
        all_choice = MENU[choice]["ingredients"]
        money_choice = MENU[choice]["cost"]
        drink_choice(all_choice)
        whats_left(all_choice, money_choice)
        total_cost()
    elif choice == "cappuccino":
        all_choice = MENU[choice]["ingredients"]
        money_choice = MENU[choice]["cost"]
        drink_choice(all_choice)
        whats_left(all_choice, money_choice)
        total_cost()
    elif choice == "report":
        for keys in resources:
            print(keys, ":", resources[keys])
        for x in dict:
            print(x, ":", dict[x])
    elif choice == "off":
        end_of_coffee_machine = True

# TODO 2 OFF, REPORT
