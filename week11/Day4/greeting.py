import datetime

now = datetime.datetime.now()
curr_hour = now.hour


def greet(now_time):
    greeting = ""
    if 8 <= now_time < 13:
        greeting = "Morning"

    if 13 <= now_time < 17:
        greeting = "Afternoon"

    if 17 <= now_time < 21:
        greeting = "Evening"

    if 21 <= now_time < 8:
        greeting = "Night"

    return "Good {}".format(greeting)


print(greet(curr_hour))
