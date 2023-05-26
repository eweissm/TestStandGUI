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

ManualFrame = tkinter.Frame(master=tkTop,width=600, bg="red")
ManualLable = tkinter.Label(master= ManualFrame, text = 'Manual Controls',font=("Courier", 12,'bold')).pack() #manual controls lable

AutoFrame = tkinter.Frame(master=tkTop,width = 600, bg="blue")
AutoLable = tkinter.Label(master= AutoFrame, text = 'Automated Controls',font=("Courier", 12,'bold')).pack() #Austomated controls lable


ManualFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
AutoFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

LeftButtonsFrame = tkinter.Frame(master=ManualFrame,width = 100, bg="green")
LeftButtonsLable = tkinter.Label(master= LeftButtonsFrame, text = 'Left Side Controls',font=("Courier", 12,'bold')).pack()

RightButtonsFrame = tkinter.Frame(master=ManualFrame,width = 100, bg="yellow")
RightButtonsLable = tkinter.Label(master= RightButtonsFrame, text = 'Right Side Controls',font=("Courier", 12,'bold')).pack()

button_up_left = tkinter.IntVar()
button_up_left_state = tkinter.Button(LeftButtonsFrame,
    text="Up",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_up_left_state.pack(side='top', ipadx=10, padx=10, pady=15)

button_down_left = tkinter.IntVar()
button_down_left_state = tkinter.Button(LeftButtonsFrame,
    text="Down",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_down_left_state.pack(side='top', ipadx=10, padx=10, pady=15)

button_up_right = tkinter.IntVar()
button_up_right_state = tkinter.Button(RightButtonsFrame,
    text="Up",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_up_right_state.pack(side='top', ipadx=10, padx=10, pady=15)

button_down_right = tkinter.IntVar()
button_down_right_state = tkinter.Button(RightButtonsFrame,
    text="Down",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_down_right_state.pack(side='top', ipadx=10, padx=10, pady=15)

LeftButtonsFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
RightButtonsFrame.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

tkinter.mainloop()