import pcinput

def startBestelling():
    aantal_friet = pcinput.getInteger("het aantal mosselfriet ")
    aantal_koniginnenhapjes= pcinput.getInteger("het aantal koniginnenhapjes ")
    aantal_ijs= pcinput.getInteger("het aantal ijsjes ")
    aantal_drank= pcinput.getInteger("het aantal dranken ")
    return aantal_friet, aantal_koniginnenhapjes,aantal_ijs,aantal_drank
   

def toonTeruggave(teruggave):
    aantal1 = teruggave//100
    rest = teruggave % 100
    aantal2 = rest//50
    rest = rest % 50
    aantal3 = rest//20
    rest = rest % 20
    aantal4 = rest//10
    rest = rest % 10
    aantal5 = rest//5
    rest = rest % 5
    aantal6 = rest//2
    rest = rest % 2
    aantal7 = rest//1
    rest = rest % 1

        
    print("*" *30)
    print("{:^30}".format("Teruggave:"))
    print("*" *30)

    if aantal1 > 0:
        print("| {:5} | {:20}|".format(aantal1,"briefjes van 100"))
    if aantal2 > 0:
        print("| {:5} | {:20}|".format(aantal2,"briefjes van 50")) 
    if aantal3 > 0:
        print("| {:5} | {:20}|".format(aantal3,"briefjes van 20")) 
    if aantal4 > 0:
        print("| {:5} | {:20}|".format(aantal4,"briefjes van 10")) 
    if aantal5 > 0:
        print("| {:5} | {:20}|".format(aantal5,"briefjes van 5"))  
    if aantal6 > 0:
        print("| {:5} | {:20}|".format(aantal6,"briefjes van 2"))
    if aantal7 > 0:
        print("| {:5} | {:20}|".format(aantal7,"briefjes van 1"))  

    print("*" *30)
    print("Totaal terug te geven:", teruggave, "euro.")

    print("*" *30)




     