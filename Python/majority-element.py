# Time:  O(n)
# Space: O(1)
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [n/2] times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
import collections


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1
        
        for i in xrange(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1
        
        return nums[idx]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key=lambda a: a[1], reverse=True)[0][0]
    
    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1 :
            return nums[0]
        if n%2 :
            find = set(nums[0:(n//2)+1]) & set(nums[n//2:]) #intersection 
        else:
            find = set(nums[0:n//2]) & set(nums[n//2:])
        
        for i in find:
            if nums.count(i)>n//2:
                return i

if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
