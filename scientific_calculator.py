import tkinter as tk

import math


def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)


def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def ans_button_click():
    if previous_result is not None:
        entry.insert(tk.END, str(previous_result))

def abs_button_click():
    entry.insert(tk.END, "abs(")


root = tk.Tk()

root.title("Scientific Calculator")
root.geometry("400x600")
root.grid_propagate(False)
root.configure(bg="Black")

#label_result=Label(root,width="27",height="2",text="",font=("arial",30))
#label_result.pack()

entry = tk.Entry(root, width=20, borderwidth=10, font="arial 30", bg="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("sin\u03B8", lambda: button_click("math.sin(")), 
    ("cos\u03B8", lambda: button_click("math.cos(")), 
    ("tan\u03B8", lambda: button_click("math.tan(")), 
    ("\u221A", lambda: button_click("math.sqrt(")), 
    ("π", lambda: button_click("math.pi")), 
    ("x\u00B2", lambda: button_click("**2")), 
    ("^", lambda: button_click("**")), 
    ("sin\u207B\u00B9", lambda: button_click("math.asin(")), 
    ("cos\u207B\u00B9", lambda: button_click("math.acos(")), 
    ("tan\u207B\u00B9", lambda: button_click("math.atan(")), 
    ("Rad", lambda: button_click("math.radians(")), 
    ("In", lambda: button_click("math.log(")), 
    ("log", lambda: button_click("math.log10(")), 
    ("Abs", lambda: abs_button_click), 
    ("round", lambda: button_click("round(")), 
    ("%", lambda: button_click("%")), 
    ("(", lambda: button_click("(")), 
    (")", lambda: button_click(")")), 
    (",", lambda: button_click(",")), 
    ("←", lambda: entry.delete(len(entry.get()) - 1)), 
    ("7", lambda: button_click("7")), 
    ("8", lambda: button_click("8")), 
    ("9", lambda: button_click("9")), 
    ("DEL", lambda: entry.delete(len(entry.get()) - 1)), 
    ("AC", lambda: entry.delete(0, tk.END)), 
    ("4", lambda: button_click("4")), 
    ("5", lambda: button_click("5")), 
    ("6", lambda: button_click("6")), 
    ("X", lambda: button_click("*")), 
    ("/", lambda: button_click("/")), 
    ("1", lambda: button_click("1")), 
    ("2", lambda: button_click("2")), 
    ("3", lambda: button_click("3")), 
    ("+", lambda: button_click("+")), 
    ("-", lambda: button_click("-")), 
    ("0", lambda: button_click("0")), 
    (".", lambda: button_click(".")), 
    ("Exp", lambda: button_click("e")), 
    ("Ans", lambda: abs_button_click), 
    ("=", lambda: evaluate())
]


row_count = 1
col_count = 0


for button in buttons:
    tk.Button(root, text=button[0], width=6, height=2, font=("Arial", 12), bd=1, fg="light grey", bg="black", command=button[1]).grid(row=row_count, column=col_count, padx=5, pady=2)
    col_count += 1
    if col_count > 4:
        col_count = 0
        row_count += 1

for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(row_count + 1):
    root.grid_rowconfigure(i, weight=1)


previous_result = None

root.mainloop()
