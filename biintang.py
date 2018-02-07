tinggi = int (input('masukan tinggi :'))

for x in range (1,tinggi+1):
    print ((tinggi-x)* ' ' + '#'*x + (tinggi-x)*' ')
