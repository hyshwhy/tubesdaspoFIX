import Database
import random

def kumpul():
    pasir=0
    batu=0
    air=0
    if Database.access!="jin_pengumpul":
        print("Hanya jin pengumpul yang memiliki akses")
    else:
        pasir=random.randint(1,5)
        batu=random.randint(1,5)
        air=random.randint(1,5)

        pasir_saat_ini = int(Database.bahan_bangunan[0][2])       
        batu_saat_ini = int(Database.bahan_bangunan[1][2])
        air_saat_ini = int(Database.bahan_bangunan[2][2])

        Database.bahan_bangunan[0][2] = pasir_saat_ini + pasir
        Database.bahan_bangunan[1][2] = batu_saat_ini + batu
        Database.bahan_bangunan[2][2] = air_saat_ini + air

        print("Jin menemukan",pasir,"pasir,",batu,"batu,","dan",air,"air")
