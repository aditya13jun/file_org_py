import tkinter

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "root", "="]
]

right_Symbols = ["/", "x", "-", "+", "="]
top_Symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_1 = "#D4D4D2"
color_2 = "#1C1C1C"
color_3 = "#505050"
color_4 = "#FF9500"
color_5 = "white"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)  #Freeze the size...

frame = tkinter.Frame(window) #place frame inside window...
label = tkinter.Label(frame, text="0", font=("Ariel", 45), background=color_2, foreground=color_5, anchor="e", width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Ariel", 30), width=column_count-1, height=1, command=lambda value=value: button_clicked(value))

        if value in top_Symbols:
            button.config(foreground=color_2, background=color_1)
        elif value in right_Symbols:
            button.config(foreground=color_5, background=color_4)
        else:
            button.config(foreground=color_5, background=color_3)

        button.grid(row=row+1, column=column)

frame.pack()

A="0"
operator = None
B = None

def clear_All():
    global A, B, operator
    A ="0"
    operator = None
    B= None

def remove_zero_decimal(num):
    if num%1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_Symbols, top_Symbols, label, A, B, operator

    if value in right_Symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "x":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "/":
                    label["text"] = remove_zero_decimal(numA / numB)
                clear_All()

        elif value in "+-x/":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            operator = value
    
    elif value in top_Symbols:
        if value == "AC":
            clear_All()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"]  = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    else:
        if value == "root":
            result = float(label["text"]) ** 0.5
            label["text"] = f"{result:.4f}"
        elif value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value  #replaceing 0...
            else:
                label["text"] += value  #append digits further...


#center the window...
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_X = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_X}+{window_y}")  #format = "(w)x(h)+(x)+(y)"

window.mainloop()