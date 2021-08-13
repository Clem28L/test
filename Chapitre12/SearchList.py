Colors = ["Rouge", "Orange", "Jaune", "Vert", "Bleu"]

ColorSelect = ""

while str.upper(ColorSelect) != "QUITTER":
   ColorSelect = input("Sélectionnez le nom d'une couleur: ")
   if (Colors.count(ColorSelect) >= 1):
      print("La couleur existe dans la liste !")
   elif (str.upper(ColorSelect) != "QUITTER"):
      print("La liste ne contient pas cette couleur.")
