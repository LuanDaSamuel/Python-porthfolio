#Find SYT

#Ohjelma määrittää lukujen 396 ja 332 suurimman yhteisen tekijän
#Eukleideen algoritmilla. Ohjelma tulostaa algoritmin välivaiheet ja
#suurimman yhteisen tekijän.

luku1 = 396  #jaettava
luku2 = 332  #jakaja

print("Määritetään lukujen", luku1, "ja", luku2, "suurin yhteinen tekijä.")

jakoj = 1  #Asetetaan jakojäännöksen arvoksi nollasta poikkeava luku.

while jakoj != 0:  #Toistetaan niin kauan kuin jakoj ≠ 0.

    osam = luku1 // luku2  #Lasketaan osamäärä.
    jakoj = luku1 % luku2  #Lasketaan jakojäännös.

    #Tulostetaan jakoyhtälö.
    print(luku1, "=", luku2, "*", osam, "+", jakoj)

    luku1 = luku2  #Asetetaan uudeksi jaettavaksi jakaja.
    luku2 = jakoj  #Asetetaan uudeksi jakajaksi jakojäännös.

#Tulostetaan viimeinen nollaa suurempi jakojäännös.
print("Suurin yhteinen tekijä:", luku1)


#Continue to find PYM

#Ohjelma määrittää lukujen 396 ja 332 suurimman yhteisen tekijän
#Eukleideen algoritmilla. Ohjelma tulostaa algoritmin välivaiheet ja
#suurimman yhteisen tekijän.

luku1 = 396  #jaettava
luku2 = 332  #jakaja

#Talennetaan kantanumeroja

alku1 = luku1
alku2 = luku2

print("Määritetään lukujen", luku1, "ja", luku2, "suurin yhteinen tekijä.")

jakoj = 1  #Asetetaan jakojäännöksen arvoksi nollasta poikkeava luku.

while jakoj != 0:  #Toistetaan niin kauan kuin jakoj ≠ 0.

    osam = luku1 // luku2  #Lasketaan osamäärä.
    jakoj = luku1 % luku2  #Lasketaan jakojäännös.

    #Tulostetaan jakoyhtälö.
    print(luku1, "=", luku2, "*", osam, "+", jakoj)

    luku1 = luku2  #Asetetaan uudeksi jaettavaksi jakaja.
    luku2 = jakoj  #Asetetaan uudeksi jakajaksi jakojäännös.



#Tulostetaan viimeinen nollaa suurempi jakojäännös.
print("Suurin yhteinen tekijä:", luku1)

syt = luku1

pym = alku1 * alku2 // syt

print("Pienen yhteinen monikerta on", pym)
