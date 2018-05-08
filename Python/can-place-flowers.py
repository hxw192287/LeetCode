# Time:  O(n)
# Space: O(1)

# Suppose you have a long flowerbed in which some of the plots are planted and some are not.
# However, flowers cannot be planted in adjacent plots - they would compete for water
# and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1,
# where 0 means empty and 1 means not empty), and a number n,
# return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in xrange(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and \
                (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False

# Count consecutive zeros
# even -> can put (n // 2 -1) plants
# odd -> can put (n // 2) plants
# Add [1, 0] and [0, 1] to the flowerbed to deal with short array length(<= 2) and
# forces the loop to count the last round of consecutive zeros

  class Solution2(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [1, 0] + flowerbed + [0, 1]
        plants = n
        zeros = 0

        for f in flowerbed:
            if not f:
                zeros += 1
            else:
                if zeros > 2:
                    if zeros % 2 == 0:
                        plants -= (zeros // 2 - 1)
                    else:
                        plants -= (zeros // 2)
                zeros = 0

        return plants <= 0
