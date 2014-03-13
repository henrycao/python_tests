#!/bin/env python

dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B' }

converted_list = []

def convert(num, base):
	num = abs(num)
	remainder = num % base
	if num >= base:
		convert(num /base, base)
	converted_list.append(remainder)

def format_print(num, base):
	if num < 0:
		result = '-'
	else:
		result = ''
	convert(num, base)

	for item in converted_list:
		if item in dic.keys():
			item = dic[item]
		item = str(item)
		result += item
	print result


for i in range(0,100):
	converted_list = []
	format_print(i,12) 
