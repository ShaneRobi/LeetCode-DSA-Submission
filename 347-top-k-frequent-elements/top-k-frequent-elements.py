class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # 1. Count how many times each number appears
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # 2. Create buckets
        # index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # 3. Scan from highest frequency to lowest
        result = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result