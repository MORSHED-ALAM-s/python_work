name = input("What's your name")

match name:
    case "Manik" | "Morshed" | "Roton":
        print("Friend")
    case "Tota":
        print("New Friend")
    case _:
        print("Who?")