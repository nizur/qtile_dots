from os import environ
from subprocess import PIPE, Popen, run
from libqtile import hook
from libqtile.log_utils import logger
from asyncio import sleep

from classes import AutoStart


@hook.subscribe.startup_once
def redshift():
    Popen(["redshift"])


@hook.subscribe.startup
def autostart():
    AutoStart()


@hook.subscribe.startup_complete
def dbus_register():
    id = environ.get("DESKTOP_AUTOSTART_ID")
    if not id:
        return
    Popen(['dbus-send',
           '--session',
           '--print-reply',
           '--dest=org.gnome.SessionManager',
           '/org/gnome/SessionManager',
           'org.gnome.SessionManager.RegisterClient',
           'string:qtile',
           'string:' + id])


@hook.subscribe.startup_complete
def auto_screens():
    r = run(['sh', '-c', 'xrandr --listactivemonitors | head -n1'],
            stdout=PIPE, universal_newlines=True)
    logger.info(f'Found {r.stdout} displays')


@hook.subscribe.client_new
async def specific_instance_rules(client):
    await sleep(0.01)
    if client.name == "Spotify":
        client.togroup("music")
    elif client.name == "Discord":
        client.togroup("chat")
