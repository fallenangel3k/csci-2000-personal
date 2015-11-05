def has_no_e(string):
	num = string.count('e')
	if num == 0:
		return True
	else:
		return False

file = open('gadsby_stripped.txt', 'r')
line = file.readline()
while line != '':
	if not has_no_e(line):
		print(line)
	line = file.readline()
file.close()
