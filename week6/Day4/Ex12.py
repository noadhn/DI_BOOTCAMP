

users_list = []
user_age = ""
user_name = ""
i = 0
users = int(input("How many users? "))
while i < users:
    print(str(i+1)+"st person:")
    user_name = input("Whats ur name? ")
    users_list.append(user_name)
    user_age = int(input("How old are you? "))
    if user_age < 16:
        users_list.remove(user_name)
    i += 1
if len(users_list) == 0:
    print("Final users list is empty")
else:
    print("Final users list is" + str(users_list))