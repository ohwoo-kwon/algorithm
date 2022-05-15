def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while len(bridge):
        answer += 1
        weight += bridge.pop(0)
        if truck_weights:
            if truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                weight -= truck
            else:
                bridge.append(0)
    return answer