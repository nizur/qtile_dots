from libqtile.config import DropDown, Group, Match, ScratchPad


groups = [
    Group(
        exclusive=True,
        name="web",
        label="",
        layout="max",
        matches=[Match(wm_instance_class=["firefox", "Firefox", "Navigator"])],
        spawn=["firefox"],
    ),
    Group(
        exclusive=True,
        name="tty",
        label="",
        layout="columns",
        matches=[Match(wm_instance_class=["alacritty", "kitty", "Kitty"])],
    ),
    Group(
        exclusive=True,
        name="dev",
        label="",
        layout="max",
        matches=[Match(wm_instance_class=["code", "Code"])],
    ),
    Group(
        exclusive=True,
        name="mail",
        label="",
        layout="max",
        matches=[Match(wm_instance_class="geary")],
    ),
    Group(
        exclusive=True,
        name="chat",
        label="",
        layout="max",
        matches=[Match(wm_instance_class=["Discord", "discord"])],
    ),
    Group(
        exclusive=True,
        name="music",
        label="",
        layout="max",
        matches=[Match(wm_instance_class=["Spotify", "spotify"])],
    ),
    Group(
        exclusive=True,
        name="media",
        label="",
        layout="max",
        matches=[Match(wm_class=["Gimp-2.10"])],
    ),
    Group(
        name="misc",
        label="ﯢ",
        layout="columns",
    ),
    ScratchPad("dropdown", [
        DropDown("term", "kitty",
                 height=0.85,
                 on_focus_lost_hide=False,
                 opacity=1,
                 warp_pointer=False,
                 width=0.9,
                 x=0.05,
                 y=0.05,
                 ),
    ]),
]

# for i, (group, config) in enumerate(group_configs, 1):
#     groups.append(Group(group, **config))
#     keys.extend([
#         Key([MOD], str(i), lazy.group[group].toscreen(),
#             desc="Switch to group {}".format(group)),
#         Key([MOD, SHIFT], str(i), lazy.window.togroup(group, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(group))
#     ])
