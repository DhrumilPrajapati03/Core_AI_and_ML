from typing import List

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    bucket = [[] for i in range(len(nums)+1)]
    frequencymap = {}

    # Fill Frequenymap
    for n in nums:
        if n not in frequencymap:
            frequencymap[n] = 1
        else:
            frequencymap[n] +=1

    # Fill bucket
    for key, frequency in frequencymap.items():
        bucket[frequency].append(key)

    result = []

    for i in reversed(range(len(bucket))):
        if bucket[i]:
            for value in bucket[i]:
                if len(result) <k:
                    result.append(value)
                else:
                    return result
    return result