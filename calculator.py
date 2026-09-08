import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        # Entry field
        self.entry = tk.Entry(root, font=("Arial", 18), bd=10, relief="sunken", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

        # Buttons layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Clear button
        clear_btn = tk.Button(root, text="C", width=10, height=2, command=self.clear, bg="#f44336", fg="white")
        clear_btn.grid(row=5, column=0, columnspan=4, pady=10)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
