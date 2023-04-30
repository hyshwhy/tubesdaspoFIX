import Save

def exit():
    syarat=True
    while syarat:
        ans=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N)").upper()
        if ans=="Y":
            syarat=False
            Save.save()
        elif ans=='N':
            syarat=False
