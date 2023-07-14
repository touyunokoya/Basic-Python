a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
aa=int(a)
bb=int(b)
count =2
if aa==1:
          print("1は素数ではありません。")
while count<=aa:       
     if count ==aa:
          print("{}は素数です。".format(aa))
          break
     elif aa%count==0:
          print("{}は素数ではありません。".format(aa))
          break
     count+=1
if bb==1:
          print("1は素数ではありません。")
count=2
while count<=bb:
     if count ==bb:
          print("{}は素数です。".format(bb))
          break
     elif bb%count==0:
          print("{}は素数ではありません。".format(bb))
          break
     count+=1
