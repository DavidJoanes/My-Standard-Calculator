from tkinter import *
import math
import tkinter.messagebox


class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.newNumber = True
        self.opPending = False
        self.operation = ""
        self.equation = False

    def get_variables(self, num):
        self.equation = False
        temp1 = display.get()
        temp2 = str(num)
        if self.newNumber:
            self.current = temp2
            self.newNumber = False
        else:
            if temp2 == '.':
                if temp2 in temp1:
                    return
            self.current = temp1 + temp2
        self.display(self.current)

    def get_variable_for_zero(self, num):
        self.equation = False
        temp1 = display.get()
        temp2 = str(num)
        if temp1 != "0":
            return result.get_variables(num)
        else:
            display.insert(0, '')

    def get_operation_for_parenthesis(self, operator):
        j = display.get()
        if j == "0":
            display.delete(0, END)
            display.insert(0, operator)
        else:
            display.insert(END, operator)

    def do_sum(self):
        try:
            if self.operation == "add":
                self.total += self.current
            if self.operation == "minus":
                self.total -= self.current
            if self.operation == "multiply":
                self.total *= self.current
            if self.operation == "divide":
                self.total /= self.current
            if self.operation == "raise":
                self.total = self.total ** self.current
            if self.operation == "square":
                self.total = self.total ** 2
            if self.operation == "sqrt":
                self.total = math.sqrt(self.total)
            if self.operation == "rootof":
                self.total = self.total ** (1/self.current)
            if self.operation == "factorial":
                self.total=int(display.get())
                self.total=math.factorial(self.total)
            if self.operation == "ln":
                self.total = math.log(self.total)
            if self.operation == "log":
                self.total= math.log(self.total,10)
            if self.operation == "log2":
                self.total = math.log2(self.total)
            if self.operation == "log1p":
                self.total = math.log1p(self.total)
            if self.operation == "log10":
                self.total = math.log10(self.total)
            if self.operation == "ᴫ":
                self.total = (math.pi)
            if self.operation == "2ᴫ":
                self.total = (2 * math.pi)
            if self.operation == "sine":
                self.total= math.sin(self.total)
            if self.operation == "cosine":
                self.total = math.cos(self.total)
            if self.operation == "tangent":
                self.total = math.tan(self.total)
            if self.operation == "exp":
                self.total = (2.7182818284590452353602874713527 * self.total)
            if self.operation == "2√":
                self.total = (2*math.sqrt(self.total))
            if self.operation == "inv":
                self.total = 1/self.total
            if self.operation == "acosh":
                self.total = math.acosh(self.total)
            if self.operation == "asinh":
                self.total = math.asinh(self.total)
            if self.operation == "atanh":
                self.total = math.atanh(self.total)
            if self.operation == "lgamma":
                self.total = math.lgamma(self.total)
            if self.operation == "mod":
                j = display.get()
                self.total = float(j) % 2
            if self.operation == "expm1":
                self.total = math.expm1(self.total)
            self.newNumber = True
            self.opPending = False
            self.display(self.total)
        except Exception:
            self.display("Result is undefined!")

    def calculate(self, op):
        self.current = float(self.current)
        if self.opPending:
            self.do_sum()
        elif not self.equation:
            self.total = self.current
        self.newNumber = True
        self.opPending = True
        self.operation = op
        self.equation = False

    def calc_total(self):
        self.equation = True
        self.current = float(self.current)
        if self.opPending == True:
            self.do_sum()
        else:
            self.total = float(display.get())

    def display(self, value):
        display.delete(0, END)
        display.insert(0, value)

    def clear(self):
        self.equation = False
        self.current = "0"
        j = display.get()
        if len(j) > 0:
            new_string = j[: - 1]
            display.delete(0, END)
            display.insert(0, new_string)
            if len(j) == 1:
                display.delete(0, END)
                display.insert(0, "0")
        self.newNumber = True

    def all_clear(self):
        self.clear()
        self.total = 0
        self.display(0)
        self.newNumber = True

    def sign(self):
        self.equation = False
        self.current = -(float(display.get()))
        self.display(self.current)

    def scientific(self):
        root.configure(background="#fff")
        root.geometry("800x395")
        root.resizable(width=False, height=False)

    def standard(self):
        root.geometry("450x370")
        root.resizable(width=False, height=False)

    def Exit(self):
        Exit = tkinter.messagebox.askyesno("Calculator", "Confirm exit?")
        if Exit > 0:
            root.destroy()
            return

    def about(self):
        tkinter.messagebox.showinfo("Calculator", "This program was solely developed by David Kemdirim. \nIt is strictly copyright protected!")


result = Calculator()
root = Tk()
root.title("Calculator")
root.configure(background = "#fff")
root.geometry("450x390")
root.resizable(width=False, height=False)

root.iconbitmap('C:\\Users\\User\Documents\Python\calculator.ico')

#Adding Menu bar
calculator = Frame(root, bg="white")
calculator.grid()

menubar = Menu(calculator)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=filemenu)
filemenu.add_command(label="Standard Calc", command=result.standard)
filemenu.add_command(label="Scientific Calc", command=result.scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=result.Exit)

filemenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=filemenu2)
filemenu2.add_command(label="About", command=result.about)

#Adding the calculator input screen
display = Entry(calculator, font=("arial", 20, "bold"), bg="pink", fg="#fff", bd=30, width=26, relief=SUNKEN, justify=RIGHT)
display.grid(row=0, column=0, columnspan=5, pady=1)
display.insert(END, "0")

label = Label(calculator, font=("arial", 15, "bold"), text="SCIENTIFIC CALCULATOR", fg="#000", bg="#fff", justify=CENTER)
label.grid(row=0, column=5, columnspan=4)
label2 = Label(calculator, font=("arial", 7, "bold", "italic"), text="Powered by: JOGENICS", fg="#000", bg="#fff", justify=CENTER)
label2.grid(row=6, column=3, columnspan=4)


# Adding buttons
Button(calculator, text="√", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda :result.calculate("sqrt")).grid(row=1, column=0, pady=5)
Button(calculator, text="2√", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("2√")).grid(row=1, column=1, pady=5)
Button(calculator, text="ln", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda :result.calculate("ln")).grid(row=1, column=2, pady=5)

Button(calculator, text=chr(67), width=6, height=2, bd=4, bg="pink", fg="white", command=result.clear).grid(row=1, column=3, pady=5)
Button(calculator, text=chr(67)+chr(69), width=6, height=2, bd=4, bg="pink", fg="white", command=result.all_clear).grid(row=1, column=4, pady=5)
Button(calculator, text="^2", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("square")).grid(row=2, column=3, pady=5)
Button(calculator, text="-", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("minus")).grid(row=3, column=3, pady=5)
Button(calculator, text="+", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("add")).grid(row=4, column=3, pady=5)
Button(calculator, text="=", width=6, height=2, bd=4, bg="pink", fg="white", command=result.calc_total).grid(row=5, column=3, pady=5)

Button(calculator, text="x^y", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("raise")).grid(row=2, column=4, pady=5)
Button(calculator, text="X", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("multiply")).grid(row=3, column=4, pady=5)
Button(calculator, text=chr(247), width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("divide")).grid(row=4, column=4, pady=5)
Button(calculator, text="exp", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda :result.calculate("exp")).grid(row=5, column=4, pady=5)

Button(calculator, text="7", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("7")).grid(row=2, column=0, pady=5)
Button(calculator, text="8", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("8")).grid(row=2, column=1, pady=5)
Button(calculator, text="9", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("9")).grid(row=2, column=2, pady=5)

Button(calculator, text="4", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("4")).grid(row=3, column=0, pady=5)
Button(calculator, text="5", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("5")).grid(row=3, column=1, pady=5)
Button(calculator, text="6", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("6")).grid(row=3, column=2, pady=5)

Button(calculator, text="1", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("1")).grid(row=4, column=0, pady=5)
Button(calculator, text="2", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("2")).grid(row=4, column=1, pady=5)
Button(calculator, text="3", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables("3")).grid(row=4, column=2, pady=5)

Button(calculator, text=chr(177), width=6, height=2, bd=4, bg="white", fg="black", command=result.sign).grid(row=5, column=0, pady=5)
Button(calculator, text="0", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variable_for_zero("0")).grid(row=5, column=1, pady=5)
Button(calculator, text=".", width=6, height=2, bd=4, bg="white", fg="black", command=lambda :result.get_variables(".")).grid(row=5, column=2, pady=5)

#===========================Scientific==================================#
Button(calculator, text="ᴫ", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("ᴫ")).grid(row=1, column=5, pady=5, padx=16)
Button(calculator, text="cos", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("cosine")).grid(row=1, column=6, pady=5, padx=16)
Button(calculator, text="tan", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("tangent")).grid(row=1, column=7, pady=5, padx=16)
Button(calculator, text="sin", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("sine")).grid(row=1, column=8, pady=5, padx=16)

Button(calculator, text="2ᴫ", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("2ᴫ")).grid(row=2, column=5, pady=5, padx=16)
Button(calculator, text="cosh", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("cosh")).grid(row=2, column=6, pady=5, padx=16)
Button(calculator, text="tanh", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("tanh")).grid(row=2, column=7, pady=5, padx=16)
Button(calculator, text="sinh", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("sinh")).grid(row=2, column=8, pady=5, padx=16)

Button(calculator, text="log", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("log")).grid(row=3, column=5, pady=5, padx=16)
Button(calculator, text="acosh", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("acosh")).grid(row=3, column=6, pady=5, padx=16)
Button(calculator, text="atanh", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("atanh")).grid(row=3, column=7, pady=5, padx=16)
Button(calculator, text="asinh", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("asinh")).grid(row=3, column=8, pady=5, padx=16)


Button(calculator, text="log2", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("2ᴫ")).grid(row=4, column=5, pady=5, padx=16)
Button(calculator, text="n!", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda :result.calculate("factorial")).grid(row=4, column=6, pady=5, padx=16)
Button(calculator, text="1/x", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("inv")).grid(row=4, column=7, pady=5, padx=16)
Button(calculator, text="expm1", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("expm1")).grid(row=4, column=8, pady=5, padx=16)


Button(calculator, text="log10", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("log10")).grid(row=5, column=5, pady=5, padx=16)
Button(calculator, text="log1p", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("log1p")).grid(row=5, column=6, pady=5, padx=16)
Button(calculator, text="mod", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda :result.calculate("mod")).grid(row=5, column=7, pady=5, padx=16)
Button(calculator, text="lgamma", width=6, height=2, bd=4, bg="pink", fg="white", command=lambda : result.calculate("lgamma")).grid(row=5, column=8, pady=5, padx=16)


#Пᴫ
root.config(menu=menubar)
root.mainloop()
