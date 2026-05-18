#from structure 10 to structure 2

print("Tämä ohjelma muuntaa kaksijärjestelmän luvun")
print("kymmenjärjestelmän luvuksi")

luku10 = int(input("Anna posittiivinen kokonaisluku: "))

while luku10 <= 0:
    print("Et antanut positiivista kokonaislukua.")
    luku10 = int(input("Anna positiivinen kokonaisluku: "))
jaettava = luku10

luku2 = ""

while jaettava != 0:
    osam =jaettava // 2
    jakoj = jaettava % 2
    luku2= str(jakoj) + luku2
    jaettava = osam
print("10-järjestelmän luku", luku10, "kaksijärjestelmän lukuna:", luku2)

#from structure 2 to structure 2

print("Tämä ohjelma muuntaa kaksijärjestelmän luvun")
print("kymmenjärjestelmän luvuksi")

luku2 = input("Anna kaksijärjetelmän luku: ")

eksponentti = len(luku2) - 1

luku10 = 0

for merkki in luku2:
    if merkki == "1":
        luku10 += 2** eksponentti
    eksponentti -= 1
print("Kaksijärjestelmän luku", luku2, "10-järjestelmän lukuna:", luku10)

