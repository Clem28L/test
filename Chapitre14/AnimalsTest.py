import Animals

MyChicken = Animals.Chicken("Arthur", 2)
print(MyChicken)
MyChicken.SetAge(MyChicken.GetAge() + 1)
print(MyChicken)
MyChicken.SetType("Gorille")
print(MyChicken)
MyChicken.MakeSound()
