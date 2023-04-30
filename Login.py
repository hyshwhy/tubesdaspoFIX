import Database


def login():
  
  if Database.access != "": # sudah pernah login
    print("Login gagal!")
    print("Anda telah login dengan username" + Database.user + ", silahkan lakukan “logout” sebelum melakukan login kembali.")
  else: # belum login
    while Database.access == "":
      # Cek apakah user_name terdaftar dan password benar
      user_name = input("Username: ")
      password = input("Password: ")
      cek_username = False
      cek_password = False
      for i in range(102):
        if Database.daftar_akun[i][0] == user_name:
          cek_username = True
          if Database.daftar_akun[i][1] == password: 
            cek_password = True
            index = i
          else:
            cek_password = False
            
      if cek_username == True:
        if cek_password == True: # user_name terdaftar dan password benar
          print("Selamat datang, " + user_name + "!")
          print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
          Database.user = user_name
          Database.access = Database.daftar_akun[index][2]
        else: # user_name terdaftar tapi password salah
          print("Password salah!")
      else: 
        print("Username tidak terdaftar!")
