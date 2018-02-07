nama_hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]
dictionary = {}

while True:
    print("""     
1. Senin
2. Selasa
3. Rabu
4. Kamis
5. Jumat
6. Sabtu
7. Minggu
""")
    pilih = int(input("Pilih hari menggunakan angka [1..7]:"))
    a = nama_hari[pilih-1]
    print ("Anda memilih hari '%s'" %(a))
    b = int(input("Masukkan Data Jumlah Barang :"))
    dictionary[a] = dictionary.get(a,0) + b
    print (dictionary)



