from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("CreditCardAuthentication")
root.geometry("600x400")

root.configure(background="yellow")

img = ImageTk.PhotoImage(Image.open("Card.png"))

CardImage = Label(root,image=img)
CardImage.pack()

input_box = Entry(root)
input_box.pack()

def authentication():
    inputedData = input_box.get()
    
    try:
        inputedData = int(input_box.get())
        inputdata = type(inputedData)
        print(inputdata)
        messagebox.showinfo("Card","card is accepted")
    except:
        messagebox.showinfo("Card","card is rejected")


    #if inputedData == 202212345:
        #messagebox.showinfo("CreditCard","Credit Card Accepted")
btn=Button(root,text="Check",command=authentication)
btn.pack()

root.mainloop() 
