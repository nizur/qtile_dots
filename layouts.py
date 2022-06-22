from libqtile import layout
from libqtile.config import Match

from classes import Palette

base_layout_config = {
    "border_focus": Palette.colors["green"],
    "border_normal": Palette.colors["crust"],
    "border_on_single": False,
    "border_width": 3,
    "margin": [0, 5, 5, 5],
    "single_border_width": 0,
}

cols_layout_config = {
    "border_focus_stack": Palette.colors["green"],
    "border_normal_stack": Palette.colors["crust"],
}

layouts = [
    layout.Bsp(
        **base_layout_config,
    ),
    layout.Max(
        **base_layout_config,
    ),
    layout.Columns(
        **base_layout_config,
        **cols_layout_config,
    ),
]

floating_layout = layout.Floating(
    **base_layout_config,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pcloud"),
        Match(wm_class="gcr-prompter"),
        Match(wm_class="gnome-screenshot"),
    ],
)
