def Hello4(ArgCount, *VarArgs):
    print("Vous avez passé ", ArgCount, " argument(s).")
    for Arg in VarArgs:
       print(Arg)

Hello4(1, "Chaîne test.")
Hello4(3, "Un", "Deux", "Trois")
