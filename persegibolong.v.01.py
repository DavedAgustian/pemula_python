#!C:\Python34\python.exe
#----------------- Program Persegi 4 Bolong ----------------

y = int(input('masukan sebuah angka : '))
a =''
b =''
x =' ' * (y - 2)
z = y - 1

for j in range(1,y+1):
     a = a + str(j)
print (a)
for i in range(2,y):
     print (str(i) + x + str(z))
     z-=1
for k in range(y,0,-1):
     b = b +str(k)
print (b)
