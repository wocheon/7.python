#!/usr/bin/env python

var="1234"
print ("var : " + var)

res=len(var)
print (f"len : " + str(res))

res=max(var)
print ("max : " + str(res))

res=min(var)
print ("min : " + str(res))

res=var.isdigit()
print ("isdigit : " + str(res))

res=var.isalpha()
print ("isalpha : " + str(res))

res=var.isalnum()
print ("isalnum : " + str(res))

res=var.isspace()
print ("isspace : " + str(res))

