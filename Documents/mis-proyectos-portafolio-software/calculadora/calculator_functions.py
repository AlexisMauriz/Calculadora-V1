from tkinter import END
class Calculator:
    def __init__(self):
        self.i = 0

    def get_numbers(self, n, display):
        display.insert(END, n)
        self.i += 1

    def get_operation(self, operator, display):
        operator_length = len(operator)
        if operator == "**":
            display.insert(END, operator)
        else:
            display.insert(END, " " + operator + " ")
        self.i += operator_length

    def clear_display(self, display):
        display.delete(1.0, END)

    def undo(self, display):
        display_state = display.get("1.0", "end-1c")
        if len(display_state):
            display.delete("end-2c", END)
            self.i -= 1

    def calculate(self, display):
        display_state = display.get("1.0", "end-1c")
        try:
            result = eval(display_state)
            self.clear_display(display)
            display.insert(END, result)
        except Exception as e:
            self.clear_display(display)
            display.insert(END, "Error")
