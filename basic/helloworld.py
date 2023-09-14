#!/usr/bin/env python

var="Hello, World"

print (var)
print (var * 2)

result= "hello" in var
print (result)

print (var[4])
print (var[7:])

print (var.split())
print (var.split(','))

print (var.find(','))
print (var.replace(',', ''))

print (var.upper())
print (var.lower())

list=list(var)
print (list)

tup=tuple(var)
print (tup)
