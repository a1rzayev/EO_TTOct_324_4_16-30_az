# turtle kitabxanasından "*"(hər bir şeyi) yüklə(import elə)
from turtle import *

shape("turtle") # forması turtle(tısbağa) 
color("orange") # rəngi narıncı
pensize(15) # qələmin ölçüsün qeyd edirik
for i in range(10): # 0-dan 10-a çatmamış(9-a qədər) təkrarlanacaq
    forward(100) # 100px irəli
    left(180) # sola 180 dərəcə
    forward(100)
    left(180)
    left(36)
    penup() # qələmi qaldır(çəkməyəcək)
    right(90) # sağa 90 dərəcə
    forward(100)
    left(90) # sola 90 dərəcə
    pendown() # qələmi sal(çəkəcək)

input() # rəsm bitəndən sonra proqram tez sönməsin