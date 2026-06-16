class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:

            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)
            if a==b:
                continue
            else:
                heapq.heappush(max_heap,-abs(a-b))

        return -max_heap[0] if max_heap else 0