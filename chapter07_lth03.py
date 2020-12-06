#Protek Chapter 07 latihan nomer 3
print ("-----------------------------")
print ("  PROGRAM HITUNG RATA-RATA  ")
print ("-----------------------------")

kondisi = True
sum = 0
awal = 0

while (kondisi == True):
    try:
        bil = int (input("Masukkan bilangan bulat : "))
        sum = sum + bil
        awal += 1
        
        pastikanlagibro = input ("Lagi (y/n) ? : ")
        if pastikanlagibro != 'y' :
            kondisi = False
            print ("\nRata-rata adalah ", sum/awal)
    except (ValueError):
        print ('Bukan bilangan bulat')
