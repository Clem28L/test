MyStack = []
StackSize = 3

def DisplayStack():
   print("État courant de la pile :")
   for Item in MyStack:
      print(Item)
   
def Push(Value):
   if len(MyStack) < StackSize:
      MyStack.append(Value)
   else:
      print("La pile est pleine !")

def Pop():
   if len(MyStack) > 0:
      MyStack.pop()
   else:
      print("La pile est vide.")

Push(1)
Push(2)
Push(3)
DisplayStack()
input("Appuyez sur une touche quand vous êtes prêt...")

Push(4)
DisplayStack()
input("Appuyez sur une touche quand vous êtes prêt...")

Pop()
DisplayStack()
input("Appuyez sur une touche quand vous êtes prêt...")

Pop()
Pop()
Pop()
DisplayStack()
