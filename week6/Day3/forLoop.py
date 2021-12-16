mult_table=range(1,11)
mult_input=int(input("please enter a number "))
#option1:
mult = [mult_input * mult_index for mult_index in mult_table]
#option2:
for mult_index in mult_table:
    print(mult_input*mult_index)
#option3:
num = int(input("please enter a number "))
for index in range(1, 9):
    print(num, 'x', index, '=', num*index)
