#URL: https://leetcode.com/problems/product-of-array-except-self/submissions/2198534444/
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i]*prefix
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix = nums[i]*postfix
        return res