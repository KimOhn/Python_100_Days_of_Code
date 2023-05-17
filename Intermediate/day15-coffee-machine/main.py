
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


def resource_check(order):
    resource_req = MENU[order]["ingredients"]
    proceed = 0
    for i in resource_req:
        #print(resource_req)
        if resources[i] < resource_req[i]:
             print(f"Sorry there is not enough {i}")
             proceed += 1
    return(proceed)


def transaction(order,payment_received):
    price = MENU[order]["cost"]
    if price > payment_received:
        print("sorry that's not enough money. refunded")
        return("fail")
    else:
        resources["money"] += price
        resource_req = MENU[order]["ingredients"]
        for i in resource_req:
            resources[i] -= resource_req[i]
        if price < payment_received:
            change = payment_received - price
            change = "{:.2f}".format(change)
            print(f"here's {change}")
        print(f"here's your {order}. Enjoy!")
        return("success")

def process_coins(order):
    quarters = int(input("No Quarters"))
    dimes = int(input("No dimes"))
    nickles = int(input("No nickles"))
    pennies = int(input("No pennies"))
    payment_received = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    return(payment_received)

#initialize
run = True
resources["money"] = 0
while run:
    order = input("what would you like?").lower()
    if order == "off":
        run = False
    elif order == "report":
        print(resources)
    else:
        if resource_check(order) ==0:
            payment_received = process_coins(order)
            transaction(order, payment_received)



