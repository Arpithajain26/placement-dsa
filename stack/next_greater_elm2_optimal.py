def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []

    for i in range(2 * len(nums) - 1, -1, -1):

        current = nums[i % len(nums)]

        while stack and stack[-1] <= current:
            stack.pop()

        if i < len(nums) and stack:
            ans[i] = stack[-1]

        stack.append(current)

    return ans

print(next_greater([2, 10, 12, 1, 11]))