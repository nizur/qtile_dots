from libqtile import layout
from libqtile.config import Match

from themes.mocha import Theme

layouts = [
    layout.MonadTall(
        **Theme.layout["Base"],
        **Theme.layout["MonadTall"],
    ),
    layout.Max(
        **Theme.layout["Base"],
    ),
    layout.Columns(
        **Theme.layout["Base"],
        **Theme.layout["Columns"],
        fair=True,
    ),
    layout.Tile(
        **Theme.layout["Base"],
    ),
]

floating_layout = layout.Floating(
    **Theme.layout["Base"],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
)
