from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    time = 0
    tmp = 0    # 다리 위 트럭 무게
    
    while bridge:
        time += 1     # 트럭을 옆으로 하나씩 넣을 때마다 +1
        tmp -= bridge[0]
        bridge.popleft()
        
        if truck_weights:
            if (tmp + truck_weights[0]) <= weight:
                tmp += truck_weights[0]
                bridge.append(truck_weights.popleft())

            else:
                bridge.append(0) # 옆에 0으로 채워주면, 트럭이 왼쪽으로 밀려남
  
    return time
