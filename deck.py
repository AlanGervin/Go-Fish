#deck
from random import randint
from random import choice
import os


def deck():
  '''Creates a list of cards in a deck of cards
  '''
  card_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  suit_list = ['hearts','spades','diamonds','clubs']
  deck = []
  for suit in suit_list:
    for card in card_list:
      deck += [card, suit],
  return deck

class Deck(object):
  '''Object that represents a deck of cards and its functions
     mydeck = deck.Deck() #create a deck object.       
     mydeck = mydeck.shuffle() #shuffle's the deck object created in line above.
     mydeck = mydeck.draw() #draw a card from the deck  
  '''
  def __init__(self):
    self.deck = deck()
    self.count = len(self.deck)
    self.empty = False
    
  def shuffle(self):
    '''shuffles the deck
    '''    
    shuffled_deck = []
    count = 0
    while count < len(self.deck):
      deck_length = len(self.deck)
      number = randint(0,deck_length-1)
      item = self.deck.pop(number)
      shuffled_deck.append(item)
    self.deck = shuffled_deck

  def draw(self):
    '''takes a card from the top of the deck and returns it
    '''
    if self.empty == False:
      card_drawn = self.deck.pop(0)
      self.count -= 1
      #uncomment following two lines to see the card drawn and the deck
      #print(card_drawn)
      #print(self.deck)
      if self.count == 0:
        self.empty = True
      return(card_drawn)
    else:
      pass
    
  def deal(self,cards_to_deal):
    '''deals the number of cards passed as an argument and returns computerHand and userHand.
       example: 
          deck.deal(6)
       
       This will deal 6 cards to computerHand and userHand and return them in variable computerHand, userHand
    '''
    userHand = []
    computerHand = []
    for nums in range(0,cards_to_deal):
      computerHand.append(self.deck.pop(0))
      userHand.append(self.deck.pop(0))
      self.count -= 2
    if self.count == 0:
      self.empty = True
    return computerHand,userHand
  
  
