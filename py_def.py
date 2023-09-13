#!/usr/bin/env python

#1
def sum(a,b):
	res = a + b 
	return res

print (sum(1,2))


#2
def print_hello():
	print ("Hello World")

print_hello()


#3
def print_input(name="test", age="30"):
	#name = input('name : ?')
	#age = input('age : ?')
	return name, age

res=print_input()
name=res[0] 
age=res[1]

print(res)
print("name : " + name)
print("age : " + age)

#4
def greet(name, msg="Hello World"):
	print (f"{msg} , {name}!")

greet('hello','test')
greet('test')

#5
def sum_numbers(*args):
	total = 0
	for number in args:
		total += number
	return total

result = sum_numbers(1, 2, 3, 4, 5)
print(result)


#6
def print_info(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

print_info(name="test", age=30, city="seoul")


#7
def print_mixed_info(title, *args, **kwargs):
    print(f"title : {title}")
    print("args :", end=" ")
    for arg in args:
        print(arg, end=" ")
    print()
    print("key_value :")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_mixed_info("profile", "argument1", "argument2", name="test", age=30, city="seoul")
