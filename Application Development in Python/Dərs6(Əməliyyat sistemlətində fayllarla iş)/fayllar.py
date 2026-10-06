import os # əməliyyat sistemi ilə iş üçün kitabxana

file = open("file.txt", "w") # "w" - write(yazmaq)
file.write("Hello Yusuf")
file.close()

file = open("file.txt", "a") # "a" - append(əlavə etmək)
file.write("Hello Ali")
file.close()

file = open("file.txt", "r") # "r" - read(oxumaq)
print(file.read())
file.close()


with open("file.txt", "w") as file: # adlar məkanı yaradırıq
    file.write("Hello world!")

with open("file.txt", "a") as file:
    file.write("Hello world!")
    
with open("file.txt", "r") as file:
    print(file.read())

print("Salam ushaqlar")

os.mkdir("dir")
os.rename("file.txt", "dir\\adi_deyishmish_file.txt") # fayl adın dəyişmək
os.renames("dir\\adi_deyishmish_file.txt", "file.txt") # fayl adın dəyişmək(boş qovluq qalsa silir)

os.replace("dir\\adi_deyishmish_file.txt", "file.txt") # fayl yerlərin dəyişmək

print(os.path.getctime("file.txt")) # faylın yaradılma vaxtı
print(os.path.getmtime("file.txt")) # faylın son dəyişilmə vaxtı