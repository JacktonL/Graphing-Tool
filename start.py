from files import Start


print("Welcome to the Graph Hub")
print("Type c for Cartesian, p for Polar, or t for Parametric!")


while True:
    choice = input()
    if choice == "c":
        s = Start("cartesian", choice)
        s.start()
        break
    elif choice == "p":
        s = Start("polar", choice)
        s.start()
        break
    elif choice == "t":
        s = Start("parametric", choice)
        s.start()
    else:
        print("Not a valid Grapher!")
