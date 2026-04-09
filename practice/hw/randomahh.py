def calculate_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

print(calculate_sum([2, 4, 6, 8]))