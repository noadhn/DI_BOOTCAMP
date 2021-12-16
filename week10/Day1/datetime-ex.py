import random
import string
import datetime
from Faker import faker

rand_str = ''
for i in range(5):
    letter = random.choice(string.ascii_letters)
    rand_str += letter
print(rand_str)


def current_date():
    datetime_object = datetime.date.today()
    print(datetime_object)


current_date()


def time_left():
    january_first = datetime.date(2022, 1, 1)
    today_date = datetime.date.today()
    delta = (january_first-today_date).days
    print(f"There are {delta} days left until {january_first}")


time_left()


def how_much_mins_alive(birthdate: str):
    birthdate = birthdate.split(', ')
    birthdate_format = datetime.datetime(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
    today_date = datetime.datetime.today()
    alive_delta = (today_date-birthdate_format)
    sec_alive = alive_delta.total_seconds()
    mins_alive = sec_alive / 60
    print(f"youre alive for {mins_alive} minutes")


how_much_mins_alive(input("enter time in this format yyyy, m, d:\n"))
