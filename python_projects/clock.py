import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    labal.config(text=string)
    labal.after(1000,time)

labal = tk.Label(root, font=('calibari',50,'bold'),background='pink',foreground='red')
labal.pack(anchor='center')

time()

root.mainloop()