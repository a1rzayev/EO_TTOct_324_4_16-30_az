# *args list-lə əvəz etmək
def way(v, t): # məsafəni tapmaq üçün funksiya
    way = v * t
    print(way)

way(10, 5) # sadə funksiya çağırışı

list_1 = [60, 2] 

way(*list_1) # pointer-lə çağırış



# **kwargs dictionary-lə əvəz etmək
dict_1 = {"v": 60, "t": 2}

way(**dict_1)