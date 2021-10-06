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
	'''Updates the time, checks if alarm should go off'''
	global list_of_alarms
	time  = datetime.now().strftime("%H:%M:%S")
	if list_of_alarms:
		for index, alarm in enumerate(list_of_alarms):
			if time == alarm:
				mixer.music.play(-1)
				stop_alarm_btn.config(state = NORMAL)
				list_of_alarms = list_of_alarms[index:]
				update()

	clock.config(text = time)
	clock.after(1000, getTime)

def alarm():
	'''Manages a Toplevel window where alarm is set'''
	global hour, mnt, sec
	set_alarm_wn = Toplevel(root)
	set_alarm_wn.title("Set Alarm")
	set_alarm_wn.geometry("400x400")

	hour = Entry(set_alarm_wn, width = 5, relief = RAISED)
	hour.grid(row = 0, column = 0, padx = (130, 10), pady = (150, 40))

	mnt = Entry(set_alarm_wn, width = 5, relief = RAISED)
	mnt.grid(row = 0, column = 1, padx = 10, pady = (150, 40))

	sec = Entry(set_alarm_wn, width = 5, relief = RAISED)
	sec.grid(row = 0, column = 2, padx = 10, pady = (150, 40))
	sec.insert(0, '00') # seconds default to '00'

	confirm = Button(set_alarm_wn, text = "Save", command = confirm_alarm, padx = 20)
	confirm.grid(columnspan = 3, padx = (130, 10))

def confirm_alarm():
	'''Obtains the alarm time, adds it to the list'''
	global hour, mnt, sec
	hour_val = hour.get().strip()
	mnt_val = mnt.get().strip()
	sec_val = sec.get().strip()

	list_of_alarms.append(f"{hour_val}:{mnt_val}:{sec_val}")
	update()

def stop_alarm():
	'''Stops the alarm currently going off'''
	mixer.music.stop()
	stop_alarm_btn.config(state = DISABLED)
	list_of_alarms.pop(0)
	update()

def update():
	'''Updates the list of alarms'''
	alarms['text'] = ""
	for alarm in list_of_alarms:
		alarms['text'] += alarm + '\n'

# Tkinter Widgets
clock = Label(root, text = "", font = "ds-digital 80", bg = "black", fg = "cyan")
clock.pack()

alarm_btn = Button(root, text = 'Alarm', padx = 5, command = alarm)
alarm_btn.pack(pady = 10)

stop_alarm_btn = Button(root, text = 'Stop', state = DISABLED, padx = 5, command = stop_alarm)
stop_alarm_btn.pack(pady = 10)

alarms = Label(root, text = "")
alarms.pack(pady = 10)

getTime()

root.mainloop()
