try:
   Ex = ValueError()
   Ex.strerror = "La valeur doit être comprise entre 1 et 10."
   raise Ex
except ValueError as e:
   print("Exception ValueError !", e.strerror)
   
