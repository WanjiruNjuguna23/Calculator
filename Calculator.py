import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from Operations import Operations


class CalculatorApp:
    def __init__(self, root):
        """
        Initialize the calculator application.

        Args:
        - root: Tkinter root window
        """
        self.root_window = root
        self.root_window.title("Calculator")
        self.style = ThemedStyle(self.root_window)
        self.style.set_theme("arc")  # Use the 'arc' theme from ttkthemes

        self.entry = ttk.Entry(self.root_window, width=50, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        """
        Create the calculator GUI widgets.
        """
        # List of button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        # Create buttons and assign command to on_button_click method
        for i, text in enumerate(buttons):
            row = i // 4 + 1
            col = i % 4
            button = ttk.Button(self.root_window, text=text, width=10, style='Calculator.TButton')
            button.grid(row=row, column=col, padx=5, pady=5)
            button.bind('<Button-1>', lambda event, t=text: self.on_button_click(t))

    def on_button_click(self, text):
        """
        Handle button clicks.

        Args:
        - text: Button text
        """
        if text == '=':
            # Evaluate the expression and display the result
            result = Operations.evaluate_expression(self.entry.get())
            if result is not None:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            else:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid input")
        elif text == 'C':
            # Clear the entry widget
            self.entry.delete(0, tk.END)
        else:
            # Append the button text to the entry widget
            self.entry.insert(tk.END, text)


if __name__ == "__main__":
    root_window = tk.Tk()
    app = CalculatorApp(root_window)
    root_window.mainloop()
