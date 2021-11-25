'''
Een klant boekt bij een reisorganisatie een reis met keuze uit verschillende opties: bereken de
totale kostprijs voor deze klant met volgende gegevens:
• Vervoer : enkele reis vliegtuig=200€, enkele reis per autocar=50€, zelf met de auto = 0€.
• Hotel: standaardkamer prijs in hotel Zeezicht=30€/nacht/persoon, hotel
Duinenzicht=25€/nacht/persoon.
• Type kamer: zeezicht = supplement van 10%, balkon=+20€/nacht, luxe suite=+40€/nacht.
• Aantal nachten: hoeveelheidskorting: 7 +1 nacht gratis, 10+2 nachten gratis. (7=7, 8=7, 9=8,
10=9, 11=10, 12=10, 13=11, ….).
• Aantal personen: aantal volwassenen, kinderen (50% korting op kamerprijs en kamertype
supplement).
• Eten: geen ontbijt, met ontbijt (10€/nacht), half pension(30€/nacht), vol pension (40€/nacht).
'''


# kies Vervoer : enkele reis vliegtuig=200€, enkele reis per autocar=50€, zelf met de auto = 0€.

def vervoerskost():
    vliegtuig = 200
    autocar = 50
    zelf = 0
    print(vervoerskost)


#Hotel: standaardkamer prijs in hotel Zeezicht=30€/nacht/persoon, hotel
#Duinenzicht=25€/nacht/persoon.

def hotel(nachten, personen): #if is duinenzicht, if is zeezicht
    duinenenzicht = 25
    zeezicht = 30

