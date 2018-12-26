# 乘法表
for i in range(1, 10):
	for j in range(1, i+1):
		print('%d × %d = %d'%(i, j, i*j), end='\t')
	print()
print('*'*20)
for i in range(9, 0, -1):
	for j in range(9, i-1, -1):
		print('%d × %d = %d'%(i, j, i*j), end='\t')
	print()