# EX 1: Hello World
print("Hello World\n"*5)

# EX 2: Some Math
# didnt understand the ex

# EX 3: What is the output?
print(5 < 3) # False
print(3 == 3) # True
print(3 == "3") # False
#print("3" > 3) # error
print("Hello" == "hello") # False

# EX 4: Your Computer Brand
computer_brand= "Apple"
print("I have an {} computer".format(computer_brand))

# EX 5: Your Information
name= "noa"
age=20
shoe_size=39
info="My name is {}, I'm {} yo, my shoes size is {} and I'VE NEVER EAT COTTAGE CHEESE.".format(name, age, shoe_size)
print(info)

# EX 6: A&B
a=4
b=6
if a>b:
    print("Hello World")

# EX 7: Odd or Even
num =int(input("please enter a number"))
if num%2==0:
    print("even number ")
elif num%2==1:
    print("odd number")

#EX 8: What’s Your Name ?
name =input("whats ur name?")
if name=="noa" or name=="Noa":
    print("not surprising ha?")
else:
    print("ur parents gave you a more original name apparently")

#EX 9: Tall Enough To Ride A Roller Coaster
height=int(input("please enter ur height in inches"))
inch= 2.54
height_cm=height*inch
if height_cm> 145:
    print("high enough")
else:
    print("you need to grow boy")