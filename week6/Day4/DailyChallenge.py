current_year = 2021
user_birthday = input("What is your birthday? DD/MM/YYYY\n").split("/")
user_birthday = user_birthday
candle_number = (current_year - (int(user_birthday[2]))) % 10
candles = candle_number * "i"
birthday_cake = '''
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''
print(birthday_cake.replace('iiiii', candles))