# Final Project

# Card Memory Game

# Import module random to shuffle the deck
# Import module time to add delays when showing cards
import os
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
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [(suit, rank) for suit in suits for rank in ranks]

# Define a method that shuffles the deck and deals five cards to each player

    def deal_cards(self):       
        random.shuffle(self.deck)
        return self.deck[:5]
    
# Generate a function that clears the terminal

    def clear_terminal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

# Define a method that plays a turn of the game

    def play_turn(self):
        self.turn_count += 1
        print(f"\nTurn {self.turn_count} - Deal Cards:")
        dealt_cards = self.deal_cards()
        for card in dealt_cards:
            print(card)
            time.sleep(1)
        self.clear_terminal()


# Define a method that starts the game and displays instructions

    def start_game(self):
        print("Welcome to the Card Memory Game!")
        print(f"The game will continue until a player reaches {self.max_points} points or after {self.max_turns} turns.\n")
        
        while self.turn_count < self.max_turns:
            for player in self.players:
                if player.points >= self.max_turns:
                    print(f"[player.name] has reached {self.max_points} points. Game Over!")
                    return
                
                self.play_turn()
                self.check_for_winner()

        print("Maximum turns reached. Game Over.")

# Define a method to check if a player has reached the max points

    def check_for_winner(self):
        for player in self.players:
            if player.points >= self.max_points:
                print(f"{player.name} has reached {self.max_points} points. Game Over!")
                exit()

# Set up of the game

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    players = [Player(input(f"Enter name of Player {i+1}: ")) for i in range(num_players)]

    game = CardMemoryGame(players)
    game.start_game()
