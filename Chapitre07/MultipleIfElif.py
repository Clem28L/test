﻿print("1. Oeufs")
print("2. Crêpes")
print("3. Gaufres")
print("4. Céréales")
MainChoice = int(input("Que voulez-vous au petit déjeuner ? "))

if (MainChoice == 2):
   Meal = "Crêpes"
elif (MainChoice == 3):
   Meal = "Gaufres"

if (MainChoice == 1):
   print("1. Galette au froment")
   print("2. Beignet")
   print("3. Galette de seigle")
   print("4. Crêpe nature")
   Pancake = int(input("Choisissez un type de crêpe : "))

   if (Pancake == 1):
      print("Vous avez choisi des oeufs avec une galette au froment.")
   elif (Pancake == 2):
      print("Vous avez choisi des oeufs avec des beignets.")
   elif (Pancake == 3):
      print("Vous avez choisi des oeufs avec une galette de seigle.")
   elif (Pancake == 4):
      print("Vous avez choisi des oeufs avec une crêpe nature.")
   else:
      print("Nous avons des oeufs, mais pas ce type de crêpe.")
      
elif (MainChoice == 2) or (MainChoice == 3):
   print("1. Sirop")
   print("2. Confiture de fraises")
   print("3. Sucre en poudre")
   Topping = int(input("Choisissez une garniture : "))

   if (Topping == 1):
      print ("Vous avez choisi " + Meal + " au sirop.")
   elif (Topping == 2):
      print ("Vous avez choisi " + Meal + " à la confiture de fraises.")
   elif (Topping == 3):
      print ("Vous avez choisi " + Meal + " avec du sucre en poudre.")
   else:
      print ("Nous avons des " + Meal + ", mais pas cette garniture.")
      
elif (MainChoice == 4):
   print("Vous avez choisi des céréales.")
   
else:
   print("Désolé, nous n'avons pas cela dans notre menu !")
