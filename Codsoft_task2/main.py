from tkinter import *

class Calculator:
    
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")
        self.equation = Entry(master, width=30, borderwidth=5, font=("Arial", 12))
        self.equation.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=6)
        self.createButton()

    def createButton(self):
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton('+', bg='#1679AB', fg='white')
        b_sub = self.addButton('-', bg='#1679AB', fg='white')
        b_mult = self.addButton('*', bg='#1679AB', fg='white')
        b_div = self.addButton('/', bg='#1679AB', fg='white')
        b_clear = self.addButton('c', bg='#C80036', fg='white')
        b_equal = self.addButton('=', bg='#219C90', fg='white')
        
        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_mult]
        row4 = [b_clear, b0, b_equal, b_div]

        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for b in row:
                b.grid(row=r, column=c, columnspan=1, pady=3, padx=3)
                c += 1
            r += 1
       
        # Adding extra padding below the last row
        self.master.grid_rowconfigure(r, minsize=10)

    def addButton(self, value, bg='white', fg='black'):
        return Button(self.master,
                      text=value, 
                      width=6,
                      height=3,
                      font=("Arial", 12),
                      bg=bg, 
                      fg=fg,
                      command=lambda: self.clickButton(str(value)))
    
    def clickButton(self, value):
        current_equation = str(self.equation.get())

        if value == "c":
            self.equation.delete(0, END)
        elif value == "=":
            try:
                answer = str(eval(current_equation))
                self.equation.delete(0, END)
                self.equation.insert(0, answer)
            except:
                self.equation.delete(0, END)
                self.equation.insert(0, "Error")
        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation + value)


if __name__ == "__main__":
    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()
