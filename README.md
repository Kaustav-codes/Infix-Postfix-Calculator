# 🧮 Infix to Postfix Calculator GUI

This project is a simple Python GUI-based calculator that takes an **infix arithmetic expression**, parses it, converts it to **postfix (Reverse Polish Notation)**, and then evaluates the result — all with a clean interface built using Tkinter.

---

## 🔧 Features

- ✅ Parses infix expressions (e.g., `3+4*2/(1-5)`)
- ✅ Converts them to postfix notation (e.g., `3 4 2 * 1 5 - / +`)
- ✅ Evaluates the postfix expression
- ✅ GUI built with Python's `tkinter` module

---

## 🧠 How It Works

- `parse_infix(input)`: Adds spaces between operands and operators for easy tokenization.
- `convert_to_postfix(infix)`: Implements the **Shunting Yard Algorithm** to convert infix to postfix.
- `calculate_postfix(postfix)`: Evaluates the postfix expression using a stack.
- Tkinter GUI: Allows users to input the infix expression and see each transformation step-by-step.

---

## 💻 Demo

![Readme SS](https://github.com/user-attachments/assets/e936e1ef-a2ee-4aeb-9771-42df7a177471)


---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Run the App

```bash
python calculator.py
