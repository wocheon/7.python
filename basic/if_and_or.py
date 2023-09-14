#!/usr/bin/env python

a=1

while a<=30:
	div=a%5
	div_mod=divmod(a, 5)
	if div==0 or a==1:
		print( str(a) + ": true " +  str(div_mod) )
	elif div==1 and a <= 20:
		print( str(a) + ": check " +  str(div_mod) )
	else:
		print( str(a) + ": false " +  str(div_mod) )
	a = a + 1

print("done")
