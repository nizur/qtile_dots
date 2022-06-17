#!/bin/sh

exec gsettings set org.gnome.desktop.interface gtk-theme "Catppuccin-green" &
exec gsettings set org.gnome.desktop.wm.preferences theme "Catppuccin-green" &
exec gsettings set org.gnome.desktop.interface icon-theme "Newaita-reborn-mint-dark" &
exec xrdb -merge ~/.Xresources &
exec dex --autostart --environment qtile
