class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            hashmap[n] = i
        print(f"hashmap: {hashmap}")
        for i, n in enumerate(nums):
            diff = target-n
            if diff in hashmap and hashmap[diff] !=i:
                return [i, hashmap[diff]]