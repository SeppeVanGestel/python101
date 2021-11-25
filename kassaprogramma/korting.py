def berekening(rekening, totaal_friet):
    korting = 0
    
    if totaal_friet >=2:
        korting = 20
        
        if rekening >= 150:
            korting = 20
            

        elif rekening >= 100:
            korting = 10

        elif rekening >= 50:
            korting = 5
        
    return korting




    