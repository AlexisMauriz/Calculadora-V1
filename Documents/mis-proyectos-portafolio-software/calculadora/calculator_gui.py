from tkinter import *
from calculator_functions import Calculator

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x330")
        self.root.minsize(300, 330)
        self.root.maxsize(300, 330)

        self.display = Text(root, width=30, height=4, font=("Arial", 13))
        self.display.grid(row=1, columnspan=4, sticky="we")

        self.calculator = Calculator()

        # Agrega los botones y vincúlalos a los métodos de la calculadora
        # Botones de Calculadora
        Button(root, text="=", width=41, height=2, command=lambda: self.calculator.calculate(self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=7, column=0, columnspan=4)
        Button(root, text="AC", width=9, height=2, command=lambda: self.calculator.clear_display(self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=2, column=0)
        Button(root, text="(", width=9, height=2, command=lambda: self.calculator.get_operation("(", self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=2, column=1)
        Button(root, text=")", width=9, height=2, command=lambda: self.calculator.get_operation(")", self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=2, column=2)
        Button(root, text="exp", width=9, height=2, command=lambda: self.calculator.get_operation("**", self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=6, column=2)
        Button(root, text="🠔", width=9, height=2, command=lambda: self.calculator.undo(self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=2, column=3)
        Button(root, text="+", width=9, height=2, command=lambda: self.calculator.get_operation("+", self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=3, column=3)
        Button(root, text="-", width=9, height=2, command=lambda: self.calculator.get_operation("-", self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=4, column=3)
        Button(root, text="x", width=9, height=2, command=lambda: self.calculator.get_operation("*", self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=5, column=3)
        Button(root, text="/", width=9, height=2, command=lambda: self.calculator.get_operation("/", self.display), anchor="center", bg="Spring Green", fg="black", activebackground="Pale Green").grid(row=6, column=3)

        Button(root, text="7", width=9, height=2, command=lambda: self.calculator.get_numbers(7, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=3, column=0)
        Button(root, text="8", width=9, height=2, command=lambda: self.calculator.get_numbers(8, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=3, column=1)
        Button(root, text="9", width=9, height=2, command=lambda: self.calculator.get_numbers(9, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=3, column=2)

        Button(root, text="4", width=9, height=2, command=lambda: self.calculator.get_numbers(4, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=4, column=0)
        Button(root, text="5", width=9, height=2, command=lambda: self.calculator.get_numbers(5, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=4, column=1)
        Button(root, text="6", width=9, height=2, command=lambda: self.calculator.get_numbers(6, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=4, column=2)

        Button(root, text="1", width=9, height=2, command=lambda: self.calculator.get_numbers(1, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=5, column=0)
        Button(root, text="2", width=9, height=2, command=lambda: self.calculator.get_numbers(2, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=5, column=1)
        Button(root, text="3", width=9, height=2, command=lambda: self.calculator.get_numbers(3, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=5, column=2)
        Button(root, text="0", width=21, height=2, command=lambda: self.calculator.get_numbers(0, self.display), anchor="center", bg="Cyan", fg="black", activebackground="LightSkyBlue").grid(row=6, column=0, columnspan=2)

        Label(root, text="").grid(row=2, column=0)
        Label(root, text="").grid(row=3, column=0)
        Label(root, text="").grid(row=4, column=0)
        Label(root, text="").grid(row=5, column=0)

        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = CalculatorApp(root)
