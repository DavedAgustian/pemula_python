#!C:\Python34\python.exe
#------------List & Tuple -------------

old_list = []
n = int(input("Elemen list:"))
for i in range (1,n+1):
    old_list.append(i)

print(old_list)


while True:
    m = int(input("Element list:"))
    c = 0
    for j in range (1,m+1):
        if c < len(old_list):
            old_list[c] = old_list[c] + j
        else:
            old_list.append(j)
        c = c + 1
    print (old_list)


