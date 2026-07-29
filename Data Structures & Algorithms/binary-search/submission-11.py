class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        hashmap = {}
        for i in range(len(nums)):
            hashmap[i] = nums[i]
        print(hashmap)
        reverse_map = {value:key for key, value in enumerate(nums)}
        
        return reverse_map[target]
        