
user_fav_fruits= input("Whats ur fav fruit/s? separate them by a space please ")
user_fav_fruits= user_fav_fruits.split()
user_other_fruit= input("Now please just enter any fruit you want ")
if user_other_fruit in user_fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")
