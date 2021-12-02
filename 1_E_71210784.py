x = int(input("Masukan awal deret : "))
y = int(input("Masukan ahkir deret : "))
for i in range(x,y):
    if(i%2==0) and (i%5 != 0) and (i%9 != 0): 
        print(i, end= "")