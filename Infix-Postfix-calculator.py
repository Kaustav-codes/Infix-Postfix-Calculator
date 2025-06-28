from tkinter import *

def parse_infix(input):
    ret = ""
    for i, tmp in enumerate(input):
        if tmp == '.':
            ret += tmp
        elif tmp.isdigit():
            ret += tmp
            if i < len(input) - 1:
                if not input[i + 1].isdigit() and input[i + 1] != '.':
                    ret += " "
        else:
            ret += tmp + " "
    return ret

def convert_to_postfix(infix):
    ret = ""
    infix = infix.strip()
    infix_arr = infix.split(' ')
    s = []
    for token in infix_arr:
        if token == "(":
            s.append(token)
        elif token == "+":
            while s and s[-1] in ["+", "-", "*", "/"]:
                ret += s.pop() + " "
            s.append(token)
        elif token == "-":
            while s and s[-1] in ["+", "-", "*", "/"]:
                ret += s.pop() + " "
            s.append(token)
        elif token == "*":
            while s and s[-1] in ["*", "/"]:
                ret += s.pop() + " "
            s.append(token)
        elif token == "/":
            while s and s[-1] in ["*", "/"]:
                ret += s.pop() + " "
            s.append(token)
        elif token == ")":
            while s and s[-1] != "(":
                ret += s.pop() + " "
            if s and s[-1] == "(":
                s.pop()
        else:
            ret += token + " "
    while s:
        ret += s.pop() + " "
    return ret

def calculate_postfix(postfix):
    s = []
    postfix = postfix.strip()
    postfix_arr = postfix.split(' ')
    for token in postfix_arr:
        if token in ["+", "-", "*", "/"]:
            b = s.pop()
            a = s.pop()
            if token == "+":
                s.append(a + b)
            elif token == "-":
                s.append(a - b)
            elif token == "*":
                s.append(a * b)
            elif token == "/":
                s.append(a / b)
        else:
            s.append(float(token))
    return str(s.pop())

# ----- GUI Design -----
root = Tk()
root.title("Dark Theme Calculator")
root.geometry("350x400")
root.configure(bg="#1e1e1e")

# Styling variables
bg_color = "#1e1e1e"
fg_color = "#ffffff"
entry_bg = "#2d2d2d"
btn_color = "#3c3c3c"

# Create frame with dark background
app = Frame(root, bg=bg_color)
app.pack(padx=10, pady=10)

def styled_label(text):
    return Label(app, text=text, fg=fg_color, bg=bg_color, font=("Helvetica", 10, "bold"))

def styled_entry():
    return Entry(app, bg=entry_bg, fg=fg_color, insertbackground=fg_color, highlightbackground=entry_bg)

styled_label("Calculator").pack(pady=(0, 10))

styled_label("Infix").pack()
infix = styled_entry()
infix.pack()

styled_label("Temp Infix").pack()
tempinfix = styled_entry()
tempinfix.pack()

styled_label("Postfix").pack()
postfix = styled_entry()
postfix.pack()

styled_label("Result").pack()
result = styled_entry()
result.pack()

def calculate():
    infix_str = infix.get()
    tempinfix_str = parse_infix(infix_str)
    postfix_str = convert_to_postfix(tempinfix_str)
    result_str = calculate_postfix(postfix_str)
    tempinfix.delete(0, END)
    tempinfix.insert(0, tempinfix_str)
    postfix.delete(0, END)
    postfix.insert(0, postfix_str)
    result.delete(0, END)
    result.insert(0, result_str)

btn = Button(app, text="Calculate", command=calculate, bg=btn_color, fg=fg_color, activebackground="#505050", font=("Helvetica", 10, "bold"))
btn.pack(pady=10, ipadx=10, ipady=5)

root.mainloop()
