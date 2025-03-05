import tkinter as tk

def add():
    result_var.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result_var.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result_var.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result_var.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result_var.set("Ошибка! Деление на ноль.")

root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label1 = tk.Label(root, text="Первое число:")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Второе число:")
label2.grid(row=1, column=0)

result_var = tk.StringVar()
result_label = tk.Label(root, text="Результат:")
result_label.grid(row=2, column=0)

result_display = tk.Label(root, textvariable=result_var)
result_display.grid(row=2, column=1)

add_button = tk.Button(root, text="Сложить", command=add)
add_button.grid(row=3, column=0)

subtract_button = tk.Button(root, text="Вычесть", command=subtract)
subtract_button.grid(row=3, column=1)

multiply_button = tk.Button(root, text="Умножить", command=multiply)
multiply_button.grid(row=3, column=2)

divide_button = tk.Button(root, text="Делить", command=divide)
divide_button.grid(row=4, column=0)

root.mainloop()