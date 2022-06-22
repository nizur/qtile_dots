from os.path import expanduser

from libqtile import bar, qtile, widget
from libqtile.config import Screen

from widgets.owm import OpenWeatherMap
from widgets.volume import MyPulseVolume

from classes import Helpers, Palette

# TODO: Add CPU/Memory/HD to info section?

widget_defaults = dict(
    background=Palette.colors["base"],
    font="iM WritingQuattroS Nerd Font",
    fontsize=13,
    foreground=Palette.colors["text"],
    padding=10,
)
extension_defaults = widget_defaults.copy()

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
                    padding=4,
                    update_interval=14400,
                ),
                widget.CurrentLayoutIcon(
                    # custom_icon_paths=[expanduser(
                    #    "~/.config/qtile/layout-icons/gruvbox-neutral_orange")],
                    foreground=Palette.colors["green"],
                    padding=4,
                    scale=0.5,
                ),
                widget.Chord(
                    chords_colors={
                        "Audio": (Palette.colors["peach"], Palette.colors["crust"]),
                        "Gnome": (Palette.colors["mauve"], Palette.colors["crust"]),
                        "Grow": (Palette.colors["blue"], Palette.colors["crust"]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.WindowName(
                    for_current_screen=True,
                    padding=10,
                ),
                widget.Spacer(),
                widget.GroupBox(
                    active=Palette.colors["green"],
                    block_highlight_text_color=Palette.colors["crust"],
                    borderwidth=0,
                    disable_drag=True,
                    highlight_color=Palette.colors["green"],
                    highlight_method="block",
                    inactive=Palette.colors["surface2"],
                    rounded=False,
                    this_current_screen_border=Palette.colors["green"],
                    urgent_alert_method="block",
                    urgent_border=Palette.colors["red"],
                    urgent_text=Palette.colors["crust"],
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
                OpenWeatherMap(
                    api_key="b8c0a2258d0134fb50533560dfb89a73",
                    foreground=Palette.colors["green"],
                    format="{icon} {temp:.0f}{temp_units}",
                    latitude=30.2,
                    longitude=-97.7,
                    units="imperial",
                ),
                widget.Clock(
                    foreground=Palette.colors["yellow"],
                    format=" %a %B %d",
                ),
                widget.Clock(
                    foreground=Palette.colors["peach"],
                    format=" %I:%M %p",
                ),
                widget.Spacer(
                    length=6,
                ),
                widget.WidgetBox(
                    widgets=[
                        widget.TextBox(
                            background=Palette.colors["surface0"],
                            foreground=Palette.colors["green"],
                            text=" " + Helpers.get_os_release(),
                        ),
                        widget.TextBox(
                            background=Palette.colors["surface0"],
                            foreground=Palette.colors["yellow"],
                            text=" " + Helpers.get_kernel_release(),
                        ),
                        widget.Systray(
                            background=Palette.colors["surface0"],
                        ),
                        widget.Spacer(
                            background=Palette.colors["surface0"],
                            length=6,
                        ),
                    ],
                    fontsize=18,
                    text_closed="",
                    text_open="",
                ),
                widget.Spacer(
                    length=4,
                ),
                widget.Wallpaper(
                    directory=expanduser("~/Pictures/Wallpapers"),
                    fontsize=16,
                    foreground=Palette.colors["text"],
                    label="",
                    random_selection=True,
                ),
                widget.Spacer(
                    length=4,
                ),
            ],
                background=Palette.colors["crust"],
                border_color=Palette.colors["green"],
                border_width=[3, 0, 0, 0],
                foreground=Palette.colors["text"],
                margin=5,
                size=32,
                opacity=0.888888880,
            ),
        )
    ])
