# Problem: Array which contains duplicates.
# Time Complexity: O(n)
# Topic: Arrays, Sets
# Difficulty:Easy
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            return True