import argparse, os
import Database
import Misc

def CSV_Parser():
    Database.init()

    fu = open(str(args.nama_folder) + "\\user.csv", 'r')
    baris = 0
    fake = fu.readline()

    while True:
        lineU = fu.readline()
        kolomU = 0
        temp = ''
        for i in range (Misc.lengthString(lineU)):
            if lineU[i]==";" or lineU[i]=="\n":
                Database.daftar_akun[baris][kolomU] = temp
                temp = ''
                kolomU = (kolomU + 1) % 3
            else:
                temp += lineU[i]
            
        baris += 1
        
        if not lineU:
            break
    fu.close
    
    fc = open(str(args.nama_folder) + "\\candi.csv", 'r')
    baris = 0
    fake = fc.readline()

    while True:
        lineC = fc.readline()
        kolomC = 0
        temp = ''
        for i in range (Misc.lengthString(lineC)):
            if lineC[i]==";" or lineC[i]=="\n":
                Database.daftar_candi[baris][kolomC] = temp
                temp = ''
                kolomC = (kolomC + 1) % 5
            else:
                temp += lineC[i]
            
        baris += 1
        
        if not lineC:
            break
    fc.close
    
    fb = open(str(args.nama_folder) + "\\bahan_bangunan.csv", 'r')
    baris = 0
    fake = fb.readline()

    while True:
        lineB = fb.readline()
        kolomB = 0
        temp = ''
        for i in range (Misc.lengthString(lineB)):
            if lineB[i]==";" or lineB[i]=="\n":
                Database.bahan_bangunan[baris][kolomB] = temp
                temp = ''
                kolomB = (kolomB + 1) % 3
            else:
                temp += lineB[i]
            
        baris += 1
        
        if not lineB:
            break
    fb.close
    
    
    


def load():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder")
    args = parser.parse_args()

    if args.nama_folder == '':
        print("Tidak ada nama folder yang diberikan!")
        print("\nUsage: python -u main.py <nama_folder>")
    if os.path.exists(args.nama_folder):
        print("\nLoading...\n")
        print("Selamat datang di program \"Manajerial Candi\"")

        CSV_Parser()
    else:
        print(f"Folder \"{args.nama_folder}\" tidak ditemukan")
