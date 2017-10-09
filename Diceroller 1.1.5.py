import tkinter as tk
import random
import sys
import operator
txt="Welcome to our diceroller!"
def button1():
    global ent
    button.destroy()
    ent.pack()
    lbl.configure(text="Enter the dice you want to roll")
    but2 = tk.Button(window, text="Enter", command=diceroller)
    but2.pack()
def resshower():
    dice = int(roll[d + 1:o])
    mod = int(roll[o + 1:])
    numb = int(roll[:d])
    results = []
    for i in range(numb):
        droll = random.randint(1, dice)
        results.append(droll)
    subtotal = sum(results)
    oper = ops[op]
    final = oper(subtotal, mod)
    equal = "="
    outp = ("%(res)r %(op)r %(mod)r %(equal)r %(final)r" % 
    {'res' : results, 'op' : op, 'mod' : mod, 'equal' : equal, 'final' : final})
 
    lbl.configure(text=outp)

def diceroller():
    global roll, d, o, op, ops
    roll = ent.get()
    roll = roll.lower()

    ops = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod}
    d = roll.find("d")
    if d == True:
        d = roll.find("d")


    else:
        lbl.configure(text="""Not a valid format. Please use the following format:
        (Number of Dice)d(Number of Faces)(Operator(Optional))(Modifier)
        ex. 2d6+3
        """)

    
    if roll.find("+") != -1:
        o = roll.find("+")
        op = "+"
        resshower()

    elif roll.find("-") != -1:
        o = roll.find("-")
        op = "-"
        resshower()

    elif roll.find("*") != -1:
        o = roll.find("*")
        op = "*"
        resshower()


    elif roll.find("/") != -1:
        o = roll.find("/")
        op = "/"
        resshower()

    elif roll.find("%") != -1:
        o = roll.find("%")
        op = "%"
        resshower()

    else:
        dice = int(roll[d + 1:])
        numb = int(roll[:d])

        results = []
        for i in range(numb):
            droll = random.randint(1, dice)
            results.append(droll)
        subtotal = sum(results)
        outp = results," = ", subtotal
        lbl.configure(text=outp)

    
window = tk.Tk()
window.geometry("300x100")
window.title("Diceroller")
window.wm_iconbitmap("favicon.ico")
lbl=tk.Label(window, text=txt)
ent = tk.Entry(window)
    
button = tk.Button(window, text="Click here to begin",
    command=button1)
lbl.pack()
button.pack()
window.mainloop()

