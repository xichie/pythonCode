

def bubbleSort(a : "List", reverse = False ) -> "List":
	import copy
	nums = copy.deepcopy(a)
	for i in range(1, len(nums)):
		flag = True
		for j in range(len(nums) - i):
			if reverse:
				if nums[j] < nums[j + 1]:
					temp = nums[j]
					nums[j] = nums[j+1]
					nums[j+1] = temp
					flag = False
			else:
				if nums[j] > nums[j + 1]:
					temp = nums[j]
					nums[j] = nums[j+1]
					nums[j+1] = temp
					flag = False
	return nums


a = [5, 3, 8, 2, 4]
sorted_a = bubbleSort(a, True)

print(sorted_a)
print(a)
