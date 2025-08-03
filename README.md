# rockpaperscissors
This Python script is a Rock, Paper, Scissors game where the player competes against the computer. It tracks wins, losses, ties, and rounds played. The game continues in a loop until the player chooses to stop by pressing 's'. Choices are compared, and scores are updated and displayed after each round.

🕹 Overview
The game allows the user to continuously play Rock, Paper, Scissors against the computer until they decide to stop. It keeps track of:

Player wins

Computer wins

Ties

Total rounds played

📋 How It Works
Prompt to Start or Stop:

The user is asked whether they want to start a game by pressing 'r', or stop by pressing 's'.

Player Input:

If the user chooses to play, they input either "rock", "paper", or "scissors".

Computer's Choice:

The computer randomly selects one of the three options.

Determine the Winner:

A series of if-elif statements compare the player’s choice to the computer’s choice.

It then announces who won, lost, or if it was a tie.

Scores and rounds are updated accordingly.

Score Display:

After each round, it shows:

Player's score

Computer's score

Number of rounds played

Exit Option:

Pressing 's' exits the game gracefully with a message.

✅ Features
Easy-to-follow gameplay loop

Input validation for starting/stopping

Real-time score tracking

Randomized computer choice using Python's random module

