from random import choice as choose

def choice(currentPlayerHand):
  cards_held_by_player = []
  for items in currentPlayerHand:
    cards_held_by_player.append(items[0])  
  choice = None
  '''
  uncomment the following #line and the first #line of the while loop, 
  and comment out the try block to have the game auto choose cards
  '''
  #comment out the following line
  theList=['a','2','3','4','5','6','7','8','9','10','j','q','k']
  while choice == None:
    #comment out the following line
    choice = choose(theList)
    '''
      #section to comment out for auto choosing
      try:
        choice = str(input('ask for a card, valid choices are(A,2,3,4,5,6,7,8,9,10,J,Q,K) but you must have one of that type card: '))
      except Exception as e:
        print(e)
      #end of section to comment out for auto choosing
    '''
    if choice.upper() in cards_held_by_player:
      return choice.upper()
    else:
      choice = None
      print('you do not have a card of that type')

def choose_player(playerList,playerTurn):
  playerSelect = 0
  count = 1
  playerNumbers = []
  for items in playerList:
    playerNumbers.append(count)
    count+=1
  print(playerTurn,'player turn')
    
  while playerSelect == 0 or playerSelect == playerTurn:
    #comment out this section to have the computer auto choose a player. 
    #also make sure you dedent the section below on randomNumber
    '''
    if playerTurn == 1:
      try:
        playerSelect = int(input('Select a player who\'s hand you would like to select from: '))
      except Exception as e:
        print(e)
      #return playerSelect-1  
    else:
    '''   
   #end of section to comment out for auto choose a player.

      #dedent this line one if you are doing auto choose
    randomNumber = choose(playerNumbers)
    if randomNumber != playerTurn:
      playerSelect = randomNumber
       
  if playerSelect <= len(playerList) and int(playerSelect) > 0:
    if playerSelect == playerTurn:
      print('Cannot select yourself')
    else:
      print('This is the players hand they are looking at',playerSelect)
      return playerSelect-1
  else:
    print('incorrect player selection')
    #playerSelect = 0
    

    
def how_many_players():
  players = 1
  while players == 1:
    try:
      tempPlayers = int(input('input how many players?(2-4)'))
      if tempPlayers >=2 and tempPlayers <= 4:
        players = tempPlayers
    except Exception as e:
      print('must input number between 2-4')
  return int(players)

def generate_player_list(players):
  playerList = []
  player = 'player'
  for nums in range(0,players):
    playerString = player+str(nums+1)
    playerList.append(playerString)
  return playerList

def generate_score_dict(playerList):
  scoreDict = {}
  for items in playerList:
    scoreDict[items] = 0
  return scoreDict
    
def turn_checker(playerList,playerTurn,foundCard):
  numberOfPlayers = len(playerList)
  if bool(foundCard) == True:
    playerTurn += 0
  else:
    playerTurn += 1
  if bool(foundCard) == False and playerTurn == numberOfPlayers+1:
    playerTurn = 1
  return playerTurn

def check_for_card(card,playerHandDict,playerList,turn,playerSelect):
  foundCard = False
  otherPlayerHand = playerHandDict[playerList[playerSelect]]
  index = len(otherPlayerHand)-1
  
  while index >= 0:
    if otherPlayerHand[index][0] == card:
      actualCard = playerHandDict[playerList[playerSelect]].pop(index)
      print(actualCard)
      playerHandDict[playerList[turn-1]].append(actualCard)
      index = len(otherPlayerHand)-1
      foundCard = True
    else:
      index -= 1

  return foundCard,playerHandDict



'''
  foundCard = False
  index = 0
  otherPlayerHand = playerHandDict[playerList[playerSelect]]
  
  for cards in otherPlayerHand:
    if otherPlayerHand[index][0] == card:
      actualCard = playerHandDict[playerList[playerSelect]].pop(index)
      print(actualCard)
      playerHandDict[playerList[turn-1]].append(actualCard)
      foundCard = True
    else:
      index += 1

  return foundCard,playerHandDict
'''
  
  
  
def check_4_of_a_kind(playerHandDict,playerScoreDict,playerList):
  cardList = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  numberOf = 0

  for keys in playerHandDict.keys():
    playerHand = playerHandDict[keys]
 
    #makes cardListCount
    cardListCount = []
    for cards in cardList:
      cardListCount.append([cards,numberOf])

 
    #add one to the listCount for each card of the type in the playerHand  
    for cardsInHand in playerHand:
      for listCount in cardListCount:
        if cardsInHand != []:      
          if listCount[0] == cardsInHand[0]:
            listCount[1] += 1
        else:
          print('THE HAND WAS EMPTY')
       
        

    for cardCount in cardListCount:
      if str(cardCount[1]) == '4':
        playerScoreDict[keys] += 1
        remove_cards = cardCount[0]
        
        cardNumber = len(playerHand)-1
        while cardNumber >= 0:
          if playerHand[cardNumber][0] == remove_cards:
            playerHand.pop(cardNumber)
            cardNumber = len(playerHand)-1
          else:
            cardNumber -= 1
                  
  return(playerHandDict,playerScoreDict)

  
def computer_turn(currentPlayerHand):
  cards_to_ask_for = []
  if currentPlayerHand != []:
    for items in currentPlayerHand:
      cards_to_ask_for.append(items)
    card = choose(cards_to_ask_for)
    card = card[0]
    return card
  else:
    print('something weird happened')

  