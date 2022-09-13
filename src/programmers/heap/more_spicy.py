import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) != 1:
        v = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, v)
        answer += 1
             
    return -1 if scoville[0] < K else answer
