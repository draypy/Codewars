"""
https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
"""
def max_sequence(arr):
    result = []
    count = 0
    for elem in arr:
        count += elem
        if count < 0:
            count = 0
            continue
        result.append(count)
    return max(result) if result else 0

