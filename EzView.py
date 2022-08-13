import pyautogui
import pydirectinput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import time
from pystyle import *
import os
import httpx, requests, os, sys, threading, random, user_agent
import sys

delay = 1
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

pause = True
running = True

mouse = Controller()

mainhub = """!$! HUB !$!"""

Anime.Fade(Center.Center(mainhub), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=6)

user = input(Colorate.Horizontal(Colors.red_to_green, 'User: '))
os.system(f'title EzView ^| Botting ^| ' + user + ' ^| github/EXCET ^| V2')

views = 10

print("Go to Your Github Profile")
print("Press s To Start And h To Stop")

def start():
    for i in range(views):
         pyautogui.hotkey('ctrl', 'r') 
         time.sleep(delay)

def exitt():
    quit()

def on_press(key):
    if key == start_stop_key:
        pause = False
        print("[STARTED]")
        start()
        time.sleep(99999999)
    elif key == exit_key:
        running = False
        print("[STOPPED]")
        exitt()

with Listener(on_press=on_press) as listener:
    listener.join()