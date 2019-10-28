import os
import deck
import gameFunctions

userHand = []
computerHand = []
turn = 0
otherPlayerHand = [] 
currentPlayerHand = []
userScore = 0
computerScore = 0


theDeck = deck.Deck()
theDeck.shuffle()
computerHand,userHand = theDeck.deal(7)

userHand,userScore = gameFunctions.check_4_of_a_kind(userHand,userScore)
computerHand,computerScore = gameFunctions.check_4_of_a_kind(computerHand,computerScore)

gameInPlay = True
while gameInPlay:
  if theDeck.empty == True and currentPlayerHand == [] and otherPlayerHand == []:
    gameInPlay = False
#while computerHand and userHand != [] or theDeck.empty == True:
  
  print('\nThis is computer score '+str(computerScore))
  print('\nThis is user score '+str(userScore))
  '''Uncomment next line to see if the deck is empty during game play'''
  #print(theDeck.empty)
  #prints the users hand
  print('USER HAND\n')
  for items in userHand:
    print(items)
  '''Uncomment next lines to see the computer hand during game play'''
  #print('COMPUTERHAND\n')
  #for items in computerHand:
    #print(items)
  #print('\n')

  
  
  
  
  #changes which hand is considered the currentPlayerHand, currentPlayerScore, and otherPlayerHand
  if turn == 0:
    currentPlayerHand = userHand
    currentPlayerScore = userScore
    otherPlayerHand = computerHand
  else:
    currentPlayerHand = computerHand
    currentPlayerScore = computerScore
    otherPlayerHand = userHand    
  
  if turn == 0:

    if currentPlayerHand == [] and theDeck.empty == False:
      for nums in range(0,5):
        ''''DRAW ATTENTION HERE FOR THE RUN OUT OF CARDS'''
        if theDeck.empty == False:
          currentPlayerHand.append(theDeck.draw())
        else:
          pass
      print(currentPlayerHand,'This stuff')
      #try to get input from user
    if currentPlayerHand != []:
      try:
        card = gameFunctions.choice(currentPlayerHand)
      except Exception as e:
        print(e)
      
      #uses the check_for_card function to see if the opponent has a card of type choice
      #and adds it to current player hand if it does.  it updates the turn variable if the 
      #opponent has the card so the player will go again or do nothing so the next player will go
      if otherPlayerHand != []:
        turn, otherPlayerHand, currentPlayerHand = gameFunctions.check_for_card(turn,card,otherPlayerHand,currentPlayerHand)
      else:
        turn = 1
      if turn == 1 and theDeck.empty != True:
        currentPlayerHand.append(theDeck.draw())
      
      #checks for 4 of a kind and returns current player hand and score
      currentPlayerHand,currentPlayerScore = gameFunctions.check_4_of_a_kind(currentPlayerHand,currentPlayerScore)    
      '''CLEAR SCREEN'''
      os.system('cls')
      
      #assigns current player score and hand to the user variables
      userScore = currentPlayerScore
      userHand = currentPlayerHand
      #print(theDeck.empty)
    
  else:
    #draws 5 card if the computer doesn't have any and the deck isn't empty
    if currentPlayerHand == [] and theDeck.empty == False:
      for nums in range(0,5):
        if turn == 1 and theDeck.empty == False:
          currentPlayerHand.append(theDeck.draw())
    
    print('COMPUTER TURN\n\n')
    if currentPlayerHand != []:
        card = gameFunctions.computer_turn(currentPlayerHand)
        if otherPlayerHand != []:
          turn, otherPlayerHand, currentPlayerHand = gameFunctions.check_for_card_computer(turn,card,otherPlayerHand,currentPlayerHand)
        else:
          turn = 0
    computerScore = currentPlayerScore
    computerHand = currentPlayerHand
    '''CLEAR SCREEN'''
    os.system('cls')
    print('Computer Choose ',card)
    if turn == 0 and theDeck.empty == False:
      currentPlayerHand.append(theDeck.draw())
    if currentPlayerHand != []:
      currentPlayerHand,currentPlayerScore = gameFunctions.check_4_of_a_kind(currentPlayerHand,currentPlayerScore)
    computerScore = currentPlayerScore
    computerHand = currentPlayerHand
      #print('hand after go fish\n')
      #for items in currentPlayerHand:
       #   print(items)
    if turn == 0 and theDeck.empty != True:
      if currentPlayerHand == []:
        for nums in range(0,5):
          if turn == 0 and theDeck.empty == False: 
            currentPlayerHand.append(theDeck.draw())    
          
print('!!!!GAME OVER!!!!\nFinal Score')
print('\nThis is user score '+str(userScore))
print('\nThis is computer score '+str(computerScore))

#Win/lose logic
if userScore > computerScore:
  print('\n!!!!YOU WIN!!!!')
elif computerScore > userScore:
  print('\n!!!!YOU LOSE!!!!')
else:
  print('\n!!!!YOU TIED!!!!')  

      
    
  


