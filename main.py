import random

deck = ["Red 0", "Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9",
        "Green 0", "Green 1", "Green 2", "Green 3", "Green 4", "Green 5", "Green 6", "Green 7", "Green 8", "Green 9",
        "Blue 0", "Blue 1", "Blue 2", "Blue 3", "Blue 4", "Blue 5", "Blue 6", "Blue 7", "Blue 8", "Blue 9",
        "Yellow 0", "Yellow 1", "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", "Yellow 7", "Yellow 8",
        "Yellow 9",
        #"Red Skip", "Green Skip", "Blue Skip", "Yellow Skip",
        #"Red Draw Two", "Green Draw Two", "Blue Draw Two", "Yellow Draw Two",
        #"Wild", "Wild Draw Four"
        ] * 4
random.shuffle(deck)
player_hand = []
computer_hand = []
for i in range(7):
    player_hand.append(deck.pop())
    computer_hand.append(deck.pop())

turn = "player"
while True:
    print()
    print("Your hand: ", player_hand)
    print("Computer's hand: ", len(computer_hand), "cards")
    current_card = deck[-1]
    print("Current card: ", current_card)
    try:
        player_choice = input("Enter the card you want to play, or 'd' to draw a card: ")
        if player_choice == "d":
            player_hand.append(deck.pop())
            print()
            print("You drew 1 card")
        elif player_choice in player_hand:
            #if "Wild" in player_choice:
                #while True:
                    #color = input("Enter color to change the Wild card to (red, green, blue, yellow): ")
                    #if color in ["red", "green", "blue", "yellow"]:
                        #player_choice = color + " Wild"
                        #break
                    #else:
                        #print("Invalid color, please enter a valid color.")
            if player_choice[:-1] == current_card[:-1] or player_choice.split()[1] == current_card.split()[1]:
                current_card = player_choice
                player_hand.remove(player_choice)
                deck.append(player_choice)
                print()
                print("You played a", player_choice)
                #if "Skip" in player_choice:
                    #if turn == "player":
                        #turn = "computer"
                    #else:
                        #turn = "player"
                #elif "Draw Two" in player_choice:
                    #if turn == "player":
                        #computer_hand += [deck.pop(), deck.pop()]
                    #else:
                        #player_hand += [deck.pop(), deck.pop()]
                #elif "Reverse" in player_choice:
                    #if turn == "player":
                        #turn = "computer"
                    #else:
                        #turn = "player"
            else:
                print()
                print("Invalid choice, try again")
                continue
        else:
            print()
            print("Invalid choice, try again")
            continue
    except ValueError:
        print("Invalid Input, Please enter the correct card")
        continue
    except IndexError:
        print("Invalid Input, Please enter the correct card")
        continue

    if len(player_hand) == 0:
        print()
        print("You won!")
        break


    card_drawn = False
    for i, card in enumerate(computer_hand):
        #if "Wild" in card:
            #color_list = ["red", "green", "blue", "yellow"]
            #computer_choice = color_list[random.randint(0,3)] + " Wild"
        if card[:-1] == current_card[:-1] or card.split()[1] == current_card.split()[1]:
            current_card = card
            deck.append(computer_hand.pop(i))
            print()
            print("Computer played a", card)
            #if "Skip" in card:
                #if turn == "player":
                    #turn = "computer"
                #else:
                    #turn = "player"
            #elif "Draw Two" in card:
                #if turn == "player":
                    #computer_hand += [deck.pop(), deck.pop()]
                #else:
                    #player_hand += [deck.pop(), deck.pop()]
            #elif "Reverse" in card:
                #if turn == "player":
                    #turn = "computer"
                #else:
                    #turn = "player"
            break
    else:
        if not card_drawn:
            computer_hand.append(deck.pop())
            card_drawn = True
            print()
            print("Computer drew 1 card")
        else:
            pass

    if len(computer_hand) == 0:
        print()
        print("The computer won!")
        break



