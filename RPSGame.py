from random import randint

#create a List of play options
choices = ["Rock", "Paper", "Scissors"]
player = False

#assign a random play to the computer
computer = choices[randint(0,2)]

#show the computer's choice in the terminal window
print("Computer chooses:" , computer)

player = 5
computer = 5

while player == False:
#set player to True
    print("Choose your weapon!")
    player = input("Rock, Paper, Scissors?")
    
    print(player, "\n")

    if player == computer:
    	print("Tie!")
    
    elif player == "Rock":
    	if computer == "Paper":
    		print("you Lose !", computer, "covers", player)
    	else:
    		print("You Win!", player, "smashes", computer)
   
    elif player == "Paper":
    	if computer == "Scissors":
    		print("You Lose!", computer, "cut", player)
    	else:
    		print("You win!", player, "covers", computer)
   
    elif player == "Scissors":
    	if computer == "Rock":
    		print("You lose...", computer, "smashes", player)
    	else:
    		print("You win!", player, "cut", computer)
    elif player == "quit":
        exit()
    else:
    	print("That's not a valid play. Check your spelling!\n")

    #reset the game loop and start again
    #player was set to True, but we want it to be false so the loop continues
    player = False
    computer = choices[randint(0,2)]