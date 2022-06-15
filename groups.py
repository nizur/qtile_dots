from libqtile.config import Group, Key, KeyChord, Match
from libqtile.lazy import lazy

from keys import keys, MOD, SHIFT
from layouts import layouts
from themes.dracula import Theme


### GROUPS ###

group_configs = (
    ("", {
        "matches": [Match(wm_class=["Firefox"])],
        "spawn": ["firefox"],
    }),
    ("", {
        "layout": layouts[2].name,
        "matches": [Match(wm_class=["Alacritty"])],
        "spawn": ["alacritty"],
    }),
    ("", {
        "layout": layouts[1].name,
        "matches": [Match(wm_class=["Code"])],
        "spawn": ["code"],
    }),
    ("", {
        "layout": layouts[1].name,
    }),
    ("", {
        "layout": layouts[1].name,
        "matches": [Match(wm_class=["Discord"])],  # FIXME
    }),
    ("", {
        "layout": layouts[1].name,
        "matches": [Match(wm_class=["Spotify"])],  # FIXME
    }),
    ("", {
        "layout": layouts[1].name,
        "matches": [Match(wm_class=["Gimp-2.10"])],
    }),
    ("﮼", {
        "layout": layouts[2].name,
    }),
)

groups = []

for i, (group, config) in enumerate(group_configs, 1):
    groups.append(Group(group, **config))
    keys.extend([
        Key([MOD], str(i), lazy.group[group].toscreen(),
            desc="Switch to group {}".format(group)),
        Key([MOD, SHIFT], str(i), lazy.window.togroup(group, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group))
    ])
