from tkinter import *
from tkinter import messagebox
import base64
from datetime import datetime
import pywhatkit
def whatsapp():
     now = datetime.now()
     ext=text3.get(1.0,END)
     dial = "+91"
     total = dial+str(text)
     print(total)
     pywhatkit.sendwhatmsg_instantly(total, str(encrypt))
def decrypt():
    password = code.get()
    screen2 = Tk()
    if password == "12345":
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")
        Label(screen2, text="DECRYPT", font="arial",
        fg="white", bg="#00bd56").place(x=10, y=10)
        text2 = Text(screen2, font="Rpbote 10", bg="white",
        relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("decryption", "Input password")
    elif password != "12345":
        messagebox.showerror("decryption", "Invalid Password")
def encrypt():
    global text3
    global text4
    global encrypt
    password = code.get()
    screen1 = Tk()
    if password == "12345":
        screen1.title("Encryption")
        screen1.geometry("400x440")
        screen1.configure(bg="#ed3833")
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        Label(screen1, text="ENCRYPT", font="arial",
        fg="white", bg="#ed3833").place(x=10, y=0)
        text4 = Text(screen1, font="Rpbote 10", bg="white",
        relief=GROOVE, wrap=WORD, bd=0)
        text4.place(x=10, y=40, width=380, height=150)
        text4.insert(END, encrypt)
        Label(screen1, text="Enter Whatsapp no. :", font="arial",
        fg="white", bg="#ed3833").place(x=10, y=200)
        text3 = Text(screen1, font="Robote 20", bg="white",
        relief=GROOVE, wrap=WORD, bd=0)
        text3.place(x=10, y=250, width=380, height=100)
        Button(screen1, text="WHATSAPP", height="2", width=46, bg="#1089ff",
        fg="white", bd=0, command=whatsapp).place(x=10, y=375)
        # print(encrypt)
    elif password == "":
        messagebox.showerror("encryption", "Input password")
    elif password != "12345":
        messagebox.showerror("encryption", "Invalid Password")
def main_screen():
    global screen
    global code
    global text1
    screen = Tk()
    screen.geometry("455x418")
    screen.title("App")
    def reset():
        code.set("")
        text1.delete(1.0, END)
    Label(text="Enter text for encryption or decryption",
    fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=435, height=100)
    Label(text="Enter secret key for encryption or decryption",
    fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=(
    "arial", 25), show="*").place(x=10, y=200)
    Button(text="ENCRYPT", height="2", width=25,
    bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=21, y=270)
    Button(text="DECRYPT", height="2", width=25,
    bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=240, y=270)
    Button(text="RESET", height="2", width=53, bg="#1089ff",
    fg="white", bd=0, command=reset).place(x=20, y=350)
    screen.mainloop()
main_screen()
