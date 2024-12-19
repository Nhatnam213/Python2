
def tim_kim(arry,x):
    l = 0
    r = len(arry)-1
    mid = 0
    while l <= r:
        mid =(l+r)//2
        if arry[mid] < x:
            l = mid +1
        elif arry[mid]>x:
            r = mid -1
        else:
          return mid
        return -1
arry = [2,4,7,9,10]
x = 8
res = tim_kim(arry,x)
if res == -1:
    print("Gia tri",x,"Khong duoc tim thay")
else:
    print("Gia tri",x,'Duoc tiem thay',str(res))

