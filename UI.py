from tkinter import*
import os
import pickle

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.master = master

credentials = ["", "", ""]

root = Tk()
app = Window(root)

def click():
    exe = 'UI.py'
    final_path = ""

    for root, dirs, files in os.walk(r'C:'):
        for name in files:
            if name == exe:
                final_path = os.path.abspath(root)

    final_path = os.path.join(final_path, "credentials.pickle")
    raw_data = open(final_path , "wb")

    credentials = ["", ""]
    u = username_box.get()
    p = password_box.get()

    credentials[0] = u
    credentials[1] = p
    
    pickle.dump(credentials, raw_data)
    recorded.pack()

def clear():
    recorded.pack_forget()
    username_box.delete(0 , len(username_box.get()))
    password_box.delete(0, len(password_box.get()))

root.geometry("500x500")
root.title("Credentials")

recorded = Label(root,
        font = "Times 15",
        justify = CENTER,
        text = "Credentials have been recorded, you can now run the program")
recorded.pack_forget()


username = Label(root,
            text = "Username",
            font = "Times 20",
            justify = CENTER)

username_box = Entry(root,
                font = "Times 20",
                justify = CENTER)

password = Label(root,
            text = "Password",
            font = "Times 20",
            justify = CENTER)

password_box = Entry(root,
                font = "Times 20",
                justify = CENTER,
                show = "*")

enter = Button(root,
        font = "Times 20",
        justify = CENTER,
        command = click,
        text = "Enter")

clear = Button(root,
        font = "Times 20",
        justify = CENTER,
        command = clear,
        text = "Clear")



username.pack()
username_box.pack()
password.pack()
password_box.pack()
enter.pack()
clear.pack()
root.mainloop()
