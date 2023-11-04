from engine import narrate, speak, yes, choose

def game_over():
    narrate("suddenly a beam of light comes your way")
    narrate("game over")

narrate("You look up and see a UFO")
narrate("It is headed your way")

choice = choose(['hide', 'call for help', 'yell at the aliens'])

if choice == "hide":
    while True:
        narrate("You hide from the aliens")
        narrate('the UFO gets louder')
        choice = choose(['get out', 'keep hiding'])
        if choice == "get out":
            narrate("you break out from hiding")
            game_over()
            break
        elif choice == 'keep hiding':
            narrate("You keep hiding")
elif choice == "call for help":
    narrate("you call for help")
    narrate("suddenly, a penguin comes from the trees")
    speak("penguin", "I will help!")
    narrate("Suddenly a beam of light goes over the penguin")
    narrate("The penguim begins to levitate")
    speak("You", "Thanks for the help")
    narrate("You escape")
    narrate("The End")
elif choice == "yell at the aliens":
    narrate("You begin to yell at the aliens")
    game_over()