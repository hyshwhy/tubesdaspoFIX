import os
import Misc, Database

def Tulis_file(nama_file, arr, alamat):
    alamat = os.path.join(alamat, nama_file)
    f = open(alamat, 'w')

    if nama_file == "user.csv": 
        baris_eff, kolom = Misc.HitungBaris_daftar_akun(), 3
        f.write("username;password;role\n")
    elif nama_file == "candi.csv": 
        baris_eff, kolom = Misc.HitungBaris_daftar_candi(), 5
        f.write("id;pembuat;pasir;batu;air\n")
    elif nama_file == "bahan_bangunan.csv": 
        baris_eff, kolom = 3, 3
        f.write("nama;deskripsi;jumlah\n")

    if baris_eff == 0:
        f.close()
    else:
        for i in range(baris_eff):

            if arr[i][0] != '':
                temp = ''
                for j in range(kolom-1):
                    temp += str(arr[i][j]) + ';'
                
                temp += str(arr[i][kolom-1]) + '\n'
                f.write(temp)
            
            

def buat_dir(dir_atas, dir_saat_ini, dir_bawah):
    if dir_bawah == dir_saat_ini:
        if os.path.exists(os.path.join(dir_atas, dir_saat_ini)):
            print("", end="")
        else:
            print(f'\nMembuat folder {dir_saat_ini}...')
            os.mkdir(os.path.join(dir_atas, dir_saat_ini))
        print(f"\nBerhasil menyimpan data di folder {dir_saat_ini}!")
    else:
        if os.path.exists(os.path.join(dir_atas, dir_saat_ini)):
            print("", end="")
        else:
            print(f'Membuat folder {dir_saat_ini}...')
            os.mkdir(os.path.join(dir_atas, dir_saat_ini))

        bawahan = len(dir_saat_ini)
        
        for i in range(bawahan, len(dir_bawah)):
            dir_saat_ini += dir_bawah[i]
            if dir_bawah[i] == '/':
                break
        buat_dir(dir_atas, dir_saat_ini, dir_bawah)
        

def save():
    dir_bawah = input('Masukkan nama folder: ')
    dir_atas = os.path.dirname(os.path.realpath(__file__))

    dir_saat_ini = ''
    for i in range(len(dir_bawah)):
        dir_saat_ini = dir_saat_ini + dir_bawah[i]
        if dir_bawah[i] == '/':
            break
    print("\nSaving...")
    buat_dir(dir_atas, dir_saat_ini, dir_bawah)


    alamat_akhir = os.path.join(dir_atas, dir_bawah)

    Tulis_file('user.csv', Database.daftar_akun, alamat_akhir)
    Tulis_file('candi.csv', Database.daftar_candi, alamat_akhir)
    Tulis_file('bahan_bangunan.csv', Database.bahan_bangunan, alamat_akhir)
