import datetime, time

today_date = datetime.date.today()
birthday = datetime.date(2022, 8, 26)
countdown = birthday - today_date
i = 0
print(f"Today is the {today_date.day}/{today_date.month}/{today_date.year}")
print(f"Your birthday is the {birthday.day}/{birthday.month}/{birthday.year}")
while countdown.days >= i:
    if countdown.days - i > 1:
        print(f"There are {countdown.days-i} days left")
    if countdown.days-i == 1:
        print(f"There is {countdown.days-i} days left")
    if countdown.days - i == 0:
        print(f"Today is the day!")
    time.sleep(1)
    i += 1
