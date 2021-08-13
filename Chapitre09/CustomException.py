class CustomValueError(ValueError):
   def __init__(self, arg):
      self.strerror = arg
      self.args = {arg}

try:
   raise CustomValueError("La valeur doit être comprise entre 1 et 10.")
except CustomValueError as e:
   print("Exception CustomValueError !", e.strerror)
