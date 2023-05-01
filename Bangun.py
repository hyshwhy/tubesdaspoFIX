import Database
import random
import Misc

def bangun():
    pasir=0
    batu=0
    air=0
    if Database.access!="jin_pembangun":
        print("Hanya jin pembangun yang memiliki akses")
    else:
        pasir=random.randint(1,5)
        batu=random.randint(1,5)
        air=random.randint(1,5)

        if pasir <= int(Database.bahan_bangunan[0][2]) and batu <= int(Database.bahan_bangunan[1][2]) and air <= int(Database.bahan_bangunan[2][2]):

            pasir_saat_ini = int(Database.bahan_bangunan[0][2])
            batu_saat_ini = int(Database.bahan_bangunan[1][2])
            air_saat_ini = int(Database.bahan_bangunan[2][2])

            Database.bahan_bangunan[0][2] = pasir_saat_ini - pasir
            Database.bahan_bangunan[1][2] = batu_saat_ini - batu
            Database.bahan_bangunan[2][2] = air_saat_ini - air

            if Misc.MinIdCandi == None:
                print("", end="")
            else:
                Database.daftar_candi[Misc.MinIdCandi()] = [Misc.MinIdCandi(), Database.user, pasir, batu, air]
            
            print(f"Sisa candi yang perlu dibangun: {Misc.HitungSisaCandi()}.")
        else:
            print("Bahan bangunan tidak cukup")

