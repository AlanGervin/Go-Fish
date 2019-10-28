from random import choice as choose

def choice(currentPlayerHand):
  cards_held_by_player = []
  for items in currentPlayerHand:
    cards_held_by_player.append(items[0])  
  choice = None
  while choice == None:
      try:
        choice = str(input('ask for a card, valid choices are(A,2,3,4,5,6,7,8,9,10,J,Q,K) but you must have one of that type card: '))
      except Exception as e:
        print(e)
      if choice.upper() in cards_held_by_player:
        return choice.upper()
      else:
        choice = None
        print('you do not have a card of that type')
  

def check_for_card(turn,card,otherPlayerHand,currentPlayerHand):
  '''checks to see if the opponent has a card of type choice
  and adds it to current player hand if it does.  it updates the turn variable if the 
  opponent has the card so the player will go again or do nothing so the next player will go 
  '''
  foundCard = False
  index = 0
  #cards = otherPlayerHand
  '''OUT OF INDEX'''
  #out of index
  while index != len(otherPlayerHand):
    '''See how the while look works'''
    #print('does card ',otherPlayerHand[index][0], 'equal ', card)
    if otherPlayerHand[index][0] == card:
      actualCard = otherPlayerHand.pop(index)
      currentPlayerHand.append(actualCard)
      foundCard = True 
    else:
      index += 1

  if foundCard == True:
    turn = 0
  else:
    turn = 1
  return turn,otherPlayerHand,currentPlayerHand
  
def check_for_card_computer(turn,card,otherPlayerHand,currentPlayerHand):
  '''checks to see if the opponent has a card of type choice
  and adds it to current player hand if it does.  it updates the turn variable if the 
  opponent has the card so the player will go again or do nothing so the next player will go 
  '''
  foundCard = False
  index = 0
  #cards = otherPlayerHand
  '''OUT OF INDEX'''
  #out of index
  while index != len(otherPlayerHand):
    '''See how the while look works'''
    #print('does card ',otherPlayerHand[index][0], 'equal ', card)
    if otherPlayerHand[index][0] == card:
      actualCard = otherPlayerHand.pop(index)
      currentPlayerHand.append(actualCard)
      foundCard = True 
    else:
      index += 1

  if foundCard == True:
    turn = 1
  else:
    turn = 0
  return turn,otherPlayerHand,currentPlayerHand

def check_4_of_a_kind(currentPlayerHand,currentPlayerScore):
  cardList = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  number = 0
  
  cardListCount = []
  #makes cardListCount
  for items in cardList:
    cardListCount.append([items,number])
  
  #for cards in players hand(currentPlayerHand) compare each card in cardListCount(listCount) and add one to list count for the card
  for cardsInHand in currentPlayerHand:
    for listCount in cardListCount:
      if cardsInHand != None:    
        if listCount[0] == cardsInHand[0]:
          listCount[1] += 1
      else:
        return(currentPlayerHand,currentPlayerScore)        
  
  for listCount in currentPlayerHand:
    if listCount != []:
      for listCount in cardListCount:
        if str(listCount[1]) == '4':
          currentPlayerScore += 1
          #print(currentPlayerScore,'after')
          remove_cards = listCount[0]
          #print(remove_cards,'Removed Card from hand')
          count = len(currentPlayerHand)-1
          while count >= 0:
            if currentPlayerHand[count][0] == remove_cards:
              currentPlayerHand.pop(count)
            count-=1
      return(currentPlayerHand,currentPlayerScore)
    else:
      return(currentPlayerHand,currentPlayerScore)  
  
def computer_turn(currentPlayerHand):
  cards_to_ask_for = []
  if currentPlayerHand != []:
    for items in currentPlayerHand:
      cards_to_ask_for.append(items)
    card = choose(cards_to_ask_for)
    card = card[0]
    return card
  else:
    pass

  