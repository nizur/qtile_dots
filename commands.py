import os

from libqtile.utils import guess_terminal

HOME = os.path.expanduser("~")


class Commands(object):
    autostart = HOME + "/.config/qtile/scripts/autostart.sh"
    browser = "firefox"
    #powermenu = "rofi -show power-menu -modi power-menu:rofi-power-menu"
    calc = "rofi -modi calc -show calc -no-show-match -no-bold"
    code = "code"
    discord = "discord"
    files = "nautilus"
    menu = HOME + "/.config/rofi/launchers/ribbon/launcher.sh"
    redshift = "redshift"
    screenshot = "scrot '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $" + \
        HOME + "/Pictures/Screenshots'"
    spotify_next = HOME + "/.config/qtile/scripts/spotify_next.sh"
    spotify_prev = HOME + "/.config/qtile/scripts/spotify_prev.sh"
    terminal = guess_terminal()
    zypper_dup = terminal + " -e sudo zypper dup"
