def check_ith_bit(n,i):
    if (n & i<<1)!=0:
        return True
    else:
        return False
print(check_ith_bit(12,2))