str = input("please enter a string of 10 characters ")
if len(str) < 10:
    print("string not long enough")
elif len(str) > 10:
    print("string too long")
str_array = []
str_array[:] = str

print('first char is '+str_array[0]+' and last char is '+str_array[len(str_array)-1])

letter = 1
for x in str_array:
   print(str[:letter])
   letter += 1

import random
def shuffled_str(str_array):
    random.shuffle(str_array)
    return str_array

print("The shuffled new string is "+', '.join(shuffled_str(str_array)))