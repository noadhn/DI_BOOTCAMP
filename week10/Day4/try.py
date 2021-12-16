import json

students = [
	{
		"name": "Lisa Simpson",
		"age": 8
	},
	{
		"name": "Janey Powell",
		"age": 9
	},
	{
		"name": "Ralph Wiggum",
		"age": 8
	}
]

to_find = input("Enter the name of the student whose age you want to find: ")

for s in students:
	if students["name"] == to_find:
		print("The age of {} is {}.".format(students["name"], students["age"]))