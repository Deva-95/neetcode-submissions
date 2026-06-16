class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]

        for p,v in count.items():
            freq[v].append(p)

        res = []

        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res