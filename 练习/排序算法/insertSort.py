import time

def insert_sort(a : "List", reverse = False) -> "List":
	import copy
	nums = copy.deepcopy(a)
	
	for i in range(1, len(nums)):
		temp = nums[i]  # 记录当前要插入的数
		j = i
		while j>0 and temp<nums[j-1]:
			nums[j] = nums[j-1]
			j -= 1
		if j != i:
			nums[j] = temp
	return nums

a = [5, 3, 8, 2, 4,5, 3, 8, 2, 4]

startime = time.time()
sorted_a = insert_sort(a, True)
endtime = time.time()
print("插入排序算法执行了%f秒"%((endtime - startime)))
print(sorted_a)
print(a)