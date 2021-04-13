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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Insert the coins.")
    total = int(input("insert quarters "))*0.25
    total += int(input("insert dimes ")) * 0.1
    total += int(input("insert  nickles ")) * 0.05
    total += int(input("insert pennies ")) * 0.01
    return total

def check_transcation(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        global profit
        profit+=drink_cost
        print(f"Here is {change} dollars in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredents):
    for item in order_ingredents:
        resources[item]-=order_ingredents[item]
    print(f"Here is your {drink_name} ☕ ")


machine_on=True


while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice=="off":
        machine_on=False
    elif user_choice=="report":
        print(f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:{profit}")
    else:
        drink=MENU[user_choice]
        if check_resource(drink["ingredients"]):
            payment=process_coins()
            if check_transcation(payment,drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])
