import random as rand
slumptal = rand.randint(1, 10)
a = 0
while True:
    a += 1
    gissning = int(input(f"Försök {a}: Gissa talet: "))
    if slumptal == gissning:
        print("Rätt gissat!")
        break
    else:
        print("Fel gissat")
        continue
    