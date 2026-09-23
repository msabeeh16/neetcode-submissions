class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        s_counts = {}
        t_counts = {}

        for letter in s:
            s_counts[letter] = s_counts.get(letter, 0) + 1
        
        for letter in t:
            t_counts[letter] = t_counts.get(letter, 0) + 1

        sorted_s = dict(sorted(s_counts.items()))
        sorted_t = dict(sorted(t_counts.items()))

        if sorted_s == sorted_t:
            return True
        else:
            return False