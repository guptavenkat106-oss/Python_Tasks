def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print("Sum of list:", list_sum(numbers))
