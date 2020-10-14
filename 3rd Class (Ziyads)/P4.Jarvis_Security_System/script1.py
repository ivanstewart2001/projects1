known_users = ["Brittany", "Courtney", "Geoffrey", "Sydney", "Isaiah"]

while True:
    print("Hi my name is Jarvis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (Y/N)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want to see you go anyway!")

    else:
        print("Hmmmm I dont think I have met you yet {}.".format(name))
        add_me = input("Would you like to be added to the system (Y/N)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")