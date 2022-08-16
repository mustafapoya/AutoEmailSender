from tkinter import *
import smtplib
import re

root = Tk()
root.title("Email Application")

f1 = Frame(root, width=1000, height=800)
f1.pack(side=TOP)

label1 = Label(f1, width=25, text="Enter your Credentials", font="Calibri 18 bold")
label1.grid(row=0, columnspan=3, pady=10, padx=10)

label2 = Label(f1, text="Email")
label2.grid(row=1, sticky=E, pady=5, padx=10)
label3 = Label(f1, text="Password")
label3.grid(row=2, sticky=E, pady=5, padx=10)

entry1 = Entry(f1)
entry2 = Entry(f1, show='*')

entry1.grid(row=1, column=1, pady=5)
entry2.grid(row=2, column=1, pady=5)

btn1 = Button(f1, text="Login", width=10, bg="black", fg="white", command=lambda: login())
btn1.grid(row=3, columnspan=3, pady=10)


f2 = Frame(root)
f2.pack(side=TOP, expand=NO, fill=NONE)

label4 = Label(f2, width=20, bg="cyan", fg="red", text="Log in Success", font="Calibri 12 bold")
label4.grid(row=0, column=0, columnspan=2, pady=5)

btn2 = Button(f2, text="logout", bg="black", fg="white", command=lambda: logout())
btn2.grid(row=0, column=4, sticky=E, pady=10, padx=(5, 0))

f3 = Frame(master=root)
f3.pack(side=TOP, expand=NO, fill=NONE)

label5 = Label(f3, width=20, text="Compose Email", font="Calibri 12 bold")
label5.grid(row=0, columnspan=3, pady=10)

label6 = Label(f3, text="To")
label6.grid(row=1, sticky=E, pady=5)

label7 = Label(f3, text="Subject")
label7.grid(row=2, sticky=E, pady=5)

label8 = Label(f3, text="Message")
label8.grid(row=3, sticky=E)

entry3 = Entry(f3)
entry4 = Entry(f3)
entry5 = Entry(f3)

entry3.grid(row=1, column=1, pady=5)
entry4.grid(row=2, column=1, pady=5)
entry5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

btn3 = Button(f3, text="Send Email", width=10, bg="black", fg="white", command=lambda: send_mail())
btn3.grid(row=6, columnspan=3, pady=10)

label9 = Label(f3, width=20, fg="white", bg="black", font="Calibri 18 bold")
label9.grid(row=7, columnspan=3, pady=5)

hide_login_label()

root.mainloop()
