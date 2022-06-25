from os.path import expanduser

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from widgets.owm import OpenWeatherMap
from widgets.volume import MyPulseVolume

from classes import Helpers, Palette

# TODO: Add CPU/Memory/HD to info section?

dpi = Helpers.dpi

widget_defaults = dict(
    background=Palette.colors["base"],
    font="iM WritingQuattroS Nerd Font",
    fontsize=dpi(13),
    foreground=Palette.colors["text"],
    padding=dpi(10),
)
extension_defaults = widget_defaults.copy()

num_screen = int(Helpers.get_num_screen())

sep = widget.Sep(
    foreground=Palette.colors["green"],
    size_percent=100,
)

screens = []

for i in range(0, num_screen):
    screens.extend([
        Screen(
            top=bar.Bar([
                widget.Spacer(
                    background=Palette.colors["green"],
                    length=2,
                ),
                widget.Image(
                    background=Palette.colors["green"],
                    filename=expanduser(
                        "~/.local/share/opensuse/Button-monochrome.png"),
                    margin=dpi(4),
                ),
                widget.CheckUpdates(
                    background=Palette.colors["green"],
                    colour_have_updates=Palette.colors["crust"],
                    custom_command="zypper lu",
                    custom_command_modify=lambda x: x - 4,
                    display_format="{updates} ",
                    mouse_callbacks={
                        "Button1": lazy.spawn("kitty -e sudo zypper dup"),
                    },
                    padding=0,
                    update_interval=14400,
                ),
                widget.CurrentLayoutIcon(
                    # custom_icon_paths=[expanduser(
                    #    "~/.config/qtile/layout-icons/gruvbox-neutral_orange")],
                    padding=dpi(4),
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
                    padding=dpi(10),
                ),
                widget.Spacer(),
                widget.GroupBox(
                    active=Palette.colors["subtext1"],
                    block_highlight_text_color=Palette.colors["green"],
                    borderwidth=0,
                    disable_drag=True,
                    fontsize=dpi(20),
                    hide_unused=True,
                    inactive=Palette.colors["surface1"],
                    padding=dpi(2),
                    rounded=False,
                    urgent_text=Palette.colors["red"],
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
                    padding=dpi(10),
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
                    fontsize=dpi(18),
                    text_closed="",
                    text_open="",
                ),
                widget.Spacer(
                    length=6,
                ),
                widget.Wallpaper(
                    directory=expanduser("~/Pictures/Wallpapers"),
                    fontsize=dpi(16),
                    foreground=Palette.colors["text"],
                    label="",
                    random_selection=True,
                ),
                widget.Spacer(
                    length=4,
                ),
            ],
                background=Palette.colors["base"],
                border_color=Palette.colors["green"],
                border_width=[dpi(1), 0, 0, 0],
                foreground=Palette.colors["text"],
                margin=dpi(5),
                opacity=0.888888880,
                size=dpi(28),
            ),
        )
    ])
