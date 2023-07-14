a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
aa=int(a)
bb=int(b)

def prime_number(x):
     count =2
     if x==1:
          return False
     while count<=x:
          if count ==x:
               return True

          if x%count==0:
               return False
          count+=1

if prime_number(aa)==1:
     print("{}は素数です。".format(aa))
else:
     print("{}は素数ではありません。".format(aa))
if prime_number(bb)==1:
     print("{}は素数です。".format(bb))
else:
     print("{}は素数ではありません。".format(bb))
