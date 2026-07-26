def max_subarray(arr):
    maxnum=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            maxnum=max(maxnum,sum)
    return maxnum
print(max_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))





