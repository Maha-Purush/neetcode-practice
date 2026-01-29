#Problem: How many numbers are smaller than the current number
#Difficulty: Easy
#Time Complexity: O(n)
# Used nested loops and enumerate [approach 1] || dictionaries [approach 2]


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #Approach 1
        #ans = []
        
        #for i,num in enumerate(nums):
            #count = 0
            #for j,jnum in enumerate(nums):
                #if jnum<num:
                    #count = count + 1
            
            #ans.append(count)
        #return ans
##################################################

      #Approach 2
        temp = sorted(nums)
        dic = {}
        for i, num in enumerate(temp):
            if num not in dic:
                dic[num] = i
            
        ans = []
        for i in nums:
            ans.append(dic[i])

        return ans
  