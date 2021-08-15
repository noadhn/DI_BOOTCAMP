user_pizza_toppings = ""
pizza_price = 10
i = 0
while user_pizza_toppings != "quit":
    user_pizza_toppings = input("What toppings would you like on ur pizza?\nEnter 'quit' if it's enough ")
    print("I'll add "+user_pizza_toppings+" to ur pizza")
    if user_pizza_toppings == "quit":
        break
    i += 2.5
total_price = pizza_price + i
print("your pizza will cost "+ str(total_price)+" shekels")
