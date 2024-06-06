import tkinter as tk
from builtins import eval


def click(event):
    current = main_display.get()
    text = event.widget.cget('text')

    if text == "=":
        result = eval(current)
        main_display.delete(0, tk.END)
        main_display.insert(tk.END, result)
    elif text == "C":
        main_display.delete(0, tk.END)
    else:
        main_display.insert(tk.END, text)




main_window = tk.Tk()
main_window.title("Calculator")
main_display = tk.Entry(main_window,font=("Arial",25),justify="right")
main_display.pack(fill = tk.X, padx = 10,pady =10 ,ipady= 10)

butn_f = tk.Frame(main_window)
butn_f.pack()

button_label = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "/", "=",
]

i=0
for label in button_label:
    button = tk.Button(butn_f, text=label, font=("Arial",18) ,padx =20,pady =20)
    button.grid(row= i//4,column = i%4, padx =10, pady = 10)
    button.bind("<Button-1>", click)
    i +=1

main_window.mainloop()




