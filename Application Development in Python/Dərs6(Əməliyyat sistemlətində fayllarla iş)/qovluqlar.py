import os # əməliyyat sistemi ilə iş üçün kitabxana

path = "C:\\Users\\rzayev_a" # adres
path2 = os.path.normpath("C:/Users/rzayev_a") # adres düzəldir

disk = "C:\\"
dir1 = "Users"
dir2 = "rzayev_a"
path3 = os.path.join(disk, dir1, dir2) # adresləri birləşdirir

print(path)
print(path2)
print(path3)

print(os.path.isabs(path)) # absolut adresdir ya yox
print(os.path.isfile(path)) # fayldir ya yox
print(os.path.isdir(path)) # qovluqdur ya yox
print(os.path.islink(path)) # linkdir ya yox

# path(adres), dirnames(qovluq adları), filenames(fayl adları)
for path, dirnames, filenames in os.walk(path): 
    print(f"path - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")

# mkdir(make directory) yeni qovluq yaradir
os.mkdir(os.path.join(disk, dir1, dir2, "YENI QOVLUQ YARATDIQ!"))

# rmdir(remove directory) qovluqu silir
os.rmdir(os.path.join(disk, dir1, dir2, "YENI QOVLUQ YARATDIQ!"))

