import os
import deck
import gameFunctions


playerTurn = 1
playerHandDict = {}

#creates the deck
theDeck = deck.Deck()

#shuffles the deck
theDeck.shuffle()

#gets number of players in the game
players = gameFunctions.how_many_players()

#generate player list and creates the data for playerHandDict dictionary which holds the cards for each players hand
playerList = gameFunctions.generate_player_list(players)
for items in playerList:
  playerHandDict[items] = [] 

#generate the scoreDict that holds the scoring for the game
scoreDict = gameFunctions.generate_score_dict(playerList)

if players == 2:
  cardsToDeal = 7
else:
  cardsToDeal = 5

#deals the cards to the dictionary
playerHandDict = theDeck.deal(playerHandDict, cardsToDeal)

#checks players hands for 4 of a kind before the game starts
playerHandDict, scoreDict = gameFunctions.check_4_of_a_kind(playerHandDict,scoreDict,playerList)

#main game loop and the var to kill the loop
gameInPlay = True
while gameInPlay:
  #statements to decide if the game is over or not. if the deck is empty and all player hands = [] the game is over
  if theDeck.empty == True:
    emptyHands = 0
    for key, values in playerHandDict.items():
      if values == []:
        emptyHands += 1
      if emptyHands == len(playerList):
        gameInPlay = False
  
  #prints the deck
  #print('THE DECK ',theDeck.deck)
  
  '''Uncomment next line to see if the deck is empty during game play'''
  #print(theDeck.empty)
  

    
  #user Turn
  if playerTurn == 1:
    turn = playerTurn

    #prints the score
    print('\nThis is the score ')
    print(scoreDict)    
 
    #prints the users hand
    for key, value in playerHandDict.items():
      cardsInHand = 0
      for items in value:
        cardsInHand += 1
        #print(items)
      print(key,'had',cardsInHand,'cards in hand')
    print('USER HAND\n')
    for card, suit in playerHandDict[playerList[turn-1]]:
      print(card, suit)  
    print('\n')
    
    #draws card is the user hand is empty and the deck is not
    if playerHandDict[playerList[turn-1]] == [] and theDeck.empty == False:
      for nums in range(0,5):
        ''''DRAW ATTENTION HERE FOR THE RUN OUT OF CARDS'''
        if theDeck.empty == False:
          playerHandDict[playerList[turn-1]].append(theDeck.draw())
        else:
          print('deck ran out of cards before 5')
        #prints the hand after the update
        for key, value in playerHandDict[playerList[turn-1]]:
          print(key, value,)
        print('\n')
 
    #if the user doesn't have any cards cause the deck is empty from the above statement it advances to the next players turn   
    if playerHandDict[playerList[turn-1]] == []:
      playerTurn += 1
    
    #if user goes they get to select the player, else a random player is chosen other than the players turn it is.
    else:
      playerSelected = gameFunctions.choose_player(playerList,playerTurn)

      #try to get input from user
      try:
        card = gameFunctions.choice(playerHandDict[playerList[turn-1]])
      except Exception as e:
        print(e)
      
      #uses the check_for_card function to see if the opponent has a card of type card
      #and adds it to current player hand if it does.     
      foundCard,playerHandDict = gameFunctions.check_for_card(card,playerHandDict,playerList,turn,playerSelected)
      
      #prints the hand after the update
      #for key, value in playerHandDict[playerList[turn-1]]:
       # print(key, value,)
      
      #if the card is found it remains players 1's turn otherwise it advances to the next player turn
      if foundCard == True:
        playerTurn = 1
      else:
        playerTurn += 1
        
      #if its player 2's turn its the same thing as go-fish so draw a card       
      if playerTurn == 2:
        if theDeck.empty == False:
          playerHandDict[playerList[turn-1]].append(theDeck.draw())
        else:
          print('THE DECK OUT OF CARDS' )
      else:
        os.system('cls')
        print('STILL PLAYER 1 TURN')

      #checks for 4 of a kind and returns playerHandDict and scoreDict
      playerHandDict,scoreDict = gameFunctions.check_4_of_a_kind(playerHandDict,scoreDict,playerList)
      '''CLEAR SCREEN'''
      os.system('cls')
  
  #not the users turn so computer goes  
  else:
    #makes the variable turn equal to the player turn so we evaluate the correct player hand 
    turn = playerTurn
    
    #what to set turn back to, to go again for the computer if it found the correct card
    repeatTurn = turn
    
    #draws 5 card if the computer doesn't have any and the deck isn't empty
    if playerHandDict[playerList[turn-1]] == [] and theDeck.empty == False:
      for nums in range(0,5):
        if theDeck.empty == False:
          playerHandDict[playerList[turn-1]].append(theDeck.draw())
        else:
          print('no cards')

    #if the computer has cards and the deck is empty the computer still guesses for cards
    if playerHandDict[playerList[turn-1]] == []:
      #sets foundCard to false because it didn't get to guess
      foundCard = False
      #advances the computer turn      
      playerTurn = gameFunctions.turn_checker(playerList,playerTurn,foundCard)
    else:
    
      #print('ACTUAL PLAYERS HAND')
      #print(playerHandDict[playerList[turn-1]])
      if playerHandDict[playerList[turn-1]] != []:
        card = gameFunctions.computer_turn(playerHandDict[playerList[turn-1]])
        print('\n')
        #selects a player for the computer to get cards from
        playerSelectedByComputer = gameFunctions.choose_player(playerList,playerTurn)
        
        if playerHandDict[playerList[playerSelectedByComputer]] != []:
          foundCard, playerHandDict = gameFunctions.check_for_card(card,playerHandDict,playerList,turn,playerSelectedByComputer)
          
          if bool(foundCard) == True:
            playerTurn = repeatTurn
          else:
            foundCard = False
      '''CLEAR SCREEN'''
      #os.system('cls')
      print(playerList[turn-1],'choose ',card)
      if bool(theDeck.empty) == False and bool(foundCard) == False:
        
        playerHandDict[playerList[turn-1]].append(theDeck.draw())    
    
      if playerHandDict[playerList[turn-1]] != []:
        playerHandDict,scoreDict = gameFunctions.check_4_of_a_kind(playerHandDict,scoreDict,playerList)
      else:
        print('THE COMPUTER HAND WAS EMPTY')
        playerHandDict,scoreDict = gameFunctions.check_4_of_a_kind(playerHandDict,scoreDict,playerList)
    
      print('THIS CARD WAS FOUND ',foundCard)    
      
      if foundCard == False:
      #advances the computer turn      
        playerTurn = gameFunctions.turn_checker(playerList,playerTurn,foundCard)


#END OF LOOP      
print('!!!!GAME OVER!!!!\nFinal Score')
print(scoreDict)

#Win/tie logic
gameFunctions.win_printer(scoreDict)
    
  


