import math

# Read number of test cases
T = int(input())

for _ in range(T):
    # Read N (number of people) and X (cost per subscription)
    N, X = map(int, input().split())
    
    # Calculate required number of subscriptions (6 people per subscription)
    subscriptions_needed = math.ceil(N / 6)
    
    # Calculate total cost
    total_cost = subscriptions_needed * X
    
    # Print the result
    print(total_cost)
