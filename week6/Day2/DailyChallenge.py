import random
user_string = input("please enter a string of 10 characters ")
if len(user_string) < 10:
    print("string not long enough")
elif len(user_string) > 10:
    print("string too long")
string_array = [] #can use also user_string[0]
string_array[:] = user_string

print('first char is ' + string_array[0] + ' and last char is ' + string_array[len(string_array) - 1])

letter = 1
for x in string_array: #can use also range
   print(user_string[:letter])
   letter += 1

def shuffled_str(str_array):
    random.shuffle(str_array)
    return str_array

print("The shuffled new string is " +', '.join(shuffled_str(string_array)))