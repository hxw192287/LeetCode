# Time:  O(r), r is the range size of the integers
# Space: O(r)

# Given an array of 2n integers, your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4.
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
# 
# Proof:
# Assume in each pair i, bi >= ai.
# Denote Sm = min(a1, b1) + min(a2, b2) + ... + min(an, bn). The biggest Sm is the answer of this problem. Given 1, Sm = a1 + a2 + ... + an.
# Denote Sa = a1 + b1 + a2 + b2 + ... + an + bn. Sa is constant for a given input.
# Denote di = |ai - bi|. Given 1, di = bi - ai. Denote Sd = d1 + d2 + ... + dn.
# So Sa = a1 + a1 + d1 + a2 + a2 + d2 + ... + an + an + dn = 2Sm + Sd => Sm = (Sa - Sd) / 2. To get the max Sm, given Sa is constant, we need to make Sd as small as possible.
# So this problem becomes finding pairs in an array that makes sum of di (distance between ai and bi) as small as possible. Apparently, sum of these distances of adjacent elements is the smallest. If that’s not intuitive enough, see attached picture. Case 1 has the smallest Sd.
# 0_1492961937328_leetcode561.jpg
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LEFT, RIGHT = -10000, 10000
        lookup = [0] * (RIGHT-LEFT+1)
        for num in nums:
            lookup[num-LEFT] += 1
        r, result = 0, 0
        for i in xrange(LEFT, RIGHT+1):
            result += (lookup[i-LEFT] + 1 - r) / 2 * i
            r = (lookup[i-LEFT] + r) % 2
        return result


# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in xrange(0, len(nums), 2):
            result += nums[i]
        return result
    
    
# Time:  O(nlogn)
# Space: O(n)
class Solution3(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum([nums[i] for i in range(0, len(nums), 2)])
 #or
class Solution3_1:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
