
# coding: utf-8

# In[1]:

# import the library
from appJar import gui

# handle button events
def press(button):
    if button == "Exit":
        app.stop()
    if button=="ON":
        app.setImage('Light','images/ON.gif')

    if button=="OFF":
        app.setImage('Light', 'images/OFF.gif')

# create a GUI variable called app
app = gui("Lights", "400x400")
app.setBg("gray")
app.setFont(18)

# link the buttons to the function called press
app.addImage('Light','images/OFF.gif')
app.addButtons(["ON", "OFF"], press)
app.addButton('Exit',press)

# start the GUI
app.go()


# In[2]:

get_ipython().system(u'jupyter --nbconvert to script ON_OFF.ipynb')


# In[ ]:



