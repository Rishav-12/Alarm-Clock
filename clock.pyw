import PySimpleGUI as sg
import time

import pygame
from pygame import mixer

pygame.init()

try:
	mixer.music.load('Sounds/alarm_tone.mp3')
except pygame.error:
	mixer.music.load('Sounds/alarm_tone.wav')

list_of_alarms = []

def get_time():
	'''Updates the time, checks if alarm should go off'''

	global list_of_alarms
	now = time.strftime("%H:%M:%S")
	window["-TIME-"].update(now)

	if list_of_alarms:
		for index, alarm in enumerate(list_of_alarms):
			if now == alarm:
				mixer.music.play(-1)
				window["Stop"].update(disabled=False)
				list_of_alarms = list_of_alarms[index:]
				update()

def confirm_alarm():
	'''Obtains the alarm time, adds it to the list'''

	hour_val = values["-HR-"]
	minute_val = values["-MIN-"]

	if hour_val and minute_val:
		list_of_alarms.append(f"{hour_val}:{minute_val}:00")
	update()

def stop_alarm():
	'''Stops the alarm currently going off'''

	mixer.music.stop()
	window["Stop"].update(disabled=True)
	list_of_alarms.pop(0)
	update()

def update():
	'''Updates the list of alarms'''

	window["-LST-"].update("")
	for alarm in list_of_alarms:
		window["-LST-"].update(window["-LST-"].get() + alarm + '\t')

clock_layout = [[sg.Text("", key="-TIME-",font=("ds-digital", 100),background_color="black",text_color="cyan")]]

alarm_layout = [[sg.Text("Hour", size=(20, 1)), sg.Text("Minute", size=(20, 1))],
				[sg.Input(key="-HR-", size=(20, 1)), sg.Input(key="-MIN-", size=(20, 1))],
				[sg.Text("", size=(40, 5), key="-LST-")],
				[sg.Button("Confirm", button_color=("white", "black"))],
				[sg.Button("Stop", disabled=True, button_color=("white", "black"))]]

layout = [[sg.TabGroup([[sg.Tab("Clock", clock_layout),
						sg.Tab("Alarm", alarm_layout)]])]]

window = sg.Window('Clock', layout)

while True:
	event, values = window.read(timeout=100)
	if event == sg.WINDOW_CLOSED:
		break
	if event == "Confirm":
		confirm_alarm()
	if event == "Stop":
		stop_alarm()

	get_time()

window.close()
