# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

def get_lowest_number(num):
    start, end = 0, len(num) - 1
    while start <= end:
        mid_point = (start + end) // 2
        # Check if mid_point is the minimum
        if mid_point > 0 and num[mid_point] < num[mid_point - 1]:
            return mid_point

        # If mid_point element is greater than the end element,
        # the minimum must be in the right half
        if num[mid_point] > num[end]:
            start = mid_point + 1
        else:  # Minimum is in the left half
            end = mid_point
        return start


result = get_lowest_number([5, 6, 9, 0, 2, 3, 4])
print(result)  # Output: 3
