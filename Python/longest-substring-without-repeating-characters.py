# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.
#

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        MaxLength = 0
        TempString = ""
        for i in s:
            if i not in TempString:
                TempString += i
                if len(TempString) > MaxLength:
                    MaxLength = len(TempString)
            else:
                TempString = TempString[TempString.index(i)+1:] + i
        return MaxLength

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")
