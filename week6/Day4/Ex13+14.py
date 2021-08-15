#Ex 13
sandwich_orders = ["salami", "Nutella", "cheese", "mozzarella"]
finished_sandwiches = []
i = 0
if len(sandwich_orders) >= 0:
    ready = input("What sandwich is ready?\nsalami\nNutella\ncheese\nmozzarella\n").split(", ")
    for x in ready:
        if ready[i] in sandwich_orders:
            finished_sandwiches.append(x)
            sandwich_orders.remove(x)
            i += 1
if len(sandwich_orders) == 0:
    for x in finished_sandwiches:
        print("I made your " + x + " sandwich")

#Ex 14
pastrami = "pastrami"
i = 0
for i in range(4):
    sandwich_orders.append(pastrami)

print("We're sorry but the deli is out of pastrami")
pastrami_occurrences = sandwich_orders.count("pastrami")

while pastrami in sandwich_orders:
        sandwich_orders.remove(pastrami)
print(sandwich_orders)
