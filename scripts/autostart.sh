#!/bin/sh

exec gsettings set org.gnome.desktop.interface gtk-theme "Dracula" &
exec gsettings set org.gnome.desktop.wm.preferences theme "Dracula" &
exec gsettings set org.gnome.desktop.interface icon-theme "Newaita-reborn-dracula-dark" &
exec xrdb -merge ~/.Xresources &
exec dex --autostart --environment qtile
