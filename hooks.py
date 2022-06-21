from os import environ
from subprocess import PIPE, Popen, run
from libqtile import qtile, hook
from libqtile.log_utils import logger
from asyncio import sleep

from classes import AutoStart


@hook.subscribe.startup_once
def redshift():
    Popen(["redshift"])


@hook.subscribe.startup
def autostart():
    AutoStart()


@hook.subscribe.startup
def dbus_register():
    id = environ.get("DESKTOP_AUTOSTART_ID")
    logger.warning(f"DESKTOP_AUTOSTART_ID = {id}")
    if not id:
        return
    Popen(["dbus-send",
           "--session",
           "--print-reply",
           "--dest=org.gnome.SessionManager",
           "/org/gnome/SessionManager",
           "org.gnome.SessionManager.RegisterClient",
           "string:qtile",
           f"string:{id}"])


@hook.subscribe.startup_complete
def auto_screens():
    r = run(["sh", "-c", "xrandr --listactivemonitors | head -n1"],
            stdout=PIPE, universal_newlines=True)
    r = r.stdout.replace("\n", "")
    logger.warning(f"{r} Found")


@hook.subscribe.client_new
def specific_instance_rules(client):
    if client.name == "Spotify":
        client.togroup("music")
    elif client.name == "Discord":
        client.togroup("chat")


@hook.subscribe.screen_change
def set_screens(event):
    if event:
        run(["autorandr", "--change"])
    qtile.restart()


# TODO: Get pcloud to run in background on startup
# TODO: Go to or spawn app/group
# TODO: Have generic groups. When specific apps are opened
#   inside a group, the label changes to an associated icon
#   to indicate where that app is. When the app is closed
#   the group label reverts back to the default icon
