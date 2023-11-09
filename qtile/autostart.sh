#!/bin/sh
# nm-applet &

# background
~/bin/changewallpapper &

# compositor
picom --config ~/.config/picom/picom.conf &

# sxhkd
sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

# Notifications
dunst &

# power manager
/usr/bin/xfce4-power-manager &

xscreensaver &

# Music
mpd &

# Clipboard manager
# parcellite &

# Blue light filter
~/bin/redshift-on &

# xterm config
# xrdb .Xresources &

# volume
# volumeicon &



