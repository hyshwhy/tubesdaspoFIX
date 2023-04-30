import Database
import Misc
import random

def batchbangun():
    if Database.access!="bandung_bondowoso":
        print("Hanya Bandung Bondowoso yang memiliki akses")
    else:   
        candi_berhasil=Database.daftar_candi
        bahan_berhasil=Database.bahan_bangunan
        count=0
        totalPasir=0
        totalBatu=0
        totalAir=0
        for i in range (Misc.lengthList(Database.daftar_akun)):
            pasir=0
            batu=0
            air=0
            
            
            if Database.daftar_akun[i][2]=="jin_pembangun":
                pasir=random.randint(1,5)
                batu=random.randint(1,5)
                air=random.randint(1,5)
                count = count + 1

                totalPasir+=pasir
                totalBatu+=batu
                totalAir+=air
                # jika candi sudah lebih dari 100
                if Misc.MinIdCandi() == None: continue
                else:
                    candi_berhasil[Misc.MinIdCandi()] = [Misc.MinIdCandi(), Database.daftar_akun[i][0], pasir, batu, air]

        print(f"Mengerahkan {count} jin untuk membangun candi dengan total bahan {totalPasir} pasir, {totalBatu} batu, dan {totalAir} air.")

        if totalPasir <= int(Database.bahan_bangunan[0][2]) and totalBatu <= int(Database.bahan_bangunan[1][2]) and totalAir <= int(Database.bahan_bangunan[2][2]):
            print(f"Jin berhasil membangun total {count} candi")
            Database.daftar_candi=candi_berhasil

            pasir_saat_ini = int(Database.bahan_bangunan[0][2])       
            batu_saat_ini = int(Database.bahan_bangunan[1][2])
            air_saat_ini = int(Database.bahan_bangunan[2][2])

            Database.bahan_bangunan[0][2] = pasir_saat_ini - totalPasir
            Database.bahan_bangunan[1][2] = batu_saat_ini - totalBatu
            Database.bahan_bangunan[2][2] = air_saat_ini - totalAir
        
        else:
            print("Bangun gagal, kurang", end=" ")
            if(totalPasir-Database.bahan_bangunan[0][2] < 0): print("0 pasir", end=", ") 
            else: print(f"{totalPasir-Database.bahan_bangunan[0][2]} pasir", end=", ")
            if(totalBatu-Database.bahan_bangunan[1][2] < 0): print("0 batu", end=", dan ") 
            else: print(f"{totalBatu-Database.bahan_bangunan[1][2]} batu", end=", dan ")
            if(totalAir-Database.bahan_bangunan[2][2] < 0): print("0 air") 
            else: print(f"{totalAir-Database.bahan_bangunan[2][2]} air")

