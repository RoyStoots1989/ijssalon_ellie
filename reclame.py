from algemene_functies import mijn_functie_2
   
aanbieding_1 = {
    "smaak": "aardbei",
    "prijs": 4,
    "korting": 0.1
} 
nieuwe_prijs = aanbieding_1["prijs"] *(1-aanbieding_1["korting"])
print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {aanbieding_1 ["smaak"]} van {aanbieding_1["prijs"]} euro voor {nieuwe_prijs} euro.")


def inkomsten_totaal(inkomsten, btw=None):
    totaal = sum (inkomsten)
    if btw is not None:
        btw_bedrag = totaal * btw
        return f"het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return f"het totaal van alle inkomsten van deze week is {totaal} euro."
inkomsten_deze_week = [220, 430, 125, 160, 205, 90,345]
print(inkomsten_totaal(inkomsten_deze_week,0.09))

def gemiddelde(inkomsten_deze_week):
    gemiddelde= sum(inkomsten_deze_week) / len(inkomsten_deze_week)
    return f"de gemiddelde inkomsten deze week zijn {gemiddelde} euro "
inkomsten_deze_week=[220,430,125,160,205,90,345]

print(gemiddelde(inkomsten_deze_week))

def meervoudig(invoer_lijst):
    hoogste, laagste, = hoog_en_laag(invoer_lijst)
    return[hoogste, laagste]

def hoog_en_laag(invoer_lijst):
    hoogste=max(invoer_lijst)
    laagste= min(invoer_lijst)
    return hoogste, laagste

inkomsten_deze_week=[10,5,3,2,1,2,9]

print(meervoudig(inkomsten_deze_week))

def combinatie(invoer_lijst_2):
    korte_lijst=hoog_en_laag(invoer_lijst_2)   
    resultaat = mijn_functie_2(korte_lijst)
    return resultaat


    


    
