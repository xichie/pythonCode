f = open('./num.txt')

top_10 = []
for line in f.readlines():
	num = int(line)
	if len(top_10) == 10:
		top_10.sort()
		top_10[0] = num if top_10[0] < num else top_10[0]
	else:
		top_10.append(num)	

top_10.sort()		
print(top_10)