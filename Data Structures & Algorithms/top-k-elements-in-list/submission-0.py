class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aMap = {}

        for num in nums:
            count = aMap.get(num, 0)
            aMap[num] = count + 1
        
        items = aMap.items()

        sorted_items = sorted(items, key=lambda pair: pair[1], reverse=True)

        result = []

        for pair in sorted_items[:k]:
            result.append(pair[0])

        return result