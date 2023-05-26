import serial
import time
import tkinter


def quit():
    global tkTop
    #ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def set_button1_state():
        global b
        b += 1
        varLabel.set("LED ON ")
       # ser.write(bytes('H', 'UTF-8'))
        varLabel2.set(b)
        print(b)

def set_button2_state():
        varLabel.set("LED OFF")
       #ser.write(bytes('L', 'UTF-8'))

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
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_left_state.pack(side='top', ipadx=10, padx=10, pady=40)

button_right_state = tkinter.Button(LeftButtonsFrame,
    text="Right",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_right_state.pack(side='top', ipadx=10, padx=10, pady=40)

button_both_state = tkinter.Button(LeftButtonsFrame,
    text="Both",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_both_state.pack(side='top', ipadx=10, padx=10, pady=40)

button_up_state = tkinter.Button(RightButtonsFrame,
    text="Up",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_up_state.pack(side='top', ipadx=10, padx=10, pady=40)

button_down_state = tkinter.Button(RightButtonsFrame,
    text="Down",
    command=set_button1_state,
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
AutoFrame = tkinter.Frame(master=tkTop,width = 600, bg="blue")
AutoLable = tkinter.Label(master= AutoFrame, text = 'Automated Controls',font=("Courier", 12,'bold')).pack(side='top', ipadx=10, padx=10, pady=40) #Automated controls lable

button_Automated_on_off = tkinter.Button(AutoFrame,
    text="Turn Automated Controls on/off",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 25,
    bd = 5,
    activebackground='green'
)
button_Automated_on_off.pack(side='top', ipadx=0, padx=0, pady=0)


TargetHeightLable = tkinter.Label(master= AutoFrame, text = 'Enter Target Height: ',font=("Courier", 12)).pack(side='left', ipadx=10, padx=10, pady=40) #Automated controls lable
TargetHeightEntry = tkinter.Entry(AutoFrame)
TargetHeightEntry.pack(side='left', ipadx=0, padx=0, pady=0)



AutoFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

tkinter.mainloop()