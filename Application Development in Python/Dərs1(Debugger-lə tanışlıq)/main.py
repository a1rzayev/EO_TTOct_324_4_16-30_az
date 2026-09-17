# dəyişənləri local olaraq yaratdıq
a = 0
b = 0
# dəyişənləri daxil edirik
a = int(input("A deyishenin daxil et: "))
b = int(input("B deyishenin daxil et: "))

print("A =", a)
# debugger-lə yoxlanış edirik, breakpoint qoyaraq
print("B =", a) # səhvən "b" əvəzinə "a" dəyişənin qeyd etdik
print("A + B =", a + b)