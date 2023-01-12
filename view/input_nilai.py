def nama():
    global nm
    nm = input ("Masukkan Nama Mahasiswa \t\t: ")
    return nm
def nim():
    global n
    n = input ("Masukkan NIM Mahasiswa  \t\t: ")
    return n
def tugas():
    global tgs
    tgs = int(input("Masukkan Nilai Tugas \t: "))
    return tgs
def uts():
    global ut
    ut = int(input("Masukkan Nilai UTS    \t: "))
    return ut
def uas():
    global us
    us = int(input("Masukkan Nilai UAS    \t: "))
    return us
def akhir():
    global akh
    akh = tgs*30/100+ ut*35/100 + us*35/100
    return akh