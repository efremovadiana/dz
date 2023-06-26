from tkinter import*

window = Tk()
window.geometry('700x500')
window.title('My first window app')
label_title = Label(text="it's my window app", font=("Arial", 24), fg="white", bg="red")
label_title.place(width=700, height=50, x=0, y=0)

window.mainloop()