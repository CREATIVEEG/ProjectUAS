from model.daftar_nilai import daftarnilai
from view.view_nilai import mencari

while True:
    b = daftarnilai()
    c = mencari()
    print('\nTambah\t(1)\nUbah\t(2)\nCari\t(3)\nHapus\t(4)\nLihat\t(5)\nKeluar\t(6)')
    a = input('Masukkan pilihan > ')
    if (a=="1"):
        b.tambah_data()
    elif (a=="2"):
        b.ubah_data()
    elif (a=="3"):
        c.cetak_hasil_pencarian()
    elif (a=="4"):
        b.hapus_data()
    elif (a=="5"):
        c.cetak_daftar_nilai()
    else :
        b.keluar()
        break
