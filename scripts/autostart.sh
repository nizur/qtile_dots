#!/bin/sh

exec gsettings set org.gnome.desktop.interface gtk-theme "Catppuccin-blue" &
exec gsettings set org.gnome.desktop.wm.preferences theme "Catppuccin-blue" &
exec gsettings set org.gnome.desktop.interface icon-theme "Newaita-reborn-dark" &
exec xrdb -merge ~/.Xresources &
exec dex --autostart --environment qtile &
exec pcloud
