import tkinter as tk
import csv
import sys
import os.path
from tkinter import messagebox
from Calendar import Calendar
from CalendarWork import CalendarWork

root = tk.Tk()
root.title("Holiday World")

username = tk.StringVar()
password = tk.StringVar()
name = tk.StringVar()
loggedInLabel = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()

def setup():
	file_exists = os.path.isfile("users.txt")
	if file_exists:
		pass
	else:
		file = open("users.txt", "w+")
		file.close()
	file_exists = os.path.isfile("appointments.txt")
	if file_exists:
		pass
	else:
		file = open("appointments.txt", "w+")
		file.close()
def raiseFrame(frame):
	frame.tkraise()
def moveToReg():
	raiseFrame(regFrame)
def moveToLogin():
	raiseFrame(start)
def moveToBook():
	raiseFrame(bookAppointment)

def moveToUser():
	raiseFrame(userFrame)
def register():
	entries = []
	with open ("users.txt",'a',newline="") as userFile:
		writer = csv.writer(userFile)
		writeList = [name.get(),username.get(),password.get()]
		writer.writerow(writeList)
		userFile.close()
	username.set("")
	password.set("")
	raiseFrame(start)
	
def makeAppointment(calendarWorkFrame):
	date = str(datePickercalendar.day_selected)+"/"+str(datePickercalendar.month_selected)+"/"+str(datePickercalendar.year_selected)
	minutesString=str(minutes.get())
	if minutes.get()==0:
		minutesString = "00"
	time = str(hours.get())+":"+minutesString
	with open ("appointments.txt",'a',newline="") as appFile:
		writer = csv.writer(appFile)
		writeList = [name.get(),date,time]
		writer.writerow(writeList)
		appFile.close()
	messagebox.showinfo("See you soon!","Appointment booked")
	CalendarWorkFrame = tk.Frame(userFrame, borderwidth=5, bg="white")
	CalendarWorkFrame.grid(row=2, column=1, columnspan=5)
	WorkCalendar = CalendarWork(CalendarWorkFrame, {name.get()})
	raiseFrame(userFrame)
	
def login():
	with open("users.txt",'r') as userFile:
		reader = csv.reader(userFile)
		for row in reader:
			if len(row)>0:
				if username.get()==row[1] and password.get()==row[2]:
					print(row[0]+" has logged in!")
					loggedInLabel.set("Welcome,Holiday World Booking" +row[0])
					global CalendarWorkFrame
					CalendarWorkFrame = tk.Frame(userFrame, borderwidth=5, bg="white")
					CalendarWorkFrame.grid(row=2, column=1, columnspan=5)
					WorkCalendar = CalendarWork(CalendarWorkFrame, {row[0]})
					name.set(row[0])
					raiseFrame(userFrame)
					
def logOut():
	name.set("")
	username.set("")
	password.set("")
	raiseFrame(start)

setup()
start = tk.Frame(root)
regFrame = tk.Frame(root)
userFrame = tk.Frame(root)
bookAppointment = tk.Frame(root)
frameList=[start,regFrame,userFrame,bookAppointment]
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='white')

tk.Label(start,text="Holiday World",font=("arial", 30),bg='blue').grid(row=1,column=2,columnspan=3)
tk.Label(start,text="Username: ",font=("arial", 22),bg='white').grid(row=2,column=1)
tk.Label(start,text="Password: ",font=("arial", 22),bg='white').grid(row=3,column=1)

tk.Label(regFrame,text="Register page for Holiday World",font=("arial", 22),bg='blue').grid(row=1,column=2,columnspan=3)
tk.Label(regFrame,text="Name: ",font=("arial", 22),bg='white').grid(row=2,column=1)
tk.Label(regFrame,text="Username: ",font=("arial", 22),bg='white').grid(row=3,column=1)
tk.Label(regFrame,text="Password: ",font=("arial", 22),bg='white').grid(row=4,column=1)

tk.Label(userFrame,textvariable = loggedInLabel,font=("arial", 44),bg='white',fg="black").grid(row=1,column=1,columnspan=5)

tk.Label(bookAppointment,text="Book an Appointment",font=("arial", 44),bg='white').grid(row=1,column=1,columnspan=5)
tk.Label(bookAppointment,text="Select a Date: ",font=("arial", 22),bg='white').grid(row=2,column=1)
tk.Label(bookAppointment,text="Select a Time: ",font=("arial", 22),bg='white').grid(row=3,column=1)

tk.Entry(start,textvariable=username,font=("arial", 22),bg='red').grid(row=2,column=2)
tk.Entry(start,textvariable=password,font=("arial", 22),bg='yellow').grid(row=3,column=2)

tk.Entry(regFrame,textvariable=name,font=("arial", 22),bg='red').grid(row=2,column=2)
tk.Entry(regFrame,textvariable=username,font=("arial", 22),bg='yellow').grid(row=3,column=2)
tk.Entry(regFrame,textvariable=password,font=("arial", 22),bg='blue').grid(row=4,column=2)

tk.Button(start,font=("arial", 22),bg='red',text="Login",command=login).grid(row=4,column=2)
tk.Button(start,font=("arial", 22),bg='yellow',text="Register",command=moveToReg).grid(row=4,column=1)

tk.Button(regFrame,font=("arial", 22),bg='red',text="Register",command=register).grid(row=5,column=2)
tk.Button(regFrame,font=("arial", 22),bg='yellow',text="Back",command=moveToLogin).grid(row=5,column=1)

tk.Button(userFrame,font=("arial", 22),bg='red',text="Log Out",command=logOut).grid(row=3,column=1)
tk.Button(userFrame,font=("arial", 22),bg='yellow',text="Book Appointment",command=moveToBook).grid(row=3,column=2)

tk.Button(bookAppointment,font=("arial", 22),bg='red',text="Book an Appointment",command=lambda :makeAppointment(CalendarWorkFrame)).grid(row=5,column=2)
tk.Button(bookAppointment,font=("arial", 22),bg='yellow',text="Back",command=moveToUser).grid(row=5,column=1)



timeSelectFrame = tk.Frame(bookAppointment,borderwidth=5,bg="white")
timeSelectFrame.grid(row=3,column=2)
tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="white",width=2,textvariable=hours).grid(row=1,column=1)
tk.Label(timeSelectFrame,text=":",bg="white").grid(row=1,column=2)
tk.Spinbox(timeSelectFrame,width=2,textvariable=minutes,values=(0,15,30,45),bg="white").grid(row=1,column=3)

CalendarFrame = tk.Frame(bookAppointment, borderwidth=5, bg="white")
CalendarFrame.grid(row=2, column=2, columnspan=5)
datePickercalendar = Calendar(CalendarFrame, {})

raiseFrame(start)
root.mainloop()
