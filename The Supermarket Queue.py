from typing import List

def queue_time(customers: List[int], n: int) -> int:
    lanes = [0] * n  # Represents the time remaining for each lane
    for customer in customers:
        min_lane = lanes.index(min(lanes))  # Find the lane with the shortest queue
        lanes[min_lane] += customer  # Add the customer's time to the lane

    return max(lanes)  # Return the longest queue time

# Example usage
customers = [2, 3, 10]
n = 2
total_time = queue_time(customers, n)
print(total_time)  # Output: 12
