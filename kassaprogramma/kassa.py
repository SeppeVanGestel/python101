import pcinput
import korting
import bestelling



# Na het beëindigen van het kassaprogramma berekenen we het nieuwe kassatotaal en drukken dit af 
# samen met de naam van de kassabediende. NOK

beginsituatie_kassa = 0
naam = pcinput.getString("geef je naam in a.u.b.")

while True:
   
    aantal_friet, aantal_koniginnenhapjes, aantal_ijs, aantal_drank  = bestelling.startBestelling()
    
    #lukt me niet om dit in een functie te steken, zijn de waarden garbagecollected?
    totaal_friet = aantal_friet * 20
    totaal_koniginnenhapjes = aantal_koniginnenhapjes * 10
    totaal_ijsjes = aantal_ijs * 3
    totaal_drank = aantal_drank * 2
    

    rekening = totaal_friet + totaal_koniginnenhapjes + totaal_ijsjes + totaal_drank
    nieuw_bedrag = rekening - korting.berekening(rekening, totaal_friet) 

    

    print(f"te betalen {nieuw_bedrag}")           
    betaling = pcinput.getInteger("Geef het ontvangen bedrag in: ")
    teruggave = betaling - nieuw_bedrag
    bestelling.toonTeruggave(teruggave)



    kassaticket = pcinput.getString("Wenst U een kassaticket? Y voor ja N voor nee")
    
    #als ok deze functie in de import zet herkent python de variabelen niet meer bv aantal friet
    def print_ticket(kassaticket):

        if kassaticket == "Y":
            print("*" *72)
            print("{:^65}".format("Rekening:"))
            print("*" *72)
            print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal mosselen friet ",aantal_friet,"st.", totaal_friet, "euro."))
            print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal koniginnenhapjes ",aantal_koniginnenhapjes,"st.", totaal_koniginnenhapjes, "euro."))
            print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal ijs ",aantal_ijs,"st.", totaal_ijsjes, "euro."))
            print("| {:30} | {:8}{:8} | {:10}  {} |".format("Aantal drank ",aantal_drank,"st.", totaal_drank, "euro."))
            print("*" *72)


            print("| {:30} | {:29}  {} |".format("Totaal:",rekening,"euro."))
            print("| {:30} | {:29}  {} |".format("Uw korting:",korting.berekening(rekening,totaal_friet),"euro."))
            print("| {:30} | {:29}  {} |".format("Totaal te betalen:" ,nieuw_bedrag,"euro."))
            print("*" *72)
    
    print_ticket(kassaticket) 

    #We vragen ook de beginsituatie van de de vorige shift aan het programma en tellen hierbij het nieuwe bedrag op,
    #de eerste keer neemt het programme de globale variabele, deze wordt in de local scope geupdated, hiermee gaan we verder rekenen

    
    beginsituatie_kassa = beginsituatie_kassa + nieuw_bedrag
    

    print(f"Het kassatotaal is: {beginsituatie_kassa}")
    # We blijven daarna in het kassaprogramma totdat de bediende op het einde aangeeft te willen stoppen (Stoppen? J/N: ).

    einde_shift = pcinput.getString("einde shift? typ Y VOOR JA of N voor NEE")

    if einde_shift =="Y":
        
        #print(f"het eindbedrag van {naam} is:{beginsituatie_kassa}")
        print("*" *46) 
        print("| {:30} |            |".format("Einde Shift"))
        print("| {:25}{:5} |   {}{} |".format("Het eindbedrag van" ,naam, beginsituatie_kassa ," euro."))
        print("*" *46) 
        break


    



