def transform(num,k):
    if num<k:
        return num
    else:
        return str(num%k)+str(transform(num//k,k))
print(int((transform(233,7)[::-1])))