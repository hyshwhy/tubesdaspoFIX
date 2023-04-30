import Database
import Misc
import Login, Logout,Summonjin,Hapusjin,Kumpul, Bangun,Batchbangun,Batchkumpul,Help, Save, Exit, Laporancandi, Laporanjin, Hancurkancandi, Ayamberkokok, Ubahjin
def run(perintah):
    if perintah == "login":
        Login.login()
    elif perintah =="logout":
        Logout.logout()
    elif perintah=="summonjin":
        Summonjin.summonjin()
    elif perintah=="hapusjin":
        Hapusjin.hapusjin()
    elif perintah=="kumpul":
        Kumpul.kumpul()
    elif perintah=="bangun":
        Bangun.bangun()
    elif perintah=="batchbangun":
        Batchbangun.batchbangun()
    elif perintah=="batchkumpul":
        Batchkumpul.batchkumpul()
    elif perintah=="help":
        Help.help()
    elif perintah=="save":
        Save.save()
    elif perintah=="exit":
        Exit.exit()
    elif perintah=="laporanjin":
        Laporanjin.laporanjin()
    elif perintah=="laporancandi":
        Laporancandi.laporancandi()
    elif perintah=="hapusjin":
        Hapusjin.hapusjin()
    elif perintah=="hancurkancandi":
        Hancurkancandi.hancurkancandi()
    elif perintah=="ayamberkokok":
        Ayamberkokok.ayamberkokok()
    elif perintah=="ubahjin":
        Ubahjin.ubahjin()
        