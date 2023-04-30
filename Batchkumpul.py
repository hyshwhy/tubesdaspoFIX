import Database
import Misc
import random

def batchkumpul():
    if Database.access!="bandung_bondowoso":
        print("Hanya Bandung Bondowoso yang memiliki akses")
    else:
        count = 0
        totalPasir = 0
        totalBatu = 0
        totalAir = 0
        for i in range (Misc.lengthList(Database.daftar_akun)):
            if Database.daftar_akun[i][2]=="jin_pengumpul":
                count = count + 1
        for i in range(count):
            pasir=random.randint(1,5)
            batu=random.randint(1,5)
            air=random.randint(1,5)
            totalPasir += pasir
            totalBatu += batu
            totalAir += air

        pasir_saat_ini = int(Database.bahan_bangunan[0][2])       
        batu_saat_ini = int(Database.bahan_bangunan[1][2])
        air_saat_ini = int(Database.bahan_bangunan[2][2])

        Database.bahan_bangunan[0][2] = pasir_saat_ini + totalPasir
        Database.bahan_bangunan[1][2] = batu_saat_ini + totalBatu
        Database.bahan_bangunan[2][2] = air_saat_ini + totalAir

        print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {totalPasir} pasir, {totalBatu} batu, dan {totalAir} air.")