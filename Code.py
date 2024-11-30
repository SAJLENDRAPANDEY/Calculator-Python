import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Main Window
app = tk.Tk()
app.title("Calculator BY SAJLENDRA PANDEY ")
app.geometry("400x600")
expression = ""
entry_var = tk.StringVar()

# Entry Field
entry = tk.Entry(app, textvar=entry_var, font="Arial 20", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

# Button Frame
frame = tk.Frame(app)
frame.pack()

# Button Layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

for i, button_text in enumerate(buttons):
    btn = tk.Button(frame, text=button_text, font="Arial 15", width=5, height=2)
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    btn.bind("<Button-1>", click)

app.mainloop()
