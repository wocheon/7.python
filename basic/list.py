#!/usr/bin/env python

print ("#1")
names=['john', 'jane', 'tome']
print ("var : " + str(names))
print('names[0] :' + names[0])
print('names[1] :' + names[1])
print('names[2] :' + names[2])
#print('names[3] :' + names[3])
print ("\n")

print ("#2")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print ("var : " + str(nested_list))

list_num_1=0
list_num_2=0
print ("for start")

for i in nested_list:	
	for k in i:
		print ("var[" + str(list_num_1) + "][" + str(list_num_2) + "] : " +  str(k) )
		list_num_2 = list_num_2 + 1
	
	list_num_1 = list_num_1 + 1
	list_num_2 = 0

print ("for end")
