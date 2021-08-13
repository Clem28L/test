def PrintBlue():
   print("Vous avez choisi bleu !\r\n")
   
def PrintRed():
   print("Vous avez choisi rouge !\r\n")

def PrintOrange():
   print("Vous avez choisi orange !\r\n")

def PrintYellow():
   print("Vous avez choisi jaune  !\r\n")

ColorSelect = {
   0: PrintBlue,
   1: PrintRed,
   2: PrintOrange,
   3: PrintYellow
}

Selection = 0

while (Selection != 4):
   print("0. Bleu")
   print("1. Rouge")
   print("2. Orange")
   print("3. Jaune")
   print("4. Quitter")

   Selection = int(input("Sélectionnez une option de couleur : "))

   if (Selection >= 0) and (Selection < 4):
      ColorSelect[Selection]()
