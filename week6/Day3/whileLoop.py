#num = 1
#while num < 11:
    #print(num)
    #num+=1

current_number = 0
while current_number < 10:
    current_number += 1
    if 3 < current_number < 7: # If the number is between 3 and 7
        continue                # Go back to the beginning of the loop
    print(current_number)

secret_number = 4
while True:
  user_number = input('Guess the secret number: ')
  if int(user_number) == secret_number:
    print('Congrats! You win!')
    break
  else:
    print('Wrong guess...')