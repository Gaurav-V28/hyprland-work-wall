import os
files = sorted([f'/home/gaurav/wallpaper/current/{file}' for file in os.listdir('current')])
with open("/home/gaurav/.config/hypr/hyprpaper.conf","w") as f:
    for file in files:
        f.write(f"preload = {file} \n")
    f.write(f"wallpaper = eDP-1, {files[0]} \n")
