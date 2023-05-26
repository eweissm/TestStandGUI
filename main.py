import serial
import time
import tkinter




def set_ActuatorSelection_left_state():
    global ActuatorSelection_state
    ActuatorSelection_state = 0
    ActuatorSelectionLabel.set("Left")

def set_ActuatorSelection_right_state():
    global ActuatorSelection_state
    ActuatorSelection_state = 1
    ActuatorSelectionLabel.set("Right")

def set_ActuatorSelection_both_state():
    global ActuatorSelection_state
    ActuatorSelection_state = 2
    ActuatorSelectionLabel.set("Both")


def set_Automated_Controls_state():
    global Automated_Controls_state
    if Automated_Controls_state == 1:
        Automated_Controls_state = 0
        varLabel.set("Automated Controls: Off ")
    else:
        Automated_Controls_state = 1
        varLabel.set("Automated Controls: On ")



Automated_Controls_state = 0


#ser = serial.Serial('com5', 9600)
#print("Reset Arduino")
#time.sleep(3)
#ser.write(bytes('L', 'UTF-8'))


tkTop = tkinter.Tk() # Create GUI Box
tkTop.geometry('1200x800') #size of GUI

tkTop.title("Test Stand Controller") #title in top left of window

Title = tkinter.Label(text = 'Test Stand Controls',font=("Courier", 14,'bold')).pack() #Title on top middle of screen


# Fill in the Manual controls Side----------------------------------------------------------------------------------------------------------------------------------------
ManualFrame = tkinter.Frame(master=tkTop,width=600)
ManualLable = tkinter.Label(master= ManualFrame, text = 'Manual Controls',font=("Courier", 12,'bold')).pack() #manual controls lable
ManualFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

LeftButtonsFrame = tkinter.Frame(master=ManualFrame,width = 100)
LeftButtonsLable = tkinter.Label(master= LeftButtonsFrame, text = 'Actuator Selection',font=("Courier", 12,'bold')).pack()

RightButtonsFrame = tkinter.Frame(master=ManualFrame,width = 100)
RightButtonsLable = tkinter.Label(master= RightButtonsFrame, text = 'Up/Down Controls',font=("Courier", 12,'bold')).pack()


button_left_state = tkinter.Button(LeftButtonsFrame,
    text="Left",
    command=set_ActuatorSelection_left_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_left_state.pack(side='top', ipadx=10, padx=10, pady=40)

button_right_state = tkinter.Button(LeftButtonsFrame,
    text="Right",
    command=set_ActuatorSelection_right_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_right_state.pack(side='top', ipadx=10, padx=10, pady=40)

button_both_state = tkinter.Button(LeftButtonsFrame,
    text="Both",
    command=set_ActuatorSelection_both_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_both_state.pack(side='top', ipadx=10, padx=10, pady=40)


ActuatorSelectionLabel = tkinter.IntVar()
ActuatorSelection = tkinter.Label(master= LeftButtonsFrame, textvariable=ActuatorSelectionLabel )
ActuatorSelection.pack()


button_up_state = tkinter.Button(RightButtonsFrame,
    text="Up",
    command=set_ActuatorSelection_both_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_up_state.pack(side='top', ipadx=10, padx=10, pady=40)

button_down_state = tkinter.Button(RightButtonsFrame,
    text="Down",
    command=set_ActuatorSelection_both_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_down_state.pack(side='top', ipadx=10, padx=10, pady=40)

LeftButtonsFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
RightButtonsFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

# Fill in the Automated controls Side----------------------------------------------------------------------------------------------------------------------------------------
AutoFrame = tkinter.Frame(master=tkTop,width = 600, bg="gray")
AutoLable = tkinter.Label(master= AutoFrame, text = 'Automated Controls',font=("Courier", 12,'bold'), bg="gray").pack(side='top', ipadx=10, padx=10, pady=40) #Automated controls lable

button_Automated_on_off = tkinter.Button(AutoFrame,
    text="Turn Automated Controls on/off",
    command=set_Automated_Controls_state,
    height = 4,
    fg = "black",
    width = 25,
    bd = 5,
    activebackground='green'
)
button_Automated_on_off.pack(side='top', ipadx=0, padx=0, pady=0)

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(master= AutoFrame, textvariable=varLabel, bg="gray" )
tkLabel.pack()


TargetHeightLable = tkinter.Label(master= AutoFrame, text = 'Enter Target Height: ',font=("Courier", 12), bg="gray").pack(side='left', ipadx=10, padx=10, pady=40) #Automated controls lable
TargetHeightEntry = tkinter.Entry(AutoFrame)
TargetHeightEntry.pack(side='left', ipadx=0, padx=0, pady=0)

AutoFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

TargetHeight = TargetHeightEntry.get()

tkinter.mainloop()