###
# Custom Qtile Config
# - Chris Ruzin
###

# TODO: Integrate dunst?
# TODO: Toggle screensaver
# TODO: Look into EWW
# TODO: Drag/drop files?

from defines import *
from groups import *
from keys import *
from layouts import *
from mouse import *
from screens import *
from hooks import *

try:
    from typing import List  # noqa: F401
except ImportError:
    pass


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
