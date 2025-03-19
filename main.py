from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#--------------------  CSV READING  ----------------------------------------
try:
    data_frame = pd.read_csv("data/words_to_learn.csv")
    data = data_frame.to_dict(orient="records")
except FileNotFoundError:
    data_frame = pd.read_csv("data/french_words.csv")
    data = data_frame.to_dict(orient="records")

random_choice = {}

def is_known():
    data.remove(random_choice)
    new_data = pd.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv" , index=False)
    next_card()

def next_card():
    global random_choice , flip_timer
    window.after_cancel(flip_timer)
    random_choice = random.choice(data)
    random_french_word = random_choice["French"]
    canvas.itemconfig(card_title , text="French", fill="Black")
    canvas.itemconfig(card_word , text=random_french_word, fill="Black")
    canvas.itemconfig(card, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card , image=card_back_img)
    canvas.itemconfig(card_title , text="English" , fill="White")
    canvas.itemconfig(card_word , text=random_choice["English"] , fill="White")


#--------------------  UI SETUP --------------------------------------------
window = Tk()
window.title("flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000 , flip_card)

canvas = Canvas(width=800, height=526)                  #canvas

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


right_img = PhotoImage(file="./images/right.png")       #images for button
wrong_img = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right_img , highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img , highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()


window.mainloop()