class player:
    def __init__ (self, name):
        self.name = name
        self.position = "entrance"
        self.bag = []

    def add__item (self, item):
        if len (self.bag) <4:
            self.bag.append(item)
            print(item, "added to bag")
        else:
            print("bag is full")

def show_menu():
    print("\n1.move")
    print("2.pick up item")
    print("3.check bag")

def move_player (character):
    direction = input ("move forward, left, right, back : ")

    if player.position == "entrance" and direction == "forward":
        player.position = "hallway A"

    elif player.position == "hallway A" and direction == "forward":
        player.position = "hallway B"

    elif player.position == "hallway A" and direction == "left":
        player.position = "lunch room"

    elif player.position == "hallway A" and direction == "right":
        player.position = "toilet room"

    elif player.position == "hallway A" and direction == "forward":
        player.position = "entrance"

    elif player.position == "hallway B" and direction == "back":
        player.position = "hallway A"

    elif player.position == "lunch room" and direction == "back":
        player.position = "hallway A"

    elif player.position == "toilet room" and direction == "back":
        player.position = "hallway A"

    elif player.position == "hallway B" and direction == "left":
        player.position = "cleaners room"

    elif player.position == "hallway B" and direction == "right":
        player.position = "office room"

    elif player.position == "hallway B" and direction == "forward":
        player.position = "hallway C"

    elif player.position == "cleaners room" and direction == "back":
        player.position = "hallway B"

    elif player.position == "office room" and direction == "back":
        player.position = "hallway B"

    elif player.position == "hallway C" and direction == "forward":
        player.position = "hallway D"

    elif player.position == "hallway C" and direction == "back":
        player.position = "hallaway B"

    elif player.position == "hallway D" and direction == "back":
        player.position = "hallway C"

    elif player.position == "hallway D" and direction == "forward":
        player.position = "storage room"

    else:
        print("wrong way")

def pick_item(player):
    if player.position == "lunch room":
        choice = input("spoon on the floor. pick it up (yes/no): ")
        if choice == "yes":
            player.add__item("spoon")

    elif player.position == "toilet room":
        choice = input("bucket on the floor. pick it up (yes/no): ")
        if choice == "yes":
            player.add__item("bucket")

    elif player.position == "cleaners room":
        choice = input("mop on the floor. pick it up (yes/no): ")
        if choice == "yes":
            player.add__item("mop")

    elif player.position == "office room":
        choice = input("papers on the floor. pick it up (yes/no): ")
        if choice == "yes":
            player.add__item("papers")
            
    else:
        print("no item here")

name = input("enter player name: ")
player = player(name)

game_running = True
while game_running:
    print("\ncurrent position:", player.position)
    show_menu()

    try:
        choice = int(input("choose option: "))
    except valueerror:
        print("invalid input")
        continue
    if choice == 1:
        move_player(player)
    elif choice == 2:
        pick_item(player)
    elif choice == 3:
        print("bag:", player.bag)
    else:
        print("invalid choice")

    if player.position == "storage room":
        if len (player.bag) == 4:
            print("\ncleaning is done")
            break
