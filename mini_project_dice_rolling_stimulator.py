import random


def roll_dice():
    dice_drawing = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",

        ),

        2: (

            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",

        ),

        3: (

            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",

        ),

        4: (

            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",

        ),

        5: (

            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",

        ),

        6: (

            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",

        ),

    }

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("dice rolled: {} and {}".format(dice1, dice2))
    print("\n".join(dice_drawing[dice1]))
    print("\n".join(dice_drawing[dice2]))


while True:
    command = input("Do you want to roll a dice? Yes or No: ")
    if command.title() == "Yes":
        roll_dice()

    else:
        print("Stimulator Ended")
        quit()
