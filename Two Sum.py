#URL: https://leetcode.com/problems/two-sum/
#neet code solution video ref:https://youtu.be/KLlXCFG5TnA
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

#optimized
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            #keys are compared with entered value in dictonary
            if str(diff) in count:
                return [nums.index(int(diff)),i]
            count[str(nums[i])] = count.get(str(nums[i]),0)+1


            
        