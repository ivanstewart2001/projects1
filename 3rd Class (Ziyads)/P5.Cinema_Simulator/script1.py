movies = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
}

while True:
    choice = input("What movie would you like to see?: ").strip().title()

    if choice in movies:
        age = int(input("How old are you?: ").strip())

        #Check user age
        if age >= movies[choice][0]:
            #check enough seats

            num_seats = movies[choice][1]

            if num_seats > 0:
                print("Enjoy the movie!")
                movies[choice][1] = movies[choice][1] - 1
            else:
                print("Sorry we are sold out.")
                
        else:
            print("You are too young to see that movie!")

    else:
        print("We don't have that film...")
