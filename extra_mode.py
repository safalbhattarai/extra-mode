words = ["Supercalifragilistice" , "expialidocious" , "Antidisestablishment" , "arianism" , "Floccinaucinihilipilificate" , "Honorificabilitation" , "Incomprehensibilities" , "Unconstitutionalities" , "Discombobulating" , "Unpredictabilities" , "Circumlocution" , "Antiphospholipid" , "Disproportionateness" , "Perfidiousness" , "Orthogonalization" , "Extraterrestrial" , "Flabbergasted"]

def timer():
    global timeleft
    global score
    global wrong
    if (timeleft>11):
        pass
    else:
        timer_count.config(fg="red")
    
    if (timeleft > 0):
        timeleft = timeleft - 1
        timer_count.config(text=timeleft)
        timer_count.after(1000 , timer) #1k minisec(ms) = 1sec 
        # after function continuos calling in every 1 sec
    else:
        word_entry.config(state=DISABLED)
        game_detail_label.config(text="Words = {} | Wrong = {} | WPM = {} ".format(score,wrong,score-wrong))
        notification = messagebox.askretrycancel("Restart Game" , "Do you like to Restart Game ?")
        if (notification==TRUE):
            score = 0
            timeleft = 60
            count = 0
            wrong = 0
            timer_count.config(text=timeleft)
            word_label.config(text=words[0])
            score_count.config(text=score)
            word_entry.config(state=NORMAL)
            word_entry.delete(0 , END)


def start_game(event):
    global score
    global wrong
    if (timeleft==60):
        timer()
    game_detail_label.config(text="")
    
    if word_entry.get() == word_label["text"]:
        score = score + 1
        score_count.config(text=score)
        # print(f"score = {score}")
    else:
        wrong = wrong + 1
        # print(f"wrong = {wrong}")
    random.shuffle(words)
    word_label.config(text=words[0])
    word_entry.delete(0 , END)




from tkinter import *
from PIL import ImageTk , Image
import random
from tkinter import messagebox



random.shuffle(words)

game = Tk()
game.geometry("1450x670+50+60")
game.config(bg="grey80")
game.title("extra mode games")
game.resizable(0,0)

bg_image = Image.open("extra.jpg")
bg_image = bg_image.resize((1450,670))
bck_end_img = ImageTk.PhotoImage(bg_image)

lbl = Label(game , image=bck_end_img)
lbl.place(x=0 , y=0)

score = 0
timeleft = 60
count = 0
wrong = 0


word_label_frame = Frame(game , width=490 , height=80 , bg="black")
word_label_frame.place(x=500 , y=350)

word_label = Label(word_label_frame , text=words[0] , font="monospace 30 bold" , fg="white" , bg="black")
word_label.place(x=28 , y=15)

word_entry = Entry(game  , font="monospace 30 bold" , fg="black" , bg="white" , bd=15 , justify="center" , show="*")
word_entry.place(x=500 , y=460)
word_entry.focus()

score_label = Label(game , text="Your Score : " , font="monospace 25 bold" , fg="white" , bg="black")
score_label.place(x=30 , y=80)

score_count = Label(game , text="0" , font="monospace 25 bold" , fg="white" , bg="black")
score_count.place(x=120 , y=150)

timer_laber = Label(game , text="Time Left : " , font="monospace 25 bold" , fg="white" , bg="black")
timer_laber.place(x=1200 , y=80)

timer_count = Label(game , text="60" , font="monospace 25 bold" , fg="white" , bg="black")
timer_count.place(x=1250 , y=150)

game_detail_label = Label(game , text="Type Word and Hit Enter" , font="monospace 30 italic bold" , fg="dark grey" , bg="black")
game_detail_label.place(x=480 , y=590)

game.bind("<Return>" , start_game)

game.mainloop()