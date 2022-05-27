# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:26:58 2022

@author: dell
"""

from tkinter import*
import random

root = Tk()
root.title("Fibonacci Sum")
root.geometry("400x400")

label_series = Label(root,text = "Fibonacci Series : ")
label_sum = Label(root)
my_input = Entry(root)

def fibonacci():
    end = int( my_input.get())
    start = 0
    sum1 = 0
    first_no = 0
    second_no = 1
    total_sum = 0
    while(start <= end):
        label_series["text"] += str(sum1) + " "
        start += 1
        first_no = second_no
        second_no = sum1
        sum1 = first_no + second_no
        total_sum = total_sum + sum1
    label_sum["text"] = "Fibonacci Sum : " + str(total_sum)
        

btn = Button(root,text = "Start the Fibonacci Series",command = fibonacci)
my_input.pack()
label_series.pack()
label_sum.pack()

btn.pack()

root.mainloop()