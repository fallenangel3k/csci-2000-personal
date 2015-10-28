#!/usr/bin/python
import io

f = open("./gadsby_stripped.txt")

l = readline(f)
while(l):
	readline(f)
	print(has_no_e(l))
	

def has_no_e(line):
	if(line.contains("e")):
		return false
	else:
		return true
