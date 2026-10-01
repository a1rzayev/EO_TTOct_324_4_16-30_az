import random

print("DÖYÜŞ ROBOTLARI")
print("----------------")

name1 = input("Birinci robotun adını yaz: ")
name2 = input("İkinci robotun adını yaz: ")

robot1 = {
    "name": name1,
    "energy": 100,
    "damage": random.randint(15, 30),
    "defense": random.randint(5, 15)
}

robot2 = {
    "name": name2,
    "energy": 100,
    "damage": random.randint(15, 30),
    "defense": random.randint(5, 15)
}

print()
print("Robotlar hazırdır.")
print()

print(f"{robot1['name']} - Enerji: {robot1['energy']} - Zərər: {robot1['damage']} - Müdafiə: {robot1['defense']}")
print(f"{robot2['name']} - Enerji: {robot2['energy']} - Zərər: {robot2['damage']} - Müdafiə: {robot2['defense']}")

print()
print("Döyüş başladı!")
print("----------------")

round_number = 1

while robot1["energy"] > 0 and robot2["energy"] > 0:

    print()
    print(f"{round_number}-ci raund")

    # Birinci robot hücum edir
    attack = robot1["damage"] - robot2["defense"]

    if attack < 1:
        attack = 1

    robot2["energy"] -= attack

    if robot2["energy"] < 0:
        robot2["energy"] = 0

    print(f"{robot1['name']} hücum etdi.")
    print(f"{robot2['name']} {attack} zərər aldı.")
    print(f"{robot2['name']} enerjisi: {robot2['energy']}")

    if robot2["energy"] <= 0:
        break

    # İkinci robot hücum edir
    attack = robot2["damage"] - robot1["defense"]

    if attack < 1:
        attack = 1

    robot1["energy"] -= attack

    if robot1["energy"] < 0:
        robot1["energy"] = 0

    print(f"{robot2['name']} hücum etdi.")
    print(f"{robot1['name']} {attack} zərər aldı.")
    print(f"{robot1['name']} enerjisi: {robot1['energy']}")

    round_number += 1


print()
print("----------------")
print("Döyüş başa çatdı.")
print()

if robot1["energy"] > 0:
    print(f"Qalib: {robot1['name']}")
elif robot2["energy"] > 0:
    print(f"Qalib: {robot2['name']}")
else:
    print("Heç-heçə!")

print()
print("Yekun nəticə:")
print(f"{robot1['name']}: {robot1['energy']} enerji")
print(f"{robot2['name']}: {robot2['energy']} enerji")
