import Database
import Misc
import Laporancandi

def ayamberkokok ():
    if Database.access != "roro_jonggrang":
        print("Hanya Roro Jonggrang yang memiliki akses")
    else:
        print("Kukuruyuk.. Kukuruyuk..")
        totalCandi = Laporancandi.HitungCandi()
        print(f'\nJumlah Candi:  {totalCandi}')
        print()
        if totalCandi == 100:
            print("Yah, Bandung Bondowoso memenangkan permainan!")            
        else:
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print()
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
    exit()