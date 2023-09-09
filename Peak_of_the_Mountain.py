from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    alen = len(arr)
    left, right = 0, alen - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if mid == alen - 1 or arr[mid] > arr[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
