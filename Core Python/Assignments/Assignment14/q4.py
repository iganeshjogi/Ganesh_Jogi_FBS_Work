# 4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

nums = [2, 7, 11, 15, 4, 5]
size = len(nums)
target = 9

for i in range(size):
    for j in range (i+1,size):
        if nums[i] + nums[j] == target:
            print(nums[i],nums[j])        
            