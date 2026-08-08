def count_frequency(nums):
    mpp={}
    for num in nums:
        mpp[num]=mpp.get(num,0)+1
    return mpp
print(count_frequency([1,1,3,4,5,5,6,7]))
