#Leet Code Problem 1

#Creating Global Variables
nums = [3,3]
target = 6

#List trhrough Nums, Check each Value
def Two_Sum(nums,target):
	for i in range(0, len(nums)):
		complement = target - nums[i]
		for j in range(i + 1, len(nums)):
			if complement == nums[j]:
				final_answer = [i, j]
				print(final_answer)
				return final_answer

#Call function
Two_Sum(nums,target)
