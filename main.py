def pokerGame():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    userDeck = []
    dealerDeck = []
    userTotal = 0
    dealerTotal = 0

    continueGame = True
    user_input = input("Do you want to play a game of BlackJack?, type 'y' for yes or 'n' for no: ")

    if user_input == 'y':
        for card in range(2):
            randomCard = random.choice(cards)
            userDeck.append(randomCard)

        randomCard = random.choice(cards)
        dealerDeck.append(randomCard)
        userTotal = sum(userDeck)

        print(f"Your cards: {userDeck}, total: {userTotal}")
        print(f"Dealers first card: {dealerDeck}")
    else:
        continueGame = False

    while continueGame == True:
        shallHit = input("Press 'y' to hit, press 'n' to stay: ")
        if shallHit == 'y':
            randomCard = random.choice(cards)
            userDeck.append(randomCard)
            userTotal = sum(userDeck)
            if userTotal > 21 and 11 in userDeck:
                userDeck.remove(11)
                userDeck.append(1)
                userTotal = sum(userDeck)
                print(f"Your cards: {userDeck}, total: {userTotal}")
                continueGame = True
            elif userTotal > 21:
                print(f"Your cards: {userDeck}, total: {userTotal}")
                print("Game over ")
                continueGame = False
            else: 
                print(f"Your cards: {userDeck}, total: {userTotal}")
        else:
            continueGame = False
            
            while dealerTotal <= 17:
                randomCard = random.choice(cards)
                dealerDeck.append(randomCard)
                dealerTotal = sum(dealerDeck)
                if(dealerTotal > 21): 
                    print("Dealer Busted, you win!") 
                    continueGame = False

                if dealerTotal == userTotal:
                    print(f"Your cards: {userDeck}, total: {userTotal}")
                    print(f"Dealer cards: {dealerDeck}, total: {dealerTotal}")
                    print("Games a Tie")

                elif(userTotal > dealerTotal):
                    print(f"Your cards: {userDeck}, total: {userTotal}")
                    print(f"Dealer cards: {dealerDeck}, total: {dealerTotal}")
                    print("You win!")

                else: 
                    print(f"Your cards: {userDeck}, total: {userTotal}")
                    print(f"Dealer cards: {dealerDeck}, total: {dealerTotal}")
                    print("You lose!")
                
            pokerGame()

pokerGame()
