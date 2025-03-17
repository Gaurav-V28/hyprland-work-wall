#!/usr/bin/python3

# NOTE: To have different wallpapers in different workspaces
import os
import time
import subprocess
# Dump all existing wallpapers
#os.system("hyprctl hyprpaper unload all")


# NOTE: Preload the existing wallpapers
walls = []
for file in os.listdir("/home/gaurav/wallpaper/current"):
    walls.append(file)
walls.sort()
previous = 0

def change(n):
    try:
        os.system(f"hyprctl hyprpaper wallpaper 'eDP-1, /home/gaurav/wallpaper/current/{walls[n]}'")
    except:
        os.system(f"hyprctl hyprpaper wallpaper 'eDP-1, /home/gaurav/wallpaper/current/{walls[-1]}'")
while True:
    current = int(subprocess.check_output("hyprctl monitors | awk '/active/ {print $3}'",shell =True,text=True)[0])
    if current < previous:
        os.system('hyprctl keyword layerrule animation fade left,hyprpaper')
        change(current-1)
        previous = current
    elif current > previous:
        os.system('hyprctl keyword layerrule animation fade right,hyprpaper')
        change(current-1)
        previous = current

    time.sleep(0.1)
               
