import re


def check_password(password):
    must = '[A-Z]+[a-z]+[0-9]+[_@$]'
    check = re.search(must, password)
    while not 6 < len(password) < 30:
        password = input("Your password must include 6-30 chars. Enter a new one:\n")
    if check:
        print(f"Your password is {password}.\nPlease make sure to keep it safe!")
    elif not check:
        password = input("Your password must include at least A-Z, a-z, 0-9, special char. Enter a new one:\n")
        print(f"Your password is {password}.\nPlease make sure to keep it safe!")


check_password(input("Please enter a password of 6-30 chars:\n"))
