import random

computer_score = 0
player_score = 0
tied_score =  0
rounds_played = 0



while True:
    print(" Let's play Rock Paper Scissors !")
    select = input("If you would like to play against the computer, press r. To stop, press s: ")
    if select == "r":
        player_selected = input("rock paper scissors ? ")
        print(f"Player chooses -------------------------------------->{player_selected}")
        choices = ['rock', 'paper', 'scissors']
        computer_selected = random.choice(choices)
        print(f"Computer chooses.....{computer_selected}!")
        # code to know who won and 
        if player_selected == computer_selected :
            rounds_played = rounds_played + 1
            tied_score = tied_score + 1
            print(f"Tie!!!! \n Player Score : {player_score} || Computer Score : {computer_score} || Rounds Played : {rounds_played}")
        elif player_selected == "rock" and computer_selected == "scissors":
            rounds_played = rounds_played + 1
            player_score = player_score + 1
            print(f"Player won! Computer lost!\n Player Score : {player_score} || Computer Score : {computer_score} || Rounds Played : {rounds_played}")
        elif player_selected == "rock" and computer_selected == "paper":
            rounds_played = rounds_played + 1
            computer_score = computer_score + 1
            print(f"Player lost! Computer won!\n Player Score : {player_score} || Computer Score : {computer_score} || Rounds Played : {rounds_played}")
        elif player_selected == "paper" and computer_selected == "scissors":
            rounds_played = rounds_played + 1
            computer_score = computer_score + 1
            print(f"Player lost! Computer won!\n Player Score : {player_score} || Computer Score : {computer_score} || Rounds Played : {rounds_played}")
        elif player_selected == "paper" and computer_selected == "rock":
            rounds_played = rounds_played + 1
            player_score = player_score + 1
            print(f"Player won! Computer lost!\n Player Score : {player_score} || Computer Score : {computer_score} || Rounds Played : {rounds_played}")
        elif player_selected == "scissors" and computer_selected == "rock":
            rounds_played = rounds_played + 1
            computer_score = computer_score + 1
            print(f"Player lost! Computer won!\n Player Score : {player_score} || Computer Score : {computer_score} || Rounds Played : {rounds_played}")
        elif player_selected == "scissors" and computer_selected == "paper":
            rounds_played = rounds_played + 1
            player_score = player_score + 1
            print(f"Player won! Computer lost!\n Player Score : {player_score} || Computer Score : {computer_score} || Rounds Played : {rounds_played}")
    
    
    elif select == "s":
        print("Game stopped.")
        break
    else:
        print("Invalid input. Please press 'r' to play or 's' to stop.")








# add the logic of to keep a track of rounds and when user press s it prints game stopped and also show
# Out of x rounds, player won y rounds. 