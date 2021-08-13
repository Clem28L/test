Value = input("Tapez moins de 8 caractères : ")
LetterNum = 1

for Letter in Value:
   print ("La lettre ", LetterNum, " est ", Letter)
   LetterNum+=1
else:
   print("La chaîne est vide.")
