#Protek Chapter 07 Latihan 1

try :
    file = input ("Masukkan nama file : ")
    bukaFile = open(file, "r")
    print ("Isi File tersebut adalah ", "\n")
    print("=========================")
    print(bukaFile.read())       
except (FileNotFoundError):
    print("File tidak ditemukan", "\n Perhatikan alamat file tersebut")
            
