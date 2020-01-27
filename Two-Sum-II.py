#Leet Code Problem 1

#Creating Global Variables
nums = [2,7,11,15]
target = 9
final_answer = [0,0]
compliment = 0
answer = [0,0]

#List trhrough Nums, Check each Value
def Two_Sum(nums, target):
	for idx, vals in enumerate(nums):
		print("test", idx, vals)
		compliment = target - vals
		print("Index Val: ", nums.index(vals))
		print("Index Compliment: ", nums.index(compliment))
		if compliment in nums and nums.index(vals) == nums.index(compliment):
			final_answer[0] = nums.index(vals)
			final_answer[1] = nums.index(compliment) + 1
			answer = [final_answer[0], final_answer[1]]
			print(answer)
			return answer
		elif compliment in nums:
			final_answer[0] = nums.index(vals)
			final_answer[1] = nums.index(compliment)
			answer = [final_answer[0], final_answer[1]]
			print(answer)
			return answer

#Call function
Two_Sum(nums,target)
