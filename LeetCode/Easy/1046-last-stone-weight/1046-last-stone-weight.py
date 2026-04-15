import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heap.append(-i)
    
        heapq.heapify(heap)
    
        while len(heap) > 1:
            y = - heapq.heappop(heap)
            x = - heapq.heappop(heap)
        
            if x != y:
                z = y - x
                heapq.heappush(heap, -z)
            print(heap)
    
        if heap:
            return -heap[0]
        else: 
            return 0