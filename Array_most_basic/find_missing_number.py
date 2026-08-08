def find_missing_number(nums):
    n = 7
    x = n * (n + 1) // 2
    return x - sum(nums)

print(find_missing_number([1,2,3,4,5,7]))