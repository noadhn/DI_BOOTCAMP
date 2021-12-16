import math

list_ex = []
list_ex.insert(0, "me") #1

list_ex_spaces =list_ex.count(' ') #2

lower_count = 0 #3
upper_count = 0
for item in list_ex:
    for letters in item:
        if letters.islower():
            lower_count += 1

        if letters.isupper():
            upper_count += 1


def sum_list_items(list_num): #4
    sum_list = 0
    for num in list_num:
        sum_list += num


def find_max_num_in_list(list_num): #5
    max_num = list_num[0]
    for every in list_num:
        if every > max_num:
            max_num = every


def find_factorial(num_fact): #6
    num_fact = int(input("Enter a number: "))
    index_fact = 1
    factorial = 1
    while num_fact >= 1:
        factorial *= num_fact
        num_fact -= 1


counter = 0 #7
element_to_count = str(input("Which element do you want to count in the list? "))
for elem in list_num:
    if str(elem) == element_to_count:
        counter += 1

index_square = 0 #8
sum_square = 0
num_square_list = []
while index_square < 3:
    number_square = int(input("enter a number: "))
    sum_square += number_square * number_square
    num_square_list.append(number_square)
    index_square += 1
square_root_num = math.sqrt(sum_square)


print(num_square_list.sort(reverse=True))

print("EX8: L2-norm of all these numbers is: " + str(square_root_num))
print("EX7:" + element_to_count + " appear " + str(counter) + " time in list_num")
print("EX6: The factorial is: " + str(find_factorial(num_fact)))
print("EX5: Max num in list_num is: " + str(find_max_num_in_list(list_num=[1, 2, 3, 4, 5])))
print("EX4: Sum of the array is: " + str(sum_list_items(list_num=[1, 2, 3, 4, 5])))
print("EX3: Lower cases: " + str(lower_count))
print("EX3: Upper cases: " + str(upper_count))
print("EX2: Spaces: " + str(list_ex_spaces))
print("EX1: List items: " + str(list_ex))