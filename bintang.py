#!C:\Python34\python.exe

tinggi = int (input('masukan tinggi :'))

for x in range (1,tinggi+1):
    print ((tinggi-x)* ' ' + " ".join(['#']*x))
