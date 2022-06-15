###
# Custom Qtile Config
# - Chris Ruzin
###

# TODO: Integrate dunst?
# TODO: Toggle screensaver

import asyncio
import os
import subprocess

from typing import List  # noqa: F401

from libqtile import hook

from commands import Commands
from groups import groups, layouts
from keys import keys
from layouts import floating_layout, layouts
from mouse import mouse
from screens import screens
from themes.dracula import Theme


@hook.subscribe.startup
def dbus_register():
    id = os.environ.get('DESKTOP_AUTOSTART_ID')
    if not id:
        return
    subprocess.Popen([Commands.gnome_session + id])


@hook.subscribe.startup
def autostart():
    # subprocess.call([Commands.redshift])
    subprocess.Popen([Commands.autostart])


@hook.subscribe.client_new
async def move_spotify(client):
    await asyncio.sleep(0.01)
    if client.name == 'Spotify':
        client.togroup('music')
    elif client.name == 'Discord':
        client.togroup("chat")
    elif client.name == 'Logseq':
        client.togroup('misc')


widget_defaults = dict(Theme.widget)
extension_defaults = widget_defaults.copy()

auto_fullscreen = True
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
