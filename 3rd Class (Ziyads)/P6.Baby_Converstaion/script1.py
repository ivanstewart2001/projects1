from random import choice

questions = ["Why does LeBron always choke?: ", "How isn't Tom Brady retired yet?: ", "How do the Knicks always find a way to suck?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh....Okay")