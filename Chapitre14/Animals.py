class Animal:
   def __init__(self, Name="", Age=0, Type=""):
      self.Name = Name
      self.Age = Age
      self.Type = Type

   def GetName(self):
      return self.Name

   def SetName(self, Name):
      self.Name = Name

   def GetAge(self):
      return self.Age

   def SetAge(self, Age):
      self.Age = Age

   def GetType(self):
      return self.Type

   def SetType(self, Type):
      self.Type = Type

   def __str__(self):
      return "{0} est un {1} âgé de {2} ans.".format(self.Name,
                                            self.Type,
                                            self.Age)

class Chicken(Animal):
   def __init__(self, Name="", Age=0):
      self.Name = Name
      self.Age = Age
      self.Type = "poulet"

   def SetType(self, Type):
      print("Désolé, {0} sera toujours un {1}."
            .format(self.Name, self.Type))

   def MakeSound(self):
      print("{0} dit Cot, Cot, Cot, Codette !".format(self.Name))
