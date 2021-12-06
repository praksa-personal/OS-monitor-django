from django.shortcuts import render
import tkinter as tk
import time

def button():
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300)
    canvas1.pack()

    def hello ():  
        label1 = tk.Label(root, text= 'Test running...', fg='green', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 200, window=label1)
        
    button1 = tk.Button(text='Run test',command=hello, bg='brown',fg='white')
    canvas1.create_window(150, 150, window=button1)

    time.sleep(10)






