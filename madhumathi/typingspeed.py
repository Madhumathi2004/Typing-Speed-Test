words = ['Accumulate','characteristics','complex','Proportion','INTERPRET','Isolate','illustrate',
         'Auxiliary','substitute','composition','fundamental','EXERCISE','Equipment','Peripheral','INTERNET']

def labelSlider():
    global count,sliderWords
    text = 'Welcome to typing Speed Increaser game'
    if(count>= len(text)):
        count= 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,labelSlider)

def time():
    global timeleft,score,miss
    if(timeleft>=11):
        pass    
    else:
        timeLabelCount.configure(fg = 'red')
    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.configure(text = timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='hit = {} | Miss = {} | Total Score == {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('notification','For play Again Hit Retry Button')
        if(rr == True):
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text = timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):
    global score,miss
    if(timeleft == 60):
       time()

    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get()==wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text= score)
        
    else:
        miss += 1
        print('miss',miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

from tkinter import *
import random
from tkinter import messagebox

######Root method
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='black')
root.title('Typing speed Increaser game')
root.iconbitmap('typinglogo_XxT_icon.ico')

#######variables
score=0
timeleft = 60
count = 0
sliderWords = ''
miss = 0

#######label methods
fontLabel = Label(root,text = '',font = ('airal',25,'italic bold'),bg = 'black',fg='white')
fontLabel.place(x=80,y=10)
labelSlider()
random.shuffle(words)

wordLabel = Label(root,text= words[0], font=('airal',40,'normal'),bg='black',fg='white')
wordLabel.place(x=300,y=200)

scoreLabel= Label(root,text = 'Your Score:',font=('airal',25,'italic bold'),bg = 'black',fg= 'white')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text='0',font=('airal',25,'italic bold'),bg='black',fg = 'white')
scoreLabelCount.place(x=80,y=180)

timerLable = Label(root,text = 'Time Left:',font=('airal',25,'italic bold'),bg = 'black',fg= 'white')
timerLable.place(x=600,y=100)

timeLabelCount = Label(root,text = timeleft,font=('airal',25,'italic bold'),bg = 'black',fg = 'white')
timeLabelCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',font=('arial',30,'italic bold'),bg='black',fg='red')
gamePlayDetailLabel.place(x=120,y=450)
 
#######Entry method
wordEntry = Entry(root,font=('arial',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()
###############################################
root.bind('<Return>',startGame)
root.mainloop()
