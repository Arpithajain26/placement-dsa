def remove_the_last_set_bit(n):
    bi=list(bin(n)[2:])
    for i in range(len(bi)-1,-1,-1):
        if bi[i]=='1':
            bi[i]='0'
            break
    return int("".join(bi))
print(remove_the_last_set_bit(12))