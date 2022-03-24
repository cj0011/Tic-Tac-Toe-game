import os 
clear = lambda: os.system('cls')
should_continue = True
while should_continue:
    board = ["-","-","-",
             "-","-","-",
             "-","-","-"]
    number_board = ["1","2","3",
                    "4","5","6",
                    "7","8","9"]
    odd_player=["1","3","5","7","9"]
    even_player=["0","2","4","6","8"]
    game_working = True
    winner = None
    current_player = "odd"

    def game_board():
      print(board[0]+"|"+board[1]+"|"+board[2],end="\t  " +  number_board[0]+"|"+number_board[1]+"|"+number_board[2] + "\n")
      print(board[3]+"|"+board[4]+"|"+board[5],end="\t  " + number_board[3]+"|"+number_board[4]+"|"+number_board[5] + "\n")
      print(board[6]+"|"+board[7]+"|"+board[8],end="\t  " + number_board[6]+"|"+number_board[7]+"|"+number_board[8] + "\n")


    def play_game():
        game_board()
        while game_working:
            player_turn(current_player)
            check_if_game_over()
            flip_player()
        if winner == "odd" or winner == "even":
            print(f"{winner} won")
        elif winner == None:
            "it's draw"



    def player_turn(player):
      print(f"{player}'s turn")
      position=input("choose a position from 1-9: ")
      valid=False
      while not valid:
          while position not in ["1","2","3","4","5","6","7","8","9"]:
              position=input("invaild input.Choose a position form1-9: ")
          position = int(position)-1
          if current_player=="odd":
            number = input(f"enter the {current_player} number u want: ")
            while number not in odd_player:
                number = input(f"invaild input.enter the {current_player} number u want: ")
            odd_player.remove(number)
          if current_player=="even":
               number = input(f"enter the {current_player} number u want: ")
               while number not in even_player:
                    number = input(f"invaild input.enter the {current_player} number u want: ")
               even_player.remove(number)

        
          if board[position] == "-":
              valid = True
          else:
              print("you cant go there. please try again.")
      board[position]= number

      game_board()


    def check_if_game_over():
        check_win()
        check_draw()


    def check_win():
        global winner
        rows = check_rows()
        columns = check_columns()
        diagonals = check_diagonals()
        if rows:
            winner = rows
        elif columns:
            winner = columns
        elif diagonals:
            winner = diagonals
        else:
            winner = None
        return


    def check_rows():
        global should_continue
        global game_working
        row_1 = False
        row_2 = False 
        row_3 = False
        if board[0] !=  "-" and board[1] !=  "-" and board[2] !=  "-":
            row_1=int(board[0])+int(board[1])+int(board[2])
            if row_1 == 15:
                row_1 = True
        if board[3] !=  "-" and board[4] !=  "-" and board[5] !=  "-":
            row_2=int(board[3])+int(board[4])+int(board[5]) 
            if row_2 == 15:
                row_2 = True
        if board[6] !=  "-" and board[7] !=  "-" and board[8] !=  "-":
            row_3=int(board[6])+int(board[7])+int(board[8]) 
            if row_3 == 15:
                row_3 = True
        if row_1 == True or row_2 == True or row_3== True :
            game_working = False
            print(f"the winner is {current_player}")
            play_again = str(input("type 'Y' to play again, or type 'N' to end the game: "))
            while play_again != "Y" and play_again != "N" and play_again !="y" and play_again !="n":
                play_again = input("invaild input. type 'Y' to play again, or type 'N' to end the game. ")
            if play_again == "Y" or play_again == "y":
                    should_continue = True
            if play_again == "N" or play_again == "n":
                    should_continue = False
                    clear()
            return 
    
        
        return


    def check_columns():
        global should_continue
        global game_working
        column_1 = False
        column_2 = False
        column_3 = False


        if board[0] !=  "-" and board[3] !=  "-" and board[6] !=  "-":
            column_1=int(board[0])+int(board[3])+int(board[6]) 
            if column_1 == 15:
                column_1 = True
        if board[1] !=  "-" and board[4] !=  "-" and board[7] !=  "-":
            column_2=int(board[1])+int(board[4])+int(board[7]) 
            if column_2 == 15:
                column_2 = True
        if board[2] !=  "-" and board[5] !=  "-" and board[8] !=  "-":
            column_3=int(board[2])+int(board[5])+int(board[8]) 
            if column_3 == 15:
                column_3 = True
        if column_1 == True or column_2 == True or column_3 == True :
            game_working = False
            print(f"the winner is {current_player}")
            play_again = str(input("type 'Y' to play again, or type 'N' to end the game: "))
            while play_again != "Y" and play_again != "N" and play_again !="y" and play_again !="n":
                play_again = input("invaild input. type 'Y' to play again, or type 'N' to end the game. ")
            if play_again == "Y" or play_again == "y":
                        should_continue = True
            if play_again == "N" or play_again == "n":
                        should_continue = False
                        clear()
            return 
         
        return


    def check_diagonals():
        global should_continue
        global game_working
        diagonal_1 = False
        diagonal_2 = False
        if board[2] !=  "-" and board[4] !=  "-" and board[6] !=  "-":

            diagonal_1 = int(board[2])+int(board[4])+int(board[6])
            if diagonal_1 == 15:
                diagonal_1 = True
        if board[0] !=  "-" and board[4] !=  "-" and board[8] !=  "-":
            diagonal_2=int(board[0])+int(board[4])+int(board[8]) 
            if diagonal_2 == 15:
                diagonal_2=True

        if diagonal_1 == True or diagonal_2 == True:
            game_working = False
            print(f"the winner is {current_player}")
            play_again = str(input("type 'Y' to play again, or type 'N' to end the game: "))
            while play_again != "Y" and play_again != "N" and play_again !="y" and play_again !="n":
                play_again = input("invaild input. type 'Y' to play again, or type 'N' to end the game. ")
            if play_again == "Y" or play_again == "y":
                    should_continue = True
            if play_again == "N" or play_again == "n":
                    should_continue = False
                    clear()
            return 
      
        return
        
     
    def check_draw():
        global should_continue
        global game_working
        if "-" not in board:
            game_working=False
            print("it's draw")
            play_again = str(input("type 'Y' to play again, or type 'N' to end the game: "))
            while play_again != "Y" and play_again != "N" and play_again !="y" and play_again !="n":
                play_again = input("invaild input. type 'Y' to play again, or type 'N' to end the game. ")
            if play_again == "Y" or play_again == "y":
                    should_continue = True
            if play_again == "N" or play_again == "n":
                    should_continue = False
                    clear()
 
        return 


    def flip_player():
        global current_player
        if current_player == "odd":
            current_player = "even"
        elif current_player == "even":
            current_player = "odd"
        return

                                                                                                                  
    play_game()