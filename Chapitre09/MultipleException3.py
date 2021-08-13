try:
   Value1 = int(input("Tapez le premier nombre : "))
   Value2 = int(input("Tapez le second nombre : "))
   Output = Value1 / Value2
except ValueError:
   print("Vous devez taper un nombre entier !")
except KeyboardInterrupt:
   print("Vous avez appuyé sur Ctrl+C !")
except ZeroDivisionError:
   print("Tentative de division par zéro !")
except ArithmeticError:
   print("Une erreur de math non définie s'est produite.")
else:
   print(Output)
