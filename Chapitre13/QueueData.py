﻿import queue

MyQueue = queue.Queue(3)

print(MyQueue.empty())
input("Appuyez sur une touche quand vous êtes prêt...")

MyQueue.put(1)
MyQueue.put(2)
print(MyQueue.full())
input("Appuyez sur une touche quand vous êtes prêt...")

MyQueue.put(3)
print(MyQueue.full())
input("Appuyez sur une touche quand vous êtes prêt...")

print(MyQueue.get())
print(MyQueue.empty())
print(MyQueue.full())
input("Appuyez sur une touche quand vous êtes prêt...")

print(MyQueue.get())
print(MyQueue.get())
