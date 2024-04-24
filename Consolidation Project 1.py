# Consolidation Project 1

# Card Memory Game

# Import module random to shuffle the deck
# Import module time to add delays when showing cards

import random
import time

# Define a class to represent each player

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def __str__(self):
        return self.name
    
# Define a class to manage the game

class CardMemoryGame:
    def __init__(self, players, max_points = 25, max_turns = 3):
        self.players = players
        self.max_points = max_points
        self.max_turns = max_turns
        self.deck = self.generate_deck()
        self.turn_count = 0

# Generate a standard deck with 13 cards in each of the four suits

def generate_deck(self):
    suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [(suit, rank) for suit in suit for rank in rank]

# Define a method that shuffles the deck and deals five cards to each player



# Define a method that plays a turn of the game



# Define a method that starts the game and displays instructions



# Set up of the game


