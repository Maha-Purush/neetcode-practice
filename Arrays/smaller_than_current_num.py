#Problem: How many numbers are smaller than the current number
#Difficulty: Easy
#Time Complexity: O(n)
# Used nested loops and enumerate

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for i,num in enumerate(nums):
            count = 0
            for j,jnum in enumerate(nums):
                if jnum<num:
                    count = count + 1
            
            ans.append(count)
        return ans
