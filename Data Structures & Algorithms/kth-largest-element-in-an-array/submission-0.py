class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = [-num for num in nums]
        heapq.heapify(m)
        while(k>=2):
            -heapq.heappop(m)
            k-=1
        return -heapq.heappop(m)