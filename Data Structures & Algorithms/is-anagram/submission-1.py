class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            # create a dictionary with letter as key, value as #
            s_counts = {}
            n_counts = {}
            for i in s:
                 s_counts[i] = s_counts.get(i,0)+1
            for i in t:
                n_counts[i] = n_counts.get(i,0)+1
            if n_counts == s_counts:
                return True
            else:
                return False
        else:
            return False
        