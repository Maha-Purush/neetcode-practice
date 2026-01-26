#Problem: Find all numbers disappeared in an array
#Difficulty: Easy
#Time Complexity: O(n)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums) + 1 )) - set(nums))