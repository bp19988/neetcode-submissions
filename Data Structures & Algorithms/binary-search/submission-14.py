class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l=m+1
            else:
                return m
        return -1

    #     if target not in nums:
    #         return -1
    #     hashmap = {}
    #     for i in range(len(nums)):
    #         hashmap[i] = nums[i]
    #     print(hashmap)
    #     reverse_map = {value:key for key, value in enumerate(nums)}
        
    #     return reverse_map[target]
        