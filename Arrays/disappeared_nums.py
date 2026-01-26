#Problem: Find all numbers disappeared in an array
#Difficulty: Easy
#Time Complexity: O(n)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = set(nums)
        test = set(range(1, n + 1 ))
        missing = list(test - nums)
        return missing