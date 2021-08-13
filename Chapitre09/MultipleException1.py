try:
   Value = int(input("Tapez un nom entre 1 et 10: "))
except (ValueError, KeyboardInterrupt):
   print("Vous devez taper un nombre entre 1 et 10 !")
else:

   if (Value > 0) and (Value <= 10):
      print("Vous avez tapé : ", Value)
   else:
      print("La valeur que vous avez tapée est incorrecte !")

