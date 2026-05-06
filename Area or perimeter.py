#Final result
r = float(input("Anna ympyrän säde: "))
print("Lasketaanko ympyrän piiri (p) vai pinta-ala (a)?")
print("Valitse p/a: ")
vastaus = input()
if r > 0 and vastaus == "p":
    piiri = 2 * 3.14 * r
    print(piiri)
    print("Piiri:", round(piiri, 2))
elif r > 0 and vastaus == "a":
    ala = 3.14 * r ** 2
    print(ala)
    print("Ala:", round(ala, 2))
elif vastaus != "p" or vastaus != "a":
    print("Annoit jonkin muun vastauksen kuin p tai a.")
    print("Ohjelman suoritus päättyy.")
else:
    print("Annoit virheellisen säteen arvon")
    print("Ohjelman suoritus päättyy.")

#Bài của một khứa hôi lông trên MAOL2
r = float(input("Anna ympyrän säde: "))
print("Lasketaanko ympyrän piiri (p) vai pinta-ala (a)?")
print("Valitse p/a: ")
vastaus = input()
if r > 0:
if vastaus == "p":
piiri = 2 * 3.14 * r
print("Piiri:", round(piiri, 2))
else:
if vastaus == "a":
ala = 3.14 * r ** 2
print("Ala:", round(ala, 2))
else:
print("Annoit jonkin muun vastauksen kuin p tai a.")
print("Ohjelman suoritus päättyy.")
else:
print("Annoit virheellisen säteen arvon")
print("Ohjelman suoritus päättyy.")
