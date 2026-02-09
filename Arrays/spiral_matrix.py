#Difficulty : Medium
#Time Complexity: O(m*n) where m is number of rows and n is number of columns


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        while matrix:

            ret += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop()) 

            if matrix and matrix[0]:
                    ret.extend(matrix.pop()[::-1])

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret