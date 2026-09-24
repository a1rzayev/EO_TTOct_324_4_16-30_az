import random

def game(choise, result):
    print("")
    print("=====Welcome to ROCK PAPER SCISSORS=====")
    computer_choise = random.choice("rps")
    print("----------------------------------------")
    print("Your select - ", str.capitalize(choise))
    print("Computer select - ", str.capitalize(computer_choise))
    if(str.lower(choise) == computer_choise):
        print("Draw!")
        print(f"Computer: {result["computer"]}, Player: {result["player"]}")
    elif(str.lower(choise) == "r" and
         computer_choise == "p"):
        result["computer"] += 1
        print(f"Computer: {result["computer"]}, Player: {result["player"]}")
    elif(str.lower(choise) == "r" and
         computer_choise == "s"):
        result["player"] += 1
        print(f"Computer: {result["computer"]}, Player: {result["player"]}")
    elif(str.lower(choise) == "p" and
         computer_choise == "s"):
        result["computer"] += 1
        print(f"Computer: {result["computer"]}, Player: {result["player"]}")
    elif(str.lower(choise) == "p" and
         computer_choise == "r"):
        result["player"] += 1
        print(f"Computer: {result["computer"]}, Player: {result["player"]}")
    elif(str.lower(choise) == "s" and
         computer_choise == "r"):
        result["computer"] += 1
        print(f"Computer: {result["computer"]}, Player: {result["player"]}")
    elif(str.lower(choise) == "s" and
         computer_choise == "p"):
        result["player"] += 1
        print(f"Computer: {result["computer"]}, Player: {result["player"]}")
    

result = {"computer": 0, "player": 0}
choise = input("Select R / P / S - ")
game(choise, result)