BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random


# --------- function to randomly pick word -------- #
words = {}
def click():
    global words, flip_timer
    words = random.choice(df)
    fr_word = words['French']
    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(word, text=fr_word, fill="black")
    canvas.itemconfig(background, image=card_front)
    flip_timer = tk.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(background,image=card_back)
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=words['English'],fill="white")

def click_right():
    global words, flip_timer
    tolearn.remove(words)
    print(tolearn)
    pd.DataFrame(tolearn).to_csv("data/tolearn.csv",index=False)
    words = random.choice(df)
    fr_word = words['French']
    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(word, text=fr_word, fill="black")
    canvas.itemconfig(background, image=card_front)
    flip_timer = tk.after(3000, flip_card)



# ------------- UI Setup ------------------#
tk = Tk()
tk.title("Flashy")
tk.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = tk.after(3000, flip_card)

# --import pictures -- #
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
button_right = PhotoImage(file="./images/right.png")
button_wrong = PhotoImage(file="./images/wrong.png")

# -- Canvas setup -- #
canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(400,263,image=card_front)
title = canvas.create_text(400,150, text="title", font=("Arial",40,"italic"))
word = canvas.create_text(400,263, text="word", font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

# -- Add Buttons -- #
wrong_button = Button(image=button_wrong,bg=BACKGROUND_COLOR,command=click)
wrong_button.grid(column=0,row=1)

right_button = Button(image=button_right,highlightthickness=0,command=click_right)
right_button.grid(column=1,row=1)

# ---------- import Data  ------------#
try:
    word_data = pd.read_csv("data/tolearn.csv")
except FileNotFoundError:
    word_data = pd.read_csv("./data/french_words.csv")

df = pd.DataFrame(word_data).to_dict(orient="records")
tolearn = df


click()


tk.mainloop()