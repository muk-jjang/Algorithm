import sys
import heapq



N = int(sys.stdin.readline())
heap = []

for i in range(N):
    cal = int(sys.stdin.readline())

    if cal > 0:
        heapq.heappush(heap, -cal)
    elif cal == 0:
        if len(heap) ==0:
            print(0)
        else: print(-(heapq.heappop(heap)))
    
        