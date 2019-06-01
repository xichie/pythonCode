
import time

def selection_sort(a : "List", reverse=False) ->"List":
	import copy
	nums = copy.deepcopy(a)
	for i in range(len(nums) - 1):
		flag = i
		for j in range(i+1, len(nums)):
			if reverse:
				if nums[j] > nums[flag]:
					flag = j
			else:
				if nums[j] < nums[flag]:
					flag = j
		
		if i != flag:
			temp = nums[flag]
			nums[flag] = nums[i]
			nums[i] = temp
	
	return nums

a = [5, 3, 8, 2, 4,5, 3, 8, 2, 4]

startime = time.time()
sorted_a = quick_sort(a, True)
endtime = time.time()
print("选择排序算法执行了%f秒"%((endtime - startime)))
print(sorted_a)
print(a)
