#Problem: Two Sum (i've made it)
#Difficulty: Easy
#Time Complexity: O(n)
# Used hash map (dictionaries)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if (target-num) not in dic:
                dic[num]=i
            else:
                return [i, dic.get(target-num)]