hyprctl hyprpaper unload all
for i in $(ls ~/wallpaper/current);
do 
    hyprctl hyprpaper preload /home/gaurav/wallpaper/current/$i 
done
python3 load.py
