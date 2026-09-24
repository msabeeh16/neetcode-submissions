class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        max_len = 0
        left = 0
        for i in range(len(s)):
            letter = s[i]
            if letter not in substring:
                substring += s[i]
                max_len = max(max_len, len(substring))
            else:
                while letter in substring:
                    substring = substring[1:i]
                substring += s[i]
        
        return max_len
