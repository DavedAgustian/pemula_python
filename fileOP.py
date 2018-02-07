while True:
    print ("""
1. Login
2. Register
3. View User
""")
    pilih = (int(input("Pilih opsi [1,2,3]:")))

    if pilih == 2:
        usr = input("username : ")
        passwd = input("password : ")
        try:
            nama = open("registerinfo.txt", "a")
            nama.write(usr + "\n")
            nama.close()
            kunci = open("password.txt", "a")
            kunci.write(passwd + "\n")
            kunci.close()
        except IOError:
            nama = open ("registerinfo.txt", "w")
            nama.write(usr + "\n")
            nama.close()
            kunci = open("password.txt", "w")
            kunci.write(passwd + "\n")
            kunci.close()
    elif pilih == 1 :
        usr = input("username : ")
        passwd = input("password : ")
        try:
            nama = open("registerinfo.txt").readlines()
            kunci = open ("password.txt").readlines()
            if nama.index(usr + "\n") == kunci.index(passwd+ "\n"):
                print ("welcome", usr)
            else:
                print ("User belum terdaftar, silahkan register")
        except IOError:
            print ("Belum ada User")
    elif pilih == 3:
        tambah = 0
        nama = open("registerinfo.txt").readlines()
        kunci = open ("password.txt").readlines()
        for x in nama:
            print("[{ username:", x, "Password : ", kunci[tambah],"}]")
        tambah = tambah + 1
