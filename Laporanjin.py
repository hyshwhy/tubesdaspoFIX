import Database
import Misc


def Merangking_jin(my_list):
    result = [['', 0] for i in range(Misc.lengthList(my_list))]
    for element in my_list:
        count = 0
        for other_element in my_list:
            if element == other_element and element != '':
                count += 1
        if [element, count] not in result:
            Misc.appendGlobalJin([element, count], result)

    n = Misc.lengthList(result)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if result[j][1] > result[max_idx][1]:
                max_idx = j
        result[i], result[max_idx] = result[max_idx], result[i]
    return result

def laporanjin():
    if Database.access != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        jumlah_jin_pengumpul = Misc.HitungJin("pengumpul")
        jumlah_jin_pembangun = Misc.HitungJin("pembangun")
        jumlah_jin = jumlah_jin_pembangun + jumlah_jin_pengumpul
        print("Total Jin:", jumlah_jin)
        print("Total Jin Pengumpul:", jumlah_jin_pengumpul)
        print("Total Jin Pembangun:", jumlah_jin_pembangun)
        
        jin_terurut = [row[1] for row in Database.daftar_candi]
        panjang_daftar_candi = Misc.lengthList(Database.daftar_candi)


        # mengurut jin yang sudah membangun candi
        for i in range(panjang_daftar_candi):
            max_idx = i
            for j in range(i+1, panjang_daftar_candi):
                if jin_terurut[j].lower() > jin_terurut[max_idx].lower():
                    max_idx = j
            jin_terurut[i], jin_terurut[max_idx] = jin_terurut[max_idx], jin_terurut[i]

        ranking_jin = Merangking_jin(jin_terurut)


        # mengurut semua jin pembangun
        daftar_pembangun = ['' for i in range(Misc.HitungJin("pembangun"))]
        for i in range(Misc.lengthList(Database.daftar_akun)):
            if Database.daftar_akun[i][2] == "pembangun":
                Misc.appendGlobal1D(Database.daftar_akun[i][0], daftar_pembangun)

        for i in range(Misc.lengthList(daftar_pembangun)):
            max_idx = i
            for j in range(i+1, Misc.lengthList(daftar_pembangun)):
                if daftar_pembangun[j].lower() > daftar_pembangun[max_idx].lower():
                    max_idx = j
            daftar_pembangun[i], daftar_pembangun[max_idx] = daftar_pembangun[max_idx], daftar_pembangun[i]

        for element in daftar_pembangun:
            if element not in ranking_jin[0]:
                Misc.appendGlobalJin([element, 0], ranking_jin)
        
        

        if ranking_jin[0][0] == ['', 0]:
            jin_terajin = "-"
        else:
            jin_terajin = ranking_jin[0][0]

        found = False
        for i in range(Misc.lengthList(ranking_jin) -1, -1, -1):
            if ranking_jin[i][0] != '':
                jin_termalas = ranking_jin[i][0]
                found = True
                break
        if found == False: jin_termalas = "-"

        print("Jin Terajin:", jin_terajin)
        print("Jin Termalas:", jin_termalas)

        print("Pasir:", Database.bahan_bangunan[0][2], "unit")
        print("Air:", Database.bahan_bangunan[2][2], "unit")
        print("Batu:", Database.bahan_bangunan[1][2], "unit")