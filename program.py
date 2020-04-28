x_count = 0
o_count = 0
s_count = 0
game_still_on = True
current_player = "X"
list = ["_" ,"_" ,"_" ,"_" ,"_" ,"_" ,"_" ,"_" ,"_" ]


def display(): #display the matrix
  print("-------------")
  print("| "+list[0]+" | "+list[1]+" | "+ list[2]+" |")
  print("| "+list[3]+" | "+ list[4]+" | "+ list[5]+" |")
  print("| "+list[6]+" | "+ list[7]+" | "+ list[8]+" |")
  print("-------------")
def count(): #count the number of X ,O and _
  global x_count,o_count,s_count
  x_count = o_count = s_count = 0
  for x in list:
    if x == "X":
        x_count = x_count + 1
    elif x == "O":
        o_count = o_count + 1
    elif x == "_":
        s_count = s_count + 1
  print(x_count,o_count,s_count)
def check(): #to check the winner
  global game_still_on
  if ((list[0] == list[1] == list[2] == "X" or list[3] == list[4] == list[5] == "X" or list[6] == list[7] == list[8] == "X" or list[0] == list[3] == list[6] == "X" or list[1] == list[4] == list[7] == "X" or list[2] == list[5] == list[8] == "X" or list[0] == list[4] == list[8] == "X" or list[2] == list[4] == list[6] == "X") and (list[0] == list[1] == list[2] == "O" or list[3] == list[4] == list[5] == "O" or list[6] == list[7] == list[8] == "O" or list[0] == list[3] == list[6] == "O" or list[1] == list[4] == list[7] == "O" or list[2] == list[5] == list[8] == "O" or list[0] == list[4] == list[8] == "O" or list[2] == list[4] == list[6] == "O")) or ((x_count-o_count) >= 2 or (o_count-x_count) >= 2):
    print("Impossible")
    game_still_on = False
  elif list[0] == list[1] == list[2] == "X" or list[3] == list[4] == list[5] == "X" or list[6] == list[7] == list[8] == "X" or list[0] == list[3] == list[6] == "X" or list[1] == list[4] == list[7] == "X" or list[2] == list[5] == list[8] == "X" or list[0] == list[4] == list[8] == "X" or list[2] == list[4] == list[6] == "X":
    print("X wins")
    game_still_on = False
  elif list[0] == list[1] == list[2] == "O" or list[3] == list[4] == list[5] == "O" or list[6] == list[7] == list[8] == "O" or list[0] == list[3] == list[6] == "O" or list[1] == list[4] == list[7] == "O" or list[2] == list[5] == list[8] == "O" or list[0] == list[4] == list[8] == "O" or list[2] == list[4] == list[6] == "O":
    print("O wins")
    game_still_on = False
  else:
    if s_count > 0:
      print("Game not finished")
    else:
      print("Draw")
      game_still_on = False
def get_input(current_player): #take the index input
  print(current_player+"'s turn!")
  index = input("Enter the index (1-9)")
  index = int(index) - 1
  list[index] = current_player
def switch_player(): # to switch the player from X to O and vise versa
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
def play_game(): #runs the game
  display()
  while game_still_on:
    get_input(current_player)
    display()
    count()
    check()
    switch_player()



play_game()