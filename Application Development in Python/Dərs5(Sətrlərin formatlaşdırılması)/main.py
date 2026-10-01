name = "ali"
surname = "Ibrahimzade"
birthday = "19th June"

print("student:", name) # "vergül" sətir sıralaması(space var arasında)
print("student:" + name) # "+" sətir sıralaması(space yoxdur)
print(f"student: {name}") # "f" sətir sıralaması(space yoxdur)
print(f"Hi I am {name} {surname}. I was born on {birthday}")
print(len(name)) # len(length) - uzunluq

print(f"name: {name}") 
print(f"name: {name.upper()}") # bütün simvolu böyük edir
print(f"name: {name}".capitalize()) # ancaq ilk sözün ilk simvolu böyük edir
print(f"name: {name}".title()) # hər sözün ilk simvolu böyük edir
print(f"name: {name.lower()}") # bütün simvolu kiçik edir
print(f"         name: {name}           ".strip()) # başda və sonda space-ləri silir

a = "Salam menim adim Yusifdir, men telebeyem"
print(a)
a = a.replace("Yusifdir", "Rauldur") # ilk sözü bütün sətr boyunca ikincinə dəyişir
print(a)

fenn = "Riyaziyyat"
print("z" in fenn) # simvolun sətrdə olub olmamadığın göstərir
print(fenn.count("y")) # simvolun sətrdə neçə dəfə olduğunu göstərir