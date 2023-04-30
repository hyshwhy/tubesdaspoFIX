def init():
    global access, user, daftar_akun, daftar_candi, bahan_bangunan, id_candi
    access = ""
    user = ""
    daftar_akun = [['' for i in range(3)] for i in range (102)]
    daftar_candi = [[0, "", 0, 0, 0] for i in range(100)]
    bahan_bangunan = [["Pasir","deskripsi pasir",0],["Batu","deskripsi Batu",0],["Air","deskripsi Air",0]]
    id_candi = [i for i in range(100)]