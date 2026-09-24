# cavab olacaq 10(local dəyişən(ilk print)) və 5(qlobal dəyişən(ikinci print))
var1 = 5 # qlobal dəyişən
def func1():
    var1 = 10 # lokal dəyişən
    print(var1)
func1()
print(var1)



# səhv olacaq(var1 is not defined) 
def func1():
    var1 = 10 # lokal dəyişən
    print(var1)
func1()
print(var1)



# cavab olacaq 10(qlobal dəyişən(ilk print)) və 10(qlobal dəyişən(ikinci print))
var1 = 10 # qlobal dəyişən
def func1():
    print(var1)
func1()
print(var1)



# cavab olacaq
var1 = 5 # qlobal dəyişən
def func1():
    # print(var1) # error
    var1 = 1 # local dəyişən
    print(var1) # 1
func1()
print(var1) # 5



var1 = 5
def first():
    var1 = 10
    def second():
        print(var1)
    second()
first()
print(var1)

print("globals: ", globals()) # qlobal dəyişən və funksiyalar
print("locals: ", locals()) # local dəyişən və funksiyalar
