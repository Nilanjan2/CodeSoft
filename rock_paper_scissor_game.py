#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        # Instructions
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=('Helvetica', 14))
        self.label.pack(pady=20)
        
        # Buttons for choices
        self.rock_button = tk.Button(root, text="Rock", width=15, command=lambda: self.play('rock'))
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(root, text="Paper", width=15, command=lambda: self.play('paper'))
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: self.play('scissors'))
        self.scissors_button.pack(pady=5)
        
        # Score display
        self.score_label = tk.Label(root, text="Scores\nYou: 0\nComputer: 0", font=('Helvetica', 14))
        self.score_label.pack(pady=20)
        
    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        winner = self.determine_winner(user_choice, computer_choice)
        
        self.display_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1
        
        self.update_score()
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'
        
    def display_result(self, user_choice, computer_choice, winner):
        result_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"
        if winner == 'tie':
            result_message += "It's a tie!"
        elif winner == 'user':
            result_message += "You win!"
        else:
            result_message += "You lose!"
        messagebox.showinfo("Result", result_message)
        
    def update_score(self):
        self.score_label.config(text=f"Scores\nYou: {self.user_score}\nComputer: {self.computer_score}")

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()




















