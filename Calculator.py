from tkinter import*
 
window = Tk()
window.title("Calculator")
txt_Input = StringVar()
operator = ""

def btnClick(num):
    global operator
    operator = operator + str(num)
    txt_Input.set(operator)


def btnClear():
    global operator
    operator = ""
    txt_Input.set("")


def btnEquals():
    global operator
    try:
        operator = str(eval(operator))
        txt_Input.set(operator)
    except:
        txt_Input.set("ERROR")
 

display = Entry(window, bg = "lightgrey", bd = 15, insertwidth = 3, width = 20,font = ("arial", 25, "bold"), 
                textvariable = txt_Input, justify = RIGHT).grid(columnspan=4)

btnAC = Button(window,bg = "lightgrey", bd = 15, text = "AC", font = ("arial", 18, "bold"), width = 23, padx = 5, command = btnClear).grid(row = 1, columnspan = 4, sticky = W)
        
btn7 = Button(window, bg = "lightgrey", bd = 15,text = "7", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(7)).grid(row = 2, column = 0, sticky = W)
btn8 = Button(window, bg = "lightgrey", bd = 15,text = "8", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(8)).grid(row = 2, column = 1, sticky = W)
btn9 = Button(window, bg = "lightgrey", bd = 15,text = "9", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(9)).grid(row = 2, column = 2, sticky = W)
btndiv = Button(window, bg = "lightgrey", bd =15,text = "/", padx = 20, pady = 17, font = ("arial", 15, "bold"),command = lambda:btnClick("/")).grid(row = 2, column = 3, sticky = W)


btn4 = Button(window, bg = "lightgrey", bd = 15,text = "4", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(4)).grid(row = 3, column = 0, sticky = W)
btn5 = Button(window, bg = "lightgrey", bd = 15,text = "5", padx = 20, pady = 17, font = ("arial", 15, "bold"),command = lambda:btnClick(5) ).grid(row = 3, column = 1, sticky = W)
btn6 = Button(window, bg = "lightgrey", bd = 15,text = "6", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(6)).grid(row = 3, column = 2, sticky = W)
btnadd = Button(window, bg = "lightgrey", bd = 15,text = "+", padx = 18, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick("+")).grid(row = 3, column = 3, sticky = W)



btn1 = Button(window, bg = "lightgrey", bd = 15,text = "1", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(1)).grid(row = 4, column = 0, sticky = W)
btn2 = Button(window, bg = "lightgrey", bd = 15,text = "2", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(2)).grid(row = 4, column = 1, sticky = W)
btn3 = Button(window, bg = "lightgrey", bd = 15,text = "3", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(3)).grid(row = 4, column = 2, sticky = W)
btnsub = Button(window, bg = "lightgrey", bd = 15,text = "-", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick("-")).grid(row = 4, column = 3, sticky = W)



btn0 = Button(window, bg = "lightgrey", bd = 15,text = "0", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(0)).grid(row = 5, column = 0, sticky = W)
btndot = Button(window, bg = "lightgrey", bd = 15,text = ".", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = lambda:btnClick(".")).grid(row = 5, column = 1, sticky = W)
btnequal = Button(window, bg = "lightgrey", bd = 15,text = "=", padx = 20, pady = 17, font = ("arial", 15, "bold"), command = btnEquals).grid(row = 5, column = 2, sticky = W)
btnmul = Button(window, bg = "lightgrey", bd = 15,text = "*", padx = 20, pady = 17, font = ("arial", 15, "bold"),command = lambda:btnClick("*")).grid(row = 5, column = 3, sticky = W)
window.mainloop()
