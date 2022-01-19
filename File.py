from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("CreditCardAuthentication")
root.geometry("600x400")

root.configure(background="yellow")

input_box = Entry(root)
input_box.pack()

img = ImageTk.PhotoImage(Image.open("Card.png"))

cardLabel = Label(root, image=img)
cardLabel.pack()

def authentication():
    inputedData = input_box.get()
    print(type(inputedData))
    
    #if inputedData == 202212345:
        #messagebox.showinfo("CreditCard","Credit Card Accepted")
btn=Button(root,text="Check",command=authentication)
btn.pack()
        
root.mainloop()