# Assume you have an array of length n initialized with all 0's and are given k update operations.

# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of 
# subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

# Return the modified array after all k operations were executed.

# Example :
# Given:

#   length = 5,
#   updates = [
#       [1,  3,  2],
#       [2,  4,  3],
#       [0,  2, -2]
#   ]
#
# Output:
#
#   [-2, 0, 3, 5, 3]

# Explanation:

# Initial state:
# [ 0, 0, 0, 0, 0 ]

# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]

# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]

# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]

# Time:  O(k + n)
# Space: O(1)

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * length
        for update in updates:
            result[update[0]] += update[2]
            if update[1]+1 < length:
                result[update[1]+1] -= update[2]

        for i in xrange(1, length):
            result[i] += result[i-1]

        return result
