#!/usr/bin/env python

user = {'name': 'Wocheon', 'age': 30, 'city': 'Seoul'}

print(user)
print(user['name'])
print(user['age'])
print(user['city'])
#print(user['gender'])
print(user.get('gender'))


number=dict(t1='one', t2='two', t3='three')
 
print(number.keys())
print(number.values())

number_cp=number.copy()
number_cp['t4']='four'
number_cp['t1']='frist'
number_cp.pop('t2')
print(number_cp)


del number_cp['t3']
print(number_cp)

user.clear()
print(user)


if 't1' in number_cp:
	print ( 'key t1 in dictionary')
else:
	print ( 'key t1 not exist')
