from typing import List
def twosum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[nums[i]] = i

print(twosum([2,3,4,5,6,1], 9))