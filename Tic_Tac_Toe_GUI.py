from tkinter import *
from tkinter import messagebox
#Creating main window here
root = Tk()
root.title("Tic Tac Toe")

count = 0
winner = False

#Function for taking location of player click for backend process
def which_button(m):
    if m=="b1":
        board[1] = "X"
    elif m== "b2":
        board[2] = "X"
    elif m== "b3":
        board[3] = "X"
    elif m== "b4":
        board[4] = "X"
        print(board[4])
    elif m== "b5":
        board[5] = "X"
    elif m== "b6":
        board[6] = "X"
    elif m== "b7":
        board[7] = "X"
    elif m== "b8":
        board[8] = "X"
    elif m== "b9":
        board[9] = "X"

#Function for disabling all buttons, to be used after the game is over
def disablebuttons():
    b1.config(state= DISABLED)
    b2.config(state= DISABLED)
    b3.config(state= DISABLED)
    b4.config(state= DISABLED)
    b5.config(state= DISABLED)
    b6.config(state= DISABLED)
    b7.config(state= DISABLED)
    b8.config(state= DISABLED)
    b9.config(state= DISABLED)


#function for clicking buttons and taking in bot move
def buttonclick(b):
    global count
    #taking in user input according to button(b) be clicked on grid
    if b["text"] ==  " ":
        b["text"] = "X"
        count+=1
        checkforwin()
        #taking in bot move from minimax algorithm through compMove() function
        bot = compMove()
        if bot == 1:
            b1["text"] = "O"
        elif bot == 2:
            b2["text"] = "O"
        elif bot == 3:
            b3["text"] = "O"
        elif bot == 4:
            b4["text"] = "O"
        elif bot == 5:
            b5["text"] = "O"
        elif bot == 6:
            b6["text"] = "O"
        elif bot == 7:
            b7["text"] = "O"
        elif bot == 8:
            b8["text"] = "O"
        elif bot == 9:
            b9["text"] = "O"
        count+=1
        checkforwin()
    
    else:
        messagebox.showerror("ERROR", "The chosen box has already been chosen. Please choose another box.")

#Function for checking winner of the current round and also checks if it is a draw
def checkforwin(): 
    global winner
    if  b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "lightgreen")
        b2.config(bg = "lightgreen")
        b3.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b6.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()
    elif  b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "lightgreen")
        b8.config(bg = "lightgreen")
        b9.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()
    elif  b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "lightgreen")
        b4.config(bg = "lightgreen")
        b7.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()
    elif  b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b8.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()
    elif  b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "lightgreen")
        b6.config(bg = "lightgreen")
        b9.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()
    elif  b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b9.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b7.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "X wins!!!")
        disablebuttons()

    

    elif  b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "lightgreen")
        b2.config(bg = "lightgreen")
        b3.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b6.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()
    elif  b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = "lightgreen")
        b8.config(bg = "lightgreen")
        b9.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()
    elif  b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = "lightgreen")
        b4.config(bg = "lightgreen")
        b7.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()
    elif  b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b8.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()
    elif  b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "lightgreen")
        b6.config(bg = "lightgreen")
        b9.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()
    elif  b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b9.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "lightgreen")
        b5.config(bg = "lightgreen")
        b7.config(bg = "lightgreen")
        winner = True
        messagebox.showinfo("Game Ends", "O wins!!!")
        disablebuttons()
    if count == 9 and winner == False:
        messagebox.showinfo("Game Ends", "It is a draw.")
        disablebuttons()


#Building buttons for GUI window

b1 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="lightblue", command=lambda m="b1": [which_button(m),buttonclick(b1)])
b2 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="cyan", command=lambda m="b2": [which_button(m),buttonclick(b2)])
b3 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="lightblue", command=lambda m="b3": [which_button(m),buttonclick(b3)])
b4 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="cyan", command=lambda m="b4": [which_button(m),buttonclick(b4)])
b5 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="lightblue", command=lambda m="b5": [which_button(m),buttonclick(b5)])
b6 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="cyan", command=lambda m="b6": [which_button(m),buttonclick(b6)])
b7 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="lightblue", command=lambda m="b7": [which_button(m),buttonclick(b7)])
b8 = Button(root, text= " ", font = ("Arial", 20), height = 3, width= 6 ,bg="cyan", command=lambda m="b8": [which_button(m),buttonclick(b8)])
b9 = Button(root, text= " ", font = ("Arial", 20), height= 3, width= 6 , bg="lightblue", command=lambda m="b9": [which_button(m),buttonclick(b9)])

#placing buttons in GUI Window
b1.grid(row= 0, column= 0)
b2.grid(row= 0, column= 1)
b3.grid(row= 0, column= 2)
b4.grid(row= 1, column= 0)
b5.grid(row= 1, column= 1)
b6.grid(row= 1, column= 2)
b7.grid(row= 2, column= 0)
b8.grid(row= 2, column= 1)
b9.grid(row= 2, column= 2)


#function for taking bot move through minimax algorithm, returns the index for next move which is interpreted in button_click(b) for showing it in the GUI window
def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = "O"
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    board[bestMove] = "O"
    return bestMove


#This function implements Minimax Algorithm in the program. Minimax algorithm considers two players as maximizer and minimzer. Minimizer tries to get the mimnimum score for it's next step and Maximizer tries to get the maximum score possible in a given instance.
#Maximizer takes the move with highest value possible and minimizer takes the move with lowest value possible. The function simulates a complete round and finds the best move possible.
def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon("O")):
        return 1
    elif (checkWhichMarkWon("X")):
        return -1
    elif (checkDraw()):
        return 0

    #we are considering the bot here as Maximizer in this condition and alternatively changing the value for is Maxmizing to True and False so that both maximizer and minimizer play alternative turns for the simulation of the match. We are searching for the maximum score here in this condition.
    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = "O"
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                #finding highest score here in this conditon
                if (score > bestScore):
                    bestScore = score
        return bestScore

    #we are considering the player here as Minimiser in this condition and alternatively changing the value for isMaxmizing to True and False so that both maximizer and minimizer play alternative turns for the simulation of the match. We are searching for the minimum score here in this condition.
    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = "X"
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                #finding the minimum score here in this condition
                if (score < bestScore):
                    bestScore = score
        return bestScore    


#function for checking winner in simulation for minimax function
def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


#function for checkng draw in simulation for minimax function
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

            

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}



root.mainloop()