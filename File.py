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
    inputedData = int(input_box.get())
    inputdata = type(inputedData)
    
    try:
        if(inputdata=="int"):
        print("card is expected")
    except:
        print("card is rejected")
        
    
    #if inputedData == 202212345:
        #messagebox.showinfo("CreditCard","Credit Card Accepted")
btn=Button(root,text="Check",command=authentication)
btn.pack()
        
root.mainloop()
