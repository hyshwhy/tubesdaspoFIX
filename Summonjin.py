
import Database


def appendGlobalUser(elmt,arr):
    for i in range(lengthList(arr)):
        if arr[i] == ['' for i in range(lengthList(arr[0]))]:
            arr[i]=elmt
            break

def cekJinMaks():
    found = False
    for i in range(lengthList(Database.daftar_akun)):
        if Database.daftar_akun[i] == ['' for i in range(3)]:
            found = True
            break
    return found


def lengthString(str):
    arr = list(str)
    mark = "$$"
    arr = arr + [mark]
    count = 0
    i = 0
    while arr[i] != "$$":
        count += 1
        i += 1
    return count

def lengthList(arr):
    mark = "$$"
    arr = arr + [mark]
    count = 0
    i = 0
    while arr[i] != "$$":
        count += 1
        i += 1
    return count


def summonjin():
    if Database.access!="bandung_bondowoso":
        print("Hanya Bandung yang memiliki akses")
    else:
        if cekJinMaks():
            print("Jenis jin yang dapat dipanggil:")
            print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print(" (2) Pembangun - Bertugas membangun candi")
            print("")

            pilihanRole = 0
            role = ""
            username = ""
            password = ""


            while pilihanRole < 1 or pilihanRole > 2:
                print()
                pilihanRole = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
                
                if pilihanRole == 1:
                    role = "jin_pengumpul"
                    print(pilihanRole)

                elif pilihanRole == 2:
                    role = "jin_pembangun"
                else:
                    print()
                    print(f"Tidak ada jenis jin bernomor “{pilihanRole}”!")
            
            print(f"Memilih jin “{role}”.")

            while username == "":
                found = False
                tempUsername = input("Masukkan username jin: ")

                for i in range(lengthList(Database.daftar_akun)):
                    if tempUsername == Database.daftar_akun[i][0]:
                        found = True
                
                if found == True: #sama yang di database
                    print(f"Username “{tempUsername}” sudah diambil!")
                else:
                    username = tempUsername

            while password == "":
                tempPass = input("Masukkan password jin: ")
                
                if lengthString(tempPass) < 5 or lengthString(tempPass) > 25: #sama yang di database
                    print("Password panjangnya harus 5-25 karakter")
                else:
                    password = tempPass

            userJin = [username, password, role]

            appendGlobalUser(userJin,Database.daftar_akun)

            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print()
            print(f"Jin {username} berhasil dipanggil!")
        else: print("Jumlah jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
