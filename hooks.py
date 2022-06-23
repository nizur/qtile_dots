from os import environ
from psutil import Process
from subprocess import PIPE, Popen, run
from libqtile import qtile, hook
from libqtile.log_utils import logger

from classes import AutoStart, Helpers


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


@hook.subscribe.screen_change
def set_screens(event):
    if event:
        run(["autorandr", "--change"])
    qtile.restart()


@hook.subscribe.client_new
def app_to_group_router(window):
    pid = window.get_pid()
    name = Process(pid).name().lower()
    if "spotify" in name:
        window.togroup("music")
    elif "discord" in name:
        window.togroup("chat")
    elif "pcloud" in name:
        window.togroup("misc")
    elif "rcu_gp" in name:  # Logseq registers as rcu_gp for some reason
        window.togroup("misc")

# @hook.subscribe.client_new
# def update_group_on_new(w):
#     Helpers.update_group(window=w)


# @hook.subscribe.client_killed
# def update_group_on_kill(w):
#     Helpers.update_group(window=w)

    # TODO: Go to or spawn app/group
    # TODO: Have generic groups. When specific apps are opened
    #   inside a group, the label changes to an associated icon
    #   to indicate where that app is. When the app is closed
    #   the group label reverts back to the default icon
