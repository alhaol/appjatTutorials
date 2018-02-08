# import the library
from appJar import gui
import random
# list of answers 
answers=['Are you sure', 'This is interesting', 'Pick again']
# handle button events
def shake(name):
    global answers
    tempAns=app.getEntry("Question")
    Nspaces=tempAns.split(' ')
    if len(app.getEntry("Question"))==0:
        app.errorBox("Error","You must ask a Question")
    elif ((len(Nspaces)>=3) & ((Nspaces[0]=='who') | (Nspaces[0]=='what'))) :
        #app.playSound('buzz.wav')
        answer=random.choice(answers)
        app.setLabel("Answer",answer)
    else:
        app.errorBox("Error","You queation should have 3 spaces and start with who or what")

def clear(name):
    app.clearEntry("Question")
    app.clearLabel("Answer")
# create a GUI variable called app
app = gui("Magic 8 Ball",geom="300x400")
app.setResizable(False)
app.setBg("gray")
app.setFont(18)

# Add the 4 rows of widgets 
app.addEntry("Question")
app.addButtons(["shake","Clear"],[shake,clear])
app.addImage("8ball","8-ball.gif")
app.addEmptyLabel("Answer")
app.setLabelBg('Answer','Yellow')

# Little configuration
app.setFocus("Question")
# start the GUI
app.go()