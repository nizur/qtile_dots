from libqtile.config import DropDown, Group, Match, ScratchPad

groups = [Group(i, label="") for i in "123456789"]

groups.extend([
    ScratchPad("dropdown", [
        DropDown("term", "kitty",
                 height=0.85,
                 on_focus_lost_hide=False,
                 opacity=0.888888880,
                 warp_pointer=False,
                 width=0.9,
                 x=0.05,
                 y=0.05,
                 ),
    ]),
])
