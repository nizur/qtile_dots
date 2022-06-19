from os.path import expanduser

from libqtile import bar, widget
from libqtile.config import Screen

from widgets.owm import OpenWeatherMap
from widgets.volume import MyPulseVolume

from classes import Helpers, Palette

widget_defaults = dict(
    background=Palette.colors["base"],
    font="iM WritingQuattroS Nerd Font",
    fontsize=13,
    foreground=Palette.colors["text"],
    padding=10,
)
extension_defaults = widget_defaults.copy()

sep = widget.Sep(
    foreground=Palette.colors["base"],
    padding=0,
    size_percent=100,
)

num_screen = int(Helpers.get_num_screen())

screens = []

for i in range(0, num_screen):
    screens.extend([
        Screen(
            top=bar.Bar([
                widget.Spacer(
                    background=Palette.colors["green"],
                    length=8,
                ),
                widget.TextBox(
                    background=Palette.colors["green"],
                    fontsize="24",
                    foreground=Palette.colors["crust"],
                    padding=0,
                    text=" ",  # OpenSUSE!
                ),
                widget.CheckUpdates(
                    background=Palette.colors["green"],
                    colour_have_updates=Palette.colors["crust"],
                    custom_command="zypper lu",
                    custom_command_modify=lambda x: x - 4,
                    display_format="{updates}",
                    padding=0,
                    update_interval=14400,
                ),
                widget.Spacer(
                    background=Palette.colors["green"],
                    length=8,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[(expanduser("~/.config/qtile/icons"))],
                    foreground=Palette.colors["yellow"],
                    padding=4,
                    scale=0.4,
                ),
                sep,
                widget.GroupBox(
                    active=Palette.colors["blue"],
                    # background=Palette.colors["base"],
                    block_highlight_text_color=Palette.colors["crust"],
                    borderwidth=0,
                    disable_drag=True,
                    highlight_color=Palette.colors["blue"],
                    highlight_method="block",
                    inactive=Palette.colors["surface1"],
                    rounded=False,
                    this_current_screen_border=Palette.colors["blue"],
                    urgent_alert_method="block",
                    urgent_border=Palette.colors["maroon"],
                    urgent_text=Palette.colors["crust"],
                ),
                sep,
                widget.Chord(
                    chords_colors={
                        "Audio": (Palette.colors["peach"], Palette.colors["crust"]),
                        "Gnome": (Palette.colors["green"], Palette.colors["crust"]),
                        "Grow": (Palette.colors["blue"], Palette.colors["crust"]),
                        "Migrate": (Palette.colors["sapphire"], Palette.colors["crust"]),
                        "Open": (Palette.colors["yellow"], Palette.colors["crust"]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.WindowName(
                    for_current_screen=True,
                    padding=10,
                ),
                widget.Spacer(),
                widget.Prompt(
                    bell_style="visual",
                    cursor_color=Palette.colors["red"],
                    ignore_dups_history=True,
                    prompt=" ",
                    visual_bell_color=Palette.colors["red"],
                ),
                widget.Clipboard(
                    blacklist=["1password", "1Password"],
                    fmt=" {}",
                    foreground=Palette.colors["flamingo"],
                ),
                widget.WindowCount(
                    padding=10,
                    text_format=" {num}",
                ),
                sep,
                MyPulseVolume(
                    foreground=Palette.colors["sapphire"],
                    get_volume_command="pamixer --get-volume-human",
                    limit_max_volume=True,
                    mute_command="pamixer -m",
                    step=4,
                    volume_app="pamixer",
                    volume_down_command="pamixer -d 4",
                    volume_up_command="pamixer -i 4",
                ),
                sep,
                OpenWeatherMap(
                    api_key="b8c0a2258d0134fb50533560dfb89a73",
                    foreground=Palette.colors["green"],
                    format="{icon} {temp:.0f}{temp_units}",
                    latitude=30.2,
                    longitude=-97.7,
                    units="imperial",
                ),
                sep,
                widget.Clock(
                    foreground=Palette.colors["yellow"],
                    format=" %a %B %d",
                ),
                sep,
                widget.Clock(
                    foreground=Palette.colors["peach"],
                    format=" %I:%M %p",
                ),
                sep,
                widget.Wallpaper(
                    directory=expanduser("~/Pictures/Wallpapers"),
                    fontsize=16,
                    foreground=Palette.colors["text"],
                    label="",
                    random_selection=True,
                ),
                widget.Spacer(
                    length=2,
                ),
                sep,
                widget.Spacer(
                    length=6,
                ),
                widget.WidgetBox(
                    widgets=[
                        widget.Spacer(
                            length=6,
                        ),
                        widget.TextBox(
                            background=Palette.colors["base"],
                            foreground=Palette.colors["green"],
                            text=" " + Helpers.get_os_release(),
                        ),
                        widget.Spacer(
                            length=2,
                        ),
                        widget.TextBox(
                            background=Palette.colors["base"],
                            foreground=Palette.colors["yellow"],
                            text=" " + Helpers.get_kernel_release(),
                        ),
                        widget.Systray(),
                    ],
                    fontsize=18,
                    foreground=Palette.colors["red"],
                    text_closed="",
                    text_open=""
                ),
                widget.Spacer(
                    length=8,
                ),
            ],
                background=Palette.colors["crust"],
                foreground=Palette.colors["text"],
                size=32,
                opacity=0.888888880,
            ),
        )
    ])
