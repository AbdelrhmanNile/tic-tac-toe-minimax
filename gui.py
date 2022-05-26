from tkinter import *
from tkinter import messagebox
import xo
import trigger



root = Tk()
# root.title('Codemy.com - Tic-Tac-Toe')
# root.iconbitmap('c:/gui/codemy.ico')
# root.geometry("1200x710")

# X starts so true
clicked = True
count = 0


# disable all the buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def enable_all_buttons():
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)
    b8.config(state=NORMAL)
    b9.config(state=NORMAL)


# Check to see if someone won
def checkifwon():
    global winner
    winner = False

    if xo.checkWin()[0] == True:
        indxs = xo.checkWin()[2]
        for i in range(3):
            btn[indxs[i]].config(bg="red")

        winner = True
        if xo.checkWin()[1] == "X":
            messagebox.showinfo("Tic Tac Toe", "Ai Wins!!")
        else:
            messagebox.showinfo("Tic Tac Toe", "Player Wins!!")
        disable_all_buttons()
        return True

    # Check if tie
    if xo.checkDraw():
        messagebox.showinfo("Tic Tac Toe", "It's A Draw!\n No One Wins!")
        disable_all_buttons()
        return False


# Button clicked function
def b_click(b, i):
    global clicked, count

    if b["text"] == " " and clicked == True:
        playerMoveGUI(i)
        clicked = False
        count += 1
        if checkifwon():
            exit()
        else:
            aiMoveGui()
            checkifwon()
    elif b["text"] == " " and clicked == False:
        playerMoveGUI(i)
        clicked = True
        count += 1
        if checkifwon():
            exit()
        else:
            aiMoveGui()
            checkifwon()
    else:
        messagebox.showerror(
            "Tic Tac Toe",
            "Hey! That box has already been selected\nPick Another Box...",
        )


def startClick(btn0):
    enable_all_buttons()
    aiMoveGui()
    btn0.config(state=DISABLED)
    clicked = False
    global count
    count += 1


def getPos(index):
    return xo.board[index]


# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b0
    global clicked, count
    clicked = True
    count = 0

    # Build our buttons
    b1 = Button(
        root,
        text=getPos(1),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=1: b_click(b1, i),
        name="1",
    )
    b2 = Button(
        root,
        text=getPos(2),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=2: b_click(b2, i),
        name="2",
    )
    b3 = Button(
        root,
        text=getPos(3),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=3: b_click(b3, i),
        name="3",
    )

    b4 = Button(
        root,
        text=getPos(4),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=4: b_click(b4, i),
        name="4",
    )
    b5 = Button(
        root,
        text=getPos(5),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=5: b_click(b5, i),
        name="5",
    )
    b6 = Button(
        root,
        text=getPos(6),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=6: b_click(b6, i),
        name="6",
    )

    b7 = Button(
        root,
        text=getPos(7),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=7: b_click(b7, i),
        name="7",
    )
    b8 = Button(
        root,
        text=getPos(8),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=8: b_click(b8, i),
        name="8",
    )
    b9 = Button(
        root,
        text=getPos(9),
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="black",
        command=lambda i=9: b_click(b9, i),
        name="9",
    )

    b0 = Button(
        root,
        text="start",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="blue",
        command=lambda i=0: startClick(b0),
    )

    global btn
    btn = {1: b1, 2: b2, 3: b3, 4: b4, 5: b5, 6: b6, 7: b7, 8: b8, 9: b9}

    # Grid our buttons to the screen
    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)
    b0.grid(row=0, column=1)
    disable_all_buttons()





def updatePos():
    b1["text"] = getPos(1)
    b2["text"] = getPos(2)
    b3["text"] = getPos(3)
    b4["text"] = getPos(4)
    b5["text"] = getPos(5)
    b6["text"] = getPos(6)
    b7["text"] = getPos(7)
    b8["text"] = getPos(8)
    b9["text"] = getPos(9)


def aiMoveGui():
    xo.aiMove()
    updatePos()


def playerMoveGUI(i):
    xo.playerMove(int(i))
    updatePos()

def play_again():
    reset()
    for key in xo.board:
        xo.board[key] = " "
    trigger.first = True
    updatePos()


# Create menue
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=lambda: play_again())

reset()

root.mainloop()
