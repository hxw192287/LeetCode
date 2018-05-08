# Description

# Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays
# (each array picks one) and calculate the distance. We define the difference between two integers a and b 
# to be their absolute difference |a-b|. Your task is to find the maximum difference.

# Note: Each given array will have at least 1 number. There will be at least two non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].

# Example
# Given arrays = [[1,2,3], [4,5], [1,2,3]]
# Return 4
# One way to reach the maximum difference 4 is to pick 1 in the first or third array and pick 5 in the second array.

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result, min_val, max_val = 0,  arrays[0][0], arrays[0][-1]
        for i in xrange(1, len(arrays)):
            result = max(result, \
                         max(max_val - arrays[i][0], \
                             arrays[i][-1] - min_val))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return result
 
