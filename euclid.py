a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

aa=int(a)
bb=int(b)
firsta =aa
firstb =bb
if bb>aa:
    bb = firsta
    aa = firstb
while True:
    q=aa//bb
    r=aa-bb*q
    if r==0:
        print('{}と{}の最大公約数は{}です。'.format(firsta,firstb,bb))
        break
    aa=bb
    bb=r 
