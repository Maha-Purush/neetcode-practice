#Problem: Find all numbers disappeared in an array
#Difficulty: Easy
#Time Complexity: O(n)
#Used 2 approaches , both of O(n) Time Complexity
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Approach 1 : 

        return list(set(range(1, len(nums) + 1 )) - set(nums))

        #Approach 2 : 
        set_nums = set(nums)
        ret = []

        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                ret.append(i)
            
        return ret