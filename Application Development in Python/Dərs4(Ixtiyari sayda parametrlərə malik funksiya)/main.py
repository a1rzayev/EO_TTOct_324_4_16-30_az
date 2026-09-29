def summa(x, y): # dəqiq sayda arqument(parametrlər)
    return x + y

print(summa(10, 5))


# *args = (elem_1, elem_2, ..., elem_n)
def shop_list(*args): # *args (arguments) Ixtiyari sayda arqument qəbul edir
    print(type(args))
    for argument in args:
        print(argument)

# shop_list("Bread", "Tomatoes", "Sud", "Meat")
shop_list(1, 1, 1.5, "Bravo")


# **kwargs = {key_1:value_1, key_2:value_2, ..., key_n:value_n}
def shop_list_named(shop_name, **kwargs): # **kwargs(keyword arguments) Ixtiyari sayda adlı parametr qəbul edir
    print(type(kwargs))
    print(shop_name)
    for argument in kwargs:
        print(argument, kwargs[argument])

shop_list_named("Bravo", bread = 1, tomatoes = 1.5, milk = 1, meat = 2)