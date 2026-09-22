import math # riyazi modulu yükləyirik


def first_function(): # funksiya yaradılması def(definition)
    pass # boş buraxılacaq bir sətr(yəni heç bir şey etmir)

print(first_function) # funksiyanın məlumatın çap edirik 
print(first_function()) # funksiyanın qaytardığı veriləni çap edirik 



def say_hello(): # salam çap edən bir funksiya
    text = "Ataxan"
    return text # əldə etdiyimiz nəticəni qaytarırıq

print(say_hello())



def summ(x, y): # cəm tapmaq üçün funksiya
    return x + y

print(summ(5, 10))

print(summ(int(input("arg1: ")), int(input("arg2: "))))



def rectangle_area(height, width): # dörtbucaqın sahəsin tapmaq üçün funksiya
    return height * width

print(rectangle_area(10, 5))


def circle_area(radius, Pi = 3.14): # dairənin sahəsin tapmaq üçün funksiya
    return Pi * radius ** 2

print(circle_area(10, math.pi))