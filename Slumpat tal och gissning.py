import random as rand
slumptal = rand.randint(1, 10)
gissning = int(input("Gissa ett tal mellan 1 och 10: "))
if slumptal == gissning:
    print("Rätt gissat!")
else:
    print(f"Tyvärr, det var {slumptal}")