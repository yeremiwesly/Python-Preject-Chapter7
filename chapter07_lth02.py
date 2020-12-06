#Protek Chapter 07 Latihan nomer 2
try :
    namafile = input ("Silahkan masukkan alamat file Anda : ")
    bukadulufilenya = open (namafile, "r")
    kondisi = True
    bukadulufilenya = open(namafile, "a")
    
    while (kondisi == True):
        isi_file = input ("Data yang mau ditambahkan :")
        bukadulufilenya.write(isi_file)
        bukadulufilenya.write("\n")
        
        UdahPasBro = input ("Mau lagi? (y/n) :")
        if (UdahPasBro != 'y'):
            kondisi = False
            bukadulufilenya = open (namafile, "r")
            print ("Tampilan dari file tersebut \n")
            print(bukadulufilenya.read())
            bukadulufilenya.close()
except (PermissionError):
    print ("\n Periksa kembali alamat file yang Anda masukkan")
except (FileNotFoundError):
    print ("\n File tidak ditemukan \n Periksa kembali alamat file anda")
