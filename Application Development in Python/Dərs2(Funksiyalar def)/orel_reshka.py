from random import randint # random kitabxanasından randint funksiyasın yükləyirik

def coin_simulator(): # oyunumuzun funksiyasın yaradırıq
    coin = randint(0, 1) # 0 və 1 arasında rast gələ bir ədəd seçirik
    if(coin == 0): # əgər 0 çıxdısa - Orel
        print("Orel")
    else: # əgər 0 çıxmadısa(1 çıxdı) - Reshka
        print("Reshka")

coin_simulator() # oyunu başladırıq(funksiyanı çağıraraq)