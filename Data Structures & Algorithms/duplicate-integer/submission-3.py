import numpy as np
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = np.array(nums)
        unique_array = np.unique(array)
        if len(unique_array) < len(array):
            return True
        else:
            return False


        