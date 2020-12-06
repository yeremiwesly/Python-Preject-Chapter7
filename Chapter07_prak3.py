try :
    file = open("h:\data.txt", "r")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print('Terdapat tipe data string')
#saya menggunakan direktori h:\
