import random
# # # # #
print("Welcome to Rock, Paper, Scissors! You will be playing against the computer for victory. Do your best!")
# # # # #
continuation = "yes"
series = 'yes'
series_num = 0
game_count = 0
player_wins = 0
player_win_total = 0
computer_wins = 0
computer_win_total =0
ties = 0
ties_total = 0
player_throw = ""
computer_throw = ""
rounds = 0
rounds_count = 0

# # # # # # #
while series == "yes":
    
    series_num = series_num + 1
    rounds_count = 0
    player_wins = 0
    computer_wins = 0
    ties = 0
    rounds = int(input("Please input how many rounds you would like to play (Make sure it is an ODD number):   "))
     # # # -`-`-`-`-`-`- # # #
    while continuation == "yes":

        computer_throw = random.choice(['rock', 'paper', 'scissors'])
        print("Round", rounds_count+1)
        player_throw = input("Choose your throw: Rock, Paper, or Scissors?:   ")
        print('The Computer threw', computer_throw, ': The Player Threw', player_throw, '!')
        game_count += 1
    ### -`-`-`-`-`-`-`-`- ###
        ''' ### STALEMATES ### '''
        while player_throw == computer_throw:
            print('It was a tie!')
            ties += 1
            ties_total += 1
            player_throw = ""

        ''' ### COMPARING THROWS ### '''
        if player_throw == 'rock':
            if computer_throw == 'paper':
                print('The Computer has won the match!')
                computer_wins += 1
                computer_win_total += 1
            elif computer_throw == 'scissors':
                print('The Player has won the match!')
                player_wins += 1
                player_win_total += 1
        ###### ######### ###### 
        if player_throw == 'scissors': 
            if computer_throw == 'paper':
                print('The Player has won the match!')
                player_wins += 1
                player_win_total += 1
            elif computer_throw == 'rock':
                print('The Computer has won the match!')
                computer_wins += 1
                computer_win_total += 1
        ###### ######### #######
        if player_throw == 'paper':
            if computer_throw == 'rock':
                print('The Player has won the match!')
                player_wins += 1
                player_win_total += 1
            elif computer_throw == 'scissors':
                print('The Computer has won the match!')
                computer_wins += 1
                computer_win_total += 1
        ### ####### ### ####### ###
        rounds_count += 1
        
        if computer_wins == (round(rounds/2+0.5)):
            print("The Computer has won this game!")
            continuation = 'no'
        if player_wins == (round(rounds/2+0.5)):
            print('The Player has won this game!')
            continuation = 'no'

        if rounds_count == rounds:
            continuation = 'no'

    series = input("Would you like to continue the Matches?:   ")
    continuation = 'yes'
# # # # # # #
print('The Matches have ended')
print('You have played', series_num, 'series of matches.') 
print('In the last match, The Player won', player_wins, 'matches, while The Computer won', computer_wins, 'matches. There were', ties, 'tied matches.')
print('In this Series, The Player has won', player_win_total, 'matches overall, while The Computer has won', computer_win_total, 'matches overall. There were', ties_total, ' overall tied matches.')
# # # #
if player_win_total >= computer_win_total:
    print('The Player is the overall winner of this game!')
else:
    print('The Computer has won the overall game!')