import Database


def help():
    if Database.access=="":
        print("=========== HELP ===========")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print('2. exit')
        print('   untuk mengakhiri permainan')
        
    elif Database.access=="bandung_bondowoso":
        print('=========== HELP ===========')
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print('2. summonjin')
        print('   Untuk memanggil jin')
        print('3. hapusjin')
        print('   Untuk menghapus jin dan menghancurkan candi yang sudah dia bangun')
        print('4. ubahjin')
        print('   Untuk mengubah tipe jin')
        print('5. batchkumpul')
        print('   Untuk memerintah semua jin pengumpul untuk mengumpulkan bahan')
        print('6. batchbangun')
        print('   Untuk memerintah semua jin pembangun untuk membangun candoi')
        print('7. laporanjin')
        print('   Untuk mengambil laporan kinerja jin')
        print('8. laporancandi')
        print('   Untuk mengambil laporan candi')
        print('9. save')
        print('   untuk menyimpan progres permainan')
        print('10.exit')
        print('   untuk mengakhiri permainan')
  
  
    elif Database.access=="roro_jonggrang":
        print('=========== HELP ===========')
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print('2. hancurkancandi')
        print('   Untuk menghancurkan candi yang tersedia')
        print('3. ayamberkokok')
        print('   Untuk mengakhiri permainan')
        print('4. save')
        print('   untuk menyimpan progres permainan')
        print('5. exit')
        print('   untuk mengakhiri permainan')
       
    elif Database.access=="jin_pembangun":
        print('=========== HELP ===========')
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print('2. bangun')
        print('   untuk membangun candi')
        print('3. exit')
        print('   untuk mengakhiri permainan')
     
    
    elif Database.access=="jin_pengumpul":
        print('=========== HELP ===========')
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print('2. kumpul')
        print('   untuk mengumpulkan resource candi')
        print('3. exit')
        print('   untuk mengakhiri permainan')
        

        
      
      






        



