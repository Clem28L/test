import MyClass

SamuelRecord = MyClass.MyClass()
AnnieRecord = MyClass.MyClass("Annie", 44)

print(SamuelRecord.GetAge())
SamuelRecord.SetAge(33)

print(AnnieRecord.GetName())
AnnieRecord.SetName("Sophie")

print(SamuelRecord)
print(AnnieRecord)
