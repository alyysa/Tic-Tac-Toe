#Tic Tac Toe
#Board 
board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

#Global Variables
#If game still going on
game_still_going = True

#who won
winner = None

#check number of moves for Tie
counter = 0
#Curret player

current_player = "X"

#Display Board
def display_board():
  
  print(board[0] + " | " + board[1]+ " | " + board[2])
  print(board[3] + " | " + board[4]+ " | " + board[5])
  print(board[6] + " | " + board[7]+ " | " + board[8])

#Play Game Main Function
def play_game():
  print("Tic Tac Toe")

  global winner
  display_board()
  
  while game_still_going:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  if winner != None:
    print("The winner is "+ winner)
  else:
    print("The match is Tied")

#handle each turn
def handle_turn(player):
  global counter
  position = input(player + "'s turn, choose a position from 1-9 : ")

  #input validations
  while True:

    if position == None or position.isnumeric() == False:
      position = input("Invalid input " + player + "'s turn Please Enter a number between 1-9 ")

    elif int(position)>9 or int(position)<1:
      position = input("Invalid input " + player + "'s turn Please Enter a number between 1-9 ")

    elif board[int(position)-1] != "-":
      position = input("Position already Filled " + player + "'s turn Please Enter a unoccupied number between 1-9 ")

    else:
      break   
      

  #assign move to Board 
  position = int(position) - 1

  board[position] = current_player
  counter = counter + 1
  display_board()


#chech if the game is over
def check_if_game_over():
  check_if_win()
  check_if_tie()

#Check if win
def check_if_win():
  check_row()
  check_col()
  check_dia()

  return

#check if Tie
def check_if_tie():
  global game_still_going

  if counter == 9:
    game_still_going = False
  return 

#Flip player for each turn
def flip_player():
  global current_player

  if current_player == "X":
      current_player = "O"
  else:
     current_player = "X"
  return

#checking row wise
def check_row():
  global winner, game_still_going

  if board[0] == board[1] == board[2] != "-" :
    winner = board[0]
    game_still_going = False
    
  elif board[3] == board[4] == board[5] != "-" :
    winner = board[3]
    game_still_going = False
    
  elif board[6] == board[7] == board[8] != "-" :
    winner = board[6]
    game_still_going = False
  return  
 
    
#Checking column wise  
def check_col():
  global winner, game_still_going

  if board[0] == board[3] == board[6] != "-" :
    winner = board[0]
    game_still_going = False
    
  elif board[1] == board[4] == board[7] != "-" :
    winner = board[1]
    game_still_going = False
    
  elif board[2] == board[5] == board[8] != "-" :
    winner = board[2]
    game_still_going = False
  return

#Checking diagonal
def check_dia():
  global winner, game_still_going

  if board[0] == board[4] == board[8] != "-" :
    winner = board[0]
    game_still_going = False
    
  elif board[2] == board[4] == board[6] != "-" :
    winner = board[2]
    game_still_going = False

  return

 
#Invoke main Function
play_game()

