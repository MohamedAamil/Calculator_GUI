import PySimpleGUI as sg

sg.theme("LightBlue")

Num1 = 0
Num2 = 0

Check = False

Opr1 = " "
Opr2 = " "

Blue_Colour = "#03cafc"


layout = [
    [sg.Text("0" , font = ("Simplified Arabic Fixed",15) , key = 'text',pad = (30,20) ,size = (31,1) , background_color = "white" , text_color = "black")],

    [sg.Button("CE", font = ("Simplified Arabic Fixed", 15) , pad = (30 , 10), size = (5,1) , key = "Ce") ,
     sg.Button("<-", font = ("Simplified Arabic Fixed", 15) , size = (5,1) , key = "Bk") ,
     sg.Button("%", font = ("Simplified Arabic Fixed", 15) , pad = (30 , 10), size = (5,1)),
     sg.Button("/", font = ("Simplified Arabic Fixed", 15) , size = (5,1))
     ],
    [sg.Button("7", font = ("Simplified Arabic Fixed", 15) , pad = (30 , 10), size = (5,1)) ,
     sg.Button("8", font = ("Simplified Arabic Fixed", 15) , size = (5,1)) ,
     sg.Button("9", font = ("Simplified Arabic Fixed", 15) , pad = (30 , 10), size = (5,1)) ,
     sg.Button("x", font = ("Simplified Arabic Fixed", 15) , size = (5,1))
     ],
    [sg.Button("4", font=("Simplified Arabic Fixed", 15), pad=(30, 10), size=(5, 1)),
     sg.Button("5", font=("Simplified Arabic Fixed", 15), size=(5, 1)),
     sg.Button("6", font=("Simplified Arabic Fixed", 15), pad=(30, 10), size=(5, 1)),
     sg.Button("-", font = ("Simplified Arabic Fixed", 15) , size = (5,1))
     ],
    [sg.Button("1", font=("Simplified Arabic Fixed", 15), pad=(30, 10), size=(5, 1)),
     sg.Button("2", font=("Simplified Arabic Fixed", 15), size=(5, 1)),
     sg.Button("3", font=("Simplified Arabic Fixed", 15), pad=(30, 10), size=(5, 1)),
     sg.Button("+", font = ("Simplified Arabic Fixed", 15) , size = (5,1))
     ],
    [sg.Button("0", font=("Simplified Arabic Fixed", 15), pad=(30, 10) , size=(5, 1)),
     sg.Button("=", font=("Simplified Arabic Fixed", 15), pad = (10,10), size = (13, 1), key = "=", disabled = True, button_color = ("white", Blue_Colour))
     ],

    [sg.Image("Creator.png", size = (450,400),pad = (0,5))]
]

def add_number(event):
    global Num1
    if Num1 < 10**29:
        Num1 = Num1*10 + int(event)
        window.FindElement("text").Update(Num1)


def set_opr(event):
    global Opr1,Opr2,Num2, Num1,Check
    window.FindElement("=").Update(disabled=False)
    Opr2 = Opr1
    Opr1 = event
    if Check:
        calculate()
    if not Check:
        window.FindElement("text").Update(Num1)
        Num2 = Num1
        Num1 = 0
        Opr2 = event
    Check = True


def calculate():
    global Num2,Num1,Opr2,Opr1

    if Opr2 == "+":
        Num2 += Num1
    if Opr2 == "-":
        Num2 -= Num1
    if Opr2 == "x":
        Num2 *= Num1
    try:
        if Opr2 == "/":
            Num2 /= Num1
        Num1 = 0
        if Num2 < 10**29:
            window.FindElement("text").Update(Num2)
        else:
            print("g")
            clear_screen()
            window.FindElement("text").Update("Error")


    except ZeroDivisionError:
        window.FindElement("text").Update("Error")

def clear_screen():
    global Opr1,Opr2,Num2, Num1,Check
    Num1, Num2 = 0, 0
    Opr1, Opr2 = " ", " "
    window.FindElement("=").Update(disabled=True)



window = sg.Window("Calculator", layout , size = (450,450))

Numbers = ["1","2","3","4","5","6","7","8","9","0"]
Operators = ["+","-","x","/","%"]

while True:
    events,values = window.Read()

    if events in Numbers:
        add_number(events)

    if events in Operators:
        set_opr(events)
    if events == "%" and Opr2 == "x":
        set_opr(" ")
        Num2 = Num2/100
        window.FindElement("text").Update(Num2)
        window.FindElement("=").Update(disabled=True)

    if events == "=":
        set_opr(" ")
        window.FindElement("=").Update(disabled = True)

    if events == "Ce":
        clear_screen()
        Check = False
        window.FindElement("text").Update("0")

    if events == "Bk":
        if Num1!= 0:
            Num1 = Num1 //10
            window.FindElement("text").Update(Num1)

    if events == sg.WINDOW_CLOSED:
        break

window.Close()