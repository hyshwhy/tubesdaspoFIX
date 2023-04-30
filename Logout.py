import Database
def logout():
    if Database.access=="":
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        Database.access=""
        Database.user=""