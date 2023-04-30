import Database

def appendGlobalUser(elmt,arr):
    for i in range(lengthList(arr)):
        if arr[i] == ['' for i in range(3)]:
            arr[i]=elmt
            break

def appendGlobalJin(elmt,arr):
    for i in range(lengthList(arr)):
        if arr[i] == ['',0]:
            arr[i]=elmt
            break

def appendGlobal(elmt,arr):
    for i in range(lengthList(arr)):
        if arr[i] == ['' for i in range(lengthList(arr[i]))]:
            arr[i]=elmt
            break

def appendGlobal1D(elmt,arr):
    for i in range(lengthList(arr)):
        if arr[i] == '':
            arr[i]=elmt
            break

def lengthString(str):
    arr = list(str)
    mark = "$$"
    arr = arr + [mark]
    count = 0
    i = 0
    while arr[i] != "$$":
        count += 1
        i += 1
    return count

def lengthList(arr):
    mark = "$$"
    if type(arr) == list:
        arr = arr + [mark]
        count = 0
        i = 0
        while arr[i] != "$$":
            count += 1
            i += 1
        return count
    else:
        arr = [arr]
        arr = arr + [mark]
        count = 0
        i = 0
        while arr[i] != "$$":
            count += 1
            i += 1
        return count 

def MinIdCandi():
    for i in range (100):
        if Database.daftar_candi[i] == [0, "", 0, 0, 0]:
            return i
    

def HitungJin(role):
    count = 0
    for i in range(lengthList(Database.daftar_akun)):
        if Database.daftar_akun[i][2] == role:
            count = count + 1
    return count

def HitungSisaCandi():
    count = 0
    lenArr = lengthList(Database.daftar_candi)
    for i in range(lenArr):
        if Database.daftar_candi[i] == [0, '', 0, 0, 0]:
            count = count + 1
    return(count)

def HitungBaris_daftar_akun():
    count = 0
    for i in range(lengthList(Database.daftar_akun) -1, -1, -1):
        if Database.daftar_akun[i] != ['', '', '']:
            return 102 - count
        count += 1
        if count == 102: return 0

def HitungBaris_daftar_candi():
    count = 0
    for i in range(lengthList(Database.daftar_candi) -1, -1, -1):
        if Database.daftar_candi[i] != [0, '', 0, 0, 0]:
            return 100 - count
        count += 1
        if count == 100: return 0
