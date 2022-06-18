import os

from subprocess import check_output


HOME = os.path.expanduser("~")
AUTOSTART_ID = os.environ.get("DESKTOP_AUTOSTART_ID")


class Commands(object):
    audio_get_volume = "pamixer --get-volume-human"
    audio_mute = "pamixer -m"
    audio_play_pause = ""  # FIXME
    audio_track_next = ""  # FIXME
    audio_track_prev = ""  # FIXME
    audio_volume_down = "pamixer -d 2"
    audio_volume_up = "pamixer -i 2"
    autostart = HOME + "/.config/qtile/scripts/autostart.sh"
    browser = "firefox"
    #powermenu = "rofi -show power-menu -modi power-menu:rofi-power-menu"
    calc = "rofi -modi calc -show calc -no-show-match -no-bold"
    code = "code"
    discord = "discord"
    files = "nautilus"
    gnome_session = "dbus-send --session --print-reply --dest=org.gnome.SessionManager /org/gnome/SessionManager org.gnome.SessionManager.RegisterClient string:qtile string:"
    #menu = HOME + "/.config/rofi/launchers/ribbon/launcher.sh"
    menu = "rofi -show drun"
    redshift = "redshift"
    screenshot = "scrot '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $" + \
        HOME + "/Pictures/Screenshots'"
    #spotify_next = HOME + "/.config/qtile/scripts/spotify_next.sh"
    #spotify_prev = HOME + "/.config/qtile/scripts/spotify_prev.sh"
    terminal = "kitty"

    def get_kernel_release():
        return check_output(["uname", "-r"]).decode("utf-8").replace("\n", "")

    def get_os_release():
        return check_output(["lsb-release", "-rs"]).decode("utf-8").replace("\n", "")
