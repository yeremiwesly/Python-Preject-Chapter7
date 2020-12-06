try:
    file = open("h:/myfile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
#saya menggunakan direktori h:\
