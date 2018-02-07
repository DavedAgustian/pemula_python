#!C:\Python34\python.exe
#----------------- Program Segitiga Bolong ----------------

x = int(input('Masukan sebuah angka : '))
print ((x) * ' ' + '*')
y = 0
for z in range (x-1,1,-1):
     y += 1
     print ((z * ' ') + '*' + (2*y-1) * ' ' + '*')

print (' ' + ' '.join('*' * x))
