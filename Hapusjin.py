import Database
import Misc

def hapusjin():
    if Database.access!="bandung_bondowoso":
        print("Hanya Bandung yang memiliki akses")
    else:
        username = ""
        found = False

        while username == "":
            tempUsername = input("Masukkan username jin :")

            for i in range(Misc.lengthList(Database.daftar_akun)):
                if tempUsername == Database.daftar_akun[i][0]:
                    found = True
                    Database.daftar_akun[i] = ["", "", ""]
                    for i in range(Misc.lengthList(Database.daftar_candi)):
                        if Database.daftar_candi[i][1] == tempUsername:
                            Database.daftar_candi[i] = [0, "", 0, 0, 0]
                    break
            
            if found == False:
                print("Tidak ada jin dengan username tersebut.")
            else:
                username = tempUsername
                print("Jin telah berhasil dihapus dari alam gaib.")