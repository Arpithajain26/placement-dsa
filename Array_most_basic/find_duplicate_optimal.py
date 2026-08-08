def find_duplicate_optimal(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)
    return
print(find_duplicate_optimal([1,2,3,4,5,3]))