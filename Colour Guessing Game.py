from tkinter import *
import random
import tkinter
from tkinter import messagebox, ttk

colors = ["Red", "orange", "yellow", "green", "blue", "pink", "purple", "brown", "black", 'White']
score = 0
timeleft = 60


def startGame():
    if timeleft == 60:
        countdown()
    nextcolour()


def countdown():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo("time over", "time is over and your score is=" + str(score))
    if timeleft > 0:
        timeleft -= 1
        timeLable.config(text="Time lable:" + str(timeleft))
        timeLable.after(1000, countdown)


def nextcolour():
    global score
    global timeleft

    if timeleft > 0:
        entry.focus_set()
        if entry.get().lower() == colors[1].lower():
            score += 1
            timeleft += 5

        entry.delete(0, END)
        random.shuffle(colors)

        label.config(fg=str(colors[1]), text=str(colors[0]),bg=str(colors[2]))
        scoreLabel.config(text="score:" + str(score), bg="cyan")


root = Tk()
root.title('Word guessing game')
root.geometry("400x400")
root.resizable(0, 0)

instruction = Label(root, text="Type the color of the word,and not the word text", font=('Helvetica', 12),bg="cyan")
instruction.pack(padx=25, pady=10)

scoreLabel = Label(root, text="Press ENTER to start", font=('Helvetica', 12),bg="cyan")
scoreLabel.pack(padx=25, pady=10)

timeLable = Label(root, text="Time left:" + str(timeleft), font=('Helvetica', 12),bg="cyan")
timeLable.pack(padx=25, pady=10)

label = Label(root, font=('Helvetica', 80))
label.pack(padx=0, pady=10)

entry = Entry(root,)
root.bind('<Return>', lambda event: startGame())
entry.pack()
entry.focus_set()

btn = ttk.Button(root, text="Press Enter to Start", command=startGame)
btn.pack(padx=25, pady=20)

root.mainloop()
