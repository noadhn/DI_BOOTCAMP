family_members = int(input("How many people are u? "))
ticket_price = 0
i = 0
while i < family_members:
    client_age = int(input("How old is the person the ticket's for? "))
    if client_age <= 3:
        ticket_price += 0
    if  3 < client_age <= 12:
        ticket_price += 10
    if client_age > 12:
        ticket_price += 15
    i += 1

print("The total ticket's price is "+str(ticket_price)+" shekels")

teen_group = int(input("How many people are u? "))
num = 0
teen_age = 0
teen_name = ""
permitted_teens_list = []
while num < teen_group:
    teen_age = int(input("What's ur age? "))
    if 16 < teen_age <= 21:
        teen_name = input("You are the right age for this movie, What's ur name? ")
        permitted_teens_list.append(teen_name)
    if teen_age < 16 or teen_age > 21:
        print("This movie isn't for you")
    num += 1
    if len(permitted_teens_list) > 0:
        print("only "+str(permitted_teens_list)+ " can watch this movie, HAVE FUN!")
    if len(permitted_teens_list) == 0:
        print("Sorry guys, but no one of you is the right age for this movie")
