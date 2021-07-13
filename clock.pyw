from tkinter import *
from datetime import datetime
import pygame
from pygame import mixer

root = Tk()
root.title("Clock")

pygame.init()

try:
	mixer.music.load('alarm_tone.mp3')
except pygame.error:
	mixer.music.load('alarm_tone.wav')

alarm_time = ""

def getTime():
	'''This function updates the time and checks if it matches the alarm time.
	If it matches, the alarm sound is played'''
	time  = datetime.now().strftime("%H:%M:%S")
	if time == alarm_time:
		mixer.music.play(-1)
		stopAlarm.config(state = NORMAL)
	label.config(text = time)
	label.after(1000, getTime)

def alarm():
	'''Function to set the alarm time in a Toplevel window'''
	global hour, mint, sec
	top = Toplevel(root)
	top.title("Set An Alarm")
	top.geometry("400x400")

	hour = Entry(top, width = 5, relief = RAISED)
	hour.grid(row = 0, column = 0, padx = (130, 10), pady = (150, 40))

	mint = Entry(top, width = 5, relief = RAISED)
	mint.grid(row = 0, column = 1, padx = 10, pady = (150, 40))

	sec = Entry(top, width = 5, relief = RAISED)
	sec.grid(row = 0, column = 2, padx = 10, pady = (150, 40))

	confirm = Button(top, text = "Set", command = confirmAlarm, padx = 20)
	confirm.grid(columnspan = 3, padx = (130, 10))

def confirmAlarm():
	'''This function obtains and sets the alarm time'''
	global hour, mint, sec, alarm_time
	hour_val = hour.get().strip()
	mint_val = mint.get().strip()
	sec_val = sec.get().strip()

	alarm_time = f"{hour_val}:{mint_val}:{sec_val}"

def stopAlarm():
	mixer.music.stop()

# Tkinter Widgets
label = Label(root, text = "", font = "ds-digital 80", bg = "black", fg = "cyan")
label.pack()

setAlarm = Button(root, text = 'Alarm', padx = 5, command = alarm)
setAlarm.pack(pady = 10)

stopAlarm = Button(root, text = 'Stop', state = DISABLED, padx = 5, command = stopAlarm)
stopAlarm.pack(pady = 10)

getTime()

root.mainloop()
