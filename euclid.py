a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

aa=int(a)
bb=int(b)
firsta =aa
firstb =bb
def euclid(aa,bb):
    if bb>aa:
        bb = firsta
        aa = firstb
    while True:
        q=aa//bb
        r=aa-bb*q
        if r==0:
            return bb
        aa=bb
        bb=r 
result =euclid(aa,bb)
print("{}".format(result))
def euclid2(aa,bb):
    if euclid(aa,bb)==1:
        return True
    else:
        return False
result =euclid2(aa,bb)
print("{}".format(result))
