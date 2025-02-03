#!/usr/bin/python3

# NOTE: To have different wallpapers in different workspaces
import os
import time
# Dump all existing wallpapers
os.system("hyprctl hyprpaper unload")

# NOTE: Preload the existing wallpapers
walls = []
for file in os.listdir("current"):
    os.system(f"hyprctl hyprpaper preload '/home/gaurav/wallpaper/current/{file}'")
    walls.append(file)
    walls.sort()
previous = 0

def change(n):
    os.system(f"hyprctl hyprpaper wallpaper 'eDP-1, /home/gaurav/wallpaper/current/{walls[n]}'")
   
while True:
    os.system("hyprctl monitors | awk '/active/ {print $3}' > workspace")
    with open("workspace",'r') as f:
        dummy = [line for line in f]
    current = int(dummy[0][0])
    if current < previous:
        os.system('hyprctl keyword layerrule animation fade left,hyprpaper')
        #os.system('hyprctl keyword layerrule animation slide left layersOut,hyprpaper')
        change(current-1)
        previous = current
    elif current > previous:
        os.system('hyprctl keyword layerrule animation fade right,hyprpaper')
        #os.system('hyprctl keyword layerrule animation slide right layersOut,hyprpaper')

        change(current-1)
        previous = current

    time.sleep(0.1)
               
