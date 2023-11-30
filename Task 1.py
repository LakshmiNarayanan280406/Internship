import tkinter
window = tkinter.Tk()
window.title("Button And Text Box")
window.geometry('500x300')
label1 = tkinter.Label(window, text="Enter Name:", font=('Arial', 14), fg='blue')
label1.grid(row=0, column=0, padx=10, pady=10)
data = tkinter.StringVar()
textbox1 = tkinter.Entry(window, textvariable=data, fg='blue', font=('arial', 14))
textbox1.grid(row=0, column=1)
def function():
    emptylabel.config(text='Your name is ' + data.get())
button1 = tkinter.Button(window, command=function, text='Click Here', fg='blue', font=('arial', 14))
button1.grid(row=1, column=1)
emptylabel = tkinter.Label(window, fg='green', font=('Arial', 14))
emptylabel.grid(row=2, column=1)
window.mainloop()