LetterNum = 1

for Letter in "Bonjour !":
   if Letter == "j":
      pass
      print("La lettre j rencontrée, non traitée.")
      LetterNum+=1
      continue
   print("La lettre ", LetterNum, " est ", Letter)
   LetterNum+=1
