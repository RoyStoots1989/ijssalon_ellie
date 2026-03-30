mijn_dictionary= {
    "aardbei" : 3,
  "vanille" : 4,
  "chocolade" : 5}

aanbieding = mijn_dictionary["aardbei"] * 0.8
reclame_tekst= f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2= reclame_tekst[:63]
reclame_tekst3= reclame_tekst2.upper()
reclame_tekst4 = ["Vandaag", "in", "de","aanbieding",":", "vanille-ijs", "1 liter", "-", "slechts", (aanbieding) ]
for el in mijn_dictionary:
  if len(str(el))>= 5:
    print(str(el).upper())
else:
  print(str(el).lower())  