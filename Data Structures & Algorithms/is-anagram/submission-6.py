class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_A = {}

        for i in range(len(s)):
            dict_A[s[i]] = 1 + dict_A.get(s[i], 0)
            dict_A[t[i]] = -1 + dict_A.get(t[i], 0)  
        return not any(dict_A.values())
        