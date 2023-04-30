import Database
import Misc

def ubahjin():
    if Database.access != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        username = ""
        found = False

        while username == "":
            tempUsername = input("Masukkan username jin :")

            for i in range(Misc.lengthList(Database.daftar_akun)):
                if tempUsername == Database.daftar_akun[i][0]:
                    idx = i
                    found = True
                    break
            
            if found == False:
                print("Tidak ada jin dengan username tersebut.")
                continue
            
            username = tempUsername

            role = Database.daftar_akun[idx][2]
            lawanRole = ""
            if role == "jin_pembangun":
                lawanRole = "jin_pengumpul"
            else:
                lawanRole = "jin_pembangun"

            kalimat = (f"Jin ini bertipe “{role}”. Yakin ingin mengubah ke tipe “{lawanRole}” (Y/N)?")

            konfirmasi = input(kalimat)
            
            if konfirmasi == "Y":
                Database.daftar_akun[idx][2] = lawanRole
                print("Jin telah berhasil diubah")
            elif konfirmasi == "N":
                print("Jin tidak jadi diubah")
            else:
                print("Tidak valid")