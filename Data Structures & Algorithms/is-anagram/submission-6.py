class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = list(t)
        s_list = list(s)
        if sorted(t_list) == sorted(s_list):
            return True
        else:
            return False