import Database
import Misc

def hancurkancandi():
    if Database.access != "roro_jonggrang":
        print("Hanya Roro Jonggrang yang memiliki akses")
    else:
        id = input("Masukkan ID candi: ")

        found = False
        idx = -1
        for i in range(Misc.lengthList(Database.daftar_candi)):
            if id == Database.daftar_candi[i][0]:
                idx = i
                found = True

        if not(found):
            print("Tidak ada candi dengan ID tersebut.")
        else:
            konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ").upper()

            if konfirmasi == "N":
                print("Candi tidak jadi dihancurkan.")
            elif konfirmasi == "Y":
                Database.daftar_candi[idx] = [0, "", 0, 0, 0]
                print("Candi telah berhasil dihancurkan.")