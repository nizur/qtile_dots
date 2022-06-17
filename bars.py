from libqtile import bar, widget
from libqtile.lazy import lazy

from commands import Commands, HOME
from themes.mocha import Theme
from widgets.owm import OpenWeatherMap
from widgets.volume import MyPulseVolume

# TODO: Spotify/media control
# TODO: Look into custom systray options

sep = widget.Sep(
    foreground=Theme.colors["base"],
    padding=0,
    size_percent=100,
)

top_bar = bar.Bar([
    widget.Spacer(
        background=Theme.colors["green"],
        length=8,
    ),
    widget.TextBox(
        background=Theme.colors["green"],
        fontsize="24",
        foreground=Theme.colors["black"],
        padding=0,
        text=" ",
    ),
    widget.CheckUpdates(
        background=Theme.colors["green"],
        colour_have_updates=Theme.colors["black"],
        custom_command="zypper lu",
        custom_command_modify=lambda x: x - 4,
        display_format=" {updates}",
        mouse_callbacks={"Button1": lazy.spawn(Commands.zypper_dup)},
        padding=0,
        update_interval=14400,
    ),
    widget.Spacer(
        background=Theme.colors["green"],
        length=4,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[(HOME + "/.config/qtile/icons")],
        foreground=Theme.colors["yellow"],
        padding=4,
        scale=0.4,
    ),
    sep,
    widget.GroupBox(
        active=Theme.colors["blue"],
        # background=Theme.colors["base"],
        block_highlight_text_color=Theme.colors["black"],
        borderwidth=0,
        disable_drag=True,
        highlight_color=Theme.colors["blue"],
        highlight_method="block",
        inactive=Theme.colors["bright_black"],
        rounded=False,
        this_current_screen_border=Theme.colors["blue"],
        urgent_alert_method="block",
        urgent_border=Theme.colors["bright_red"],
        urgent_text=Theme.colors["white"],
    ),
    sep,
    widget.Chord(
        chords_colors={
            "Audio": (Theme.colors["magenta"], Theme.colors["black"]),
            "Gnome": (Theme.colors["green"], Theme.colors["black"]),
            "Grow": (Theme.colors["blue"], Theme.colors["black"]),
            "Migrate": (Theme.colors["cyan"], Theme.colors["black"]),
            "Open": (Theme.colors["yellow"], Theme.colors["black"]),
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
        cursor_color=Theme.colors["red"],
        ignore_dups_history=True,
        prompt=" ",
        visual_bell_color=Theme.colors["red"],
    ),
    widget.Clipboard(
        blacklist=["1password", "1Password"],
        fmt=" {}",
        foreground=Theme.colors["bright_magenta"],
    ),
    widget.WindowCount(
        padding=10,
        text_format=" {num}",
    ),
    sep,
    widget.Mpris2(
        name="spotify",
        objname="org.mpris.MediaPlayer2.spotify",
        persist=True,
        scroll_chars="40",
        stop_pause_text="Paused...",
    ),
    MyPulseVolume(
        foreground=Theme.colors["green"],
        get_volume_command=Commands.audio_get_volume,
        limit_max_volume=True,
        mute_command=Commands.audio_mute,
        step=4,
        volume_app="pamixer",
        volume_down_command=Commands.audio_volume_down,
        volume_up_command=Commands.audio_volume_up,
    ),
    sep,
    OpenWeatherMap(
        api_key="b8c0a2258d0134fb50533560dfb89a73",
        foreground=Theme.colors["cyan"],
        format="{icon} {temp:.0f}{temp_units}",
        latitude=30.2,
        longitude=-97.7,
        units="imperial",
    ),
    sep,
    widget.Clock(
        foreground=Theme.colors["yellow"],
        format=" %a %B %d",
    ),
    sep,
    widget.Clock(
        foreground=Theme.colors["magenta"],
        format=" %I:%M %p",
    ),
    sep,
    widget.Wallpaper(
        directory=HOME + "/Pictures/Wallpapers",
        fontsize=16,
        foreground=Theme.colors["white"],
        label="",
        random=True,
    ),
    widget.Spacer(
        length=2,
    ),
], **Theme.bar)
