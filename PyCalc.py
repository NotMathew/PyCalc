import tkinter as tk
import math
import cmath


class PyCalc:
    def __init__(self, master):
        self.master = master
        master.title("PyCalc")
        master.geometry("400x500")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Display
        display = tk.Entry(self.master, textvariable=self.result_var, justify="right", font=("Arial", 20))
        display.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # Buttons
        buttons = [
            'C', '←', '(', ')', 'π',
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '±', '+', 'log',
            'x²', '√x', 'x^y', '1/x', '='
        ]

        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.master, text=button, command=cmd, width=8, height=2).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Configure grid
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif key == 'C':
            self.result_var.set("0")
        elif key == '←':
            current = self.result_var.get()
            self.result_var.set(current[:-1])
        elif key == '±':
            current = self.result_var.get()
            if current.startswith('-'):
                self.result_var.set(current[1:])
            else:
                self.result_var.set('-' + current)
        elif key == 'π':
            self.result_var.set(str(math.pi))
        elif key in ('sin', 'cos', 'tan'):
            try:
                value = float(self.result_var.get())
                if key == 'sin':
                    result = math.sin(math.radians(value))
                elif key == 'cos':
                    result = math.cos(math.radians(value))
                else:
                    result = math.tan(math.radians(value))
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif key == 'log':
            try:
                value = float(self.result_var.get())
                result = math.log10(value)
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif key == 'x²':
            try:
                value = float(self.result_var.get())
                result = value ** 2
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif key == '√x':
            try:
                value = float(self.result_var.get())
                result = math.sqrt(value)
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif key == 'x^y':
            self.result_var.set(self.result_var.get() + '**')
        elif key == '1/x':
            try:
                value = float(self.result_var.get())
                result = 1 / value
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0":
                self.result_var.set(key)
            else:
                self.result_var.set(self.result_var.get() + key)


def main():
    root = tk.Tk()
    calculator = PyCalc(root)
    root.mainloop()


if __name__ == "__main__":
    main()