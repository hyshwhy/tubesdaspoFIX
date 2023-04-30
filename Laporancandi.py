import Database
import Misc

def HitungCandi():
    count = 0
    for i in range(Misc.lengthList(Database.daftar_candi)):
        if Database.daftar_candi[i] != [0, "", 0, 0, 0]:
            count += 1
    return count

def HitungBahanCandi(bahan):
    if bahan == "pasir": idx = 2
    elif bahan == "batu": idx = 3
    elif bahan == "air": idx = 4
    else: return("Bahan invalid.")

    count = 0
    for i in range(Misc.lengthList(Database.daftar_candi)):
        if Database.daftar_candi[i] != [0, "", 0, 0, 0]:
            count += int(Database.daftar_candi[i][idx])
    return count

def CandiTermahal():
    hargaMaks = 0
    idCandiTermahal = -1
    for i in range(Misc.lengthList(Database.daftar_candi)):
        if Database.daftar_candi[i] != [0, "", 0, 0, 0]:
            rumusHarga = int(Database.daftar_candi[i][2]) * 10000 + int(Database.daftar_candi[i][3]) * 15000 + int(Database.daftar_candi[i][4]) * 7500
            if hargaMaks < rumusHarga:
                hargaMaks = rumusHarga
                idCandiTermahal = int(Database.daftar_candi[i][0])

    if idCandiTermahal == -1:
        return "-"
    else:
        formatHarga = format(hargaMaks, ',').replace(',', '.')
        return f"{idCandiTermahal} (Rp {formatHarga})"
    
def CandiTermurah():
    hargaMin = None
    idCandiTermurah = -1
    for i in range(Misc.lengthList(Database.daftar_candi)):
        if Database.daftar_candi[i] != [0, "", 0, 0, 0]:
            rumusHarga = int(Database.daftar_candi[i][2]) * 10000 + int(Database.daftar_candi[i][3]) * 15000 + int(Database.daftar_candi[i][4]) * 7500
            if hargaMin == None:
                hargaMin = rumusHarga
                idCandiTermurah = int(Database.daftar_candi[i][0])
            elif hargaMin > rumusHarga:
                hargaMin = rumusHarga
                idCandiTermurah = int(Database.daftar_candi[i][0])

    if idCandiTermurah == -1:
        return "-"
    else:
        formatHarga = format(hargaMin, ',').replace(',', '.')
        return f"{idCandiTermurah} (Rp {formatHarga})"
    
def laporancandi():
    if Database.access != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        print("Total Candi:", HitungCandi())
        print("Total Pasir yang digunakan:", HitungBahanCandi("pasir"))
        print("Total Batu yang digunakan:", HitungBahanCandi("batu"))
        print("Total Air yang digunakan:", HitungBahanCandi("air"))
        print("ID Candi Termahal:", CandiTermahal())
        print("ID Candi Termurah:", CandiTermurah())