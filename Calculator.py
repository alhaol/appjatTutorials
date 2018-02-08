# import the library
from appJar import gui

# handleing 

def press(name):
    if name=='Exit':
        app.stop()
    else:
        try:
            firstNum=int(app.getEntry('first'))
            secondNum=int(app.getEntry('second'))
            message="Results are as follows : \n\n"
            message+="Addition:"+str(firstNum+secondNum) +"\n"
            message+="Subtraction:"+str(firstNum-secondNum) +"\n"
            message+="Multiplication:"+str(firstNum*secondNum) +"\n"
            message+="Division:"+str(firstNum/float(secondNum)) +"\n"
            if name=="Result":
                app.setLabel("Result",message)
            elif name=="MessageBox Results":
                app.infoBox('Result',message)

        except ValueError as e:
            app.errorBox("Error","Invalid Number")
            app.setFocus('first')


# create a GUI variable called app
app = gui("Calculator")
# adding 2 labels % buttons with column row specification 
app.addLabel('fn','First Number',0,0)
app.addEntry('first',0,1)
app.addLabel('sn','Second Number',0,2)
app.addEntry('second',0,3)
app.setFocus('first')

# Formating  (streching 4 columns) 
app.addEmptyLabel("Result",1,0,4)
# Format the label 
app.setLabelRelief('Result',app.GROOVE)
app.setLabelAlign('Result',app.NW)
app.setLabelHeight('Result',8)

# add the buttons 
app.addButtons(["Result","MessageBox Results","Exit"],press,2,0,4)

# start the GUI
app.go()