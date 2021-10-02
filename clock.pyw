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

list_of_alarms = []

def getTime():
	'''This function updates the time and checks if it matches the alarm time.
	If it matches, the alarm sound is played'''
	global list_of_alarms
	time  = datetime.now().strftime("%H:%M:%S")
	if list_of_alarms:
		for index, alarm in enumerate(list_of_alarms):
			if time == alarm:
				mixer.music.play(-1)
				stopAlarm.config(state = NORMAL)
				list_of_alarms = list_of_alarms[index:]
				update()

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
	global hour, mint, sec
	hour_val = hour.get().strip()
	mint_val = mint.get().strip()
	sec_val = sec.get().strip()

	list_of_alarms.append(f"{hour_val}:{mint_val}:{sec_val}")
	update()

def stopAlarm():
	mixer.music.stop()
	stopAlarm.config(state = DISABLED)
	list_of_alarms.pop(0)
	update()

def update():
	alarms['text'] = ""
	for alarm in list_of_alarms:
		alarms['text'] += alarm + '\n'

# Tkinter Widgets
label = Label(root, text = "", font = "ds-digital 80", bg = "black", fg = "cyan")
label.pack()

setAlarm = Button(root, text = 'Alarm', padx = 5, command = alarm)
setAlarm.pack(pady = 10)

stopAlarm = Button(root, text = 'Stop', state = DISABLED, padx = 5, command = stopAlarm)
stopAlarm.pack(pady = 10)

alarms = Label(root, text = "")
alarms.pack(pady = 10)

getTime()

root.mainloop()
