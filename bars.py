from libqtile import bar, widget

from commands import Commands, HOME
from themes.andromeda import Theme
from widgets.owm import OpenWeatherMap
from widgets.volume import MyPulseVolume

# TODO: Spotify/media control
# TODO: Look into custom systray options
# TODO: Find a better Dracula GTK theme

sep = widget.Sep(
    foreground=Theme.color["base"],
    padding=0,
    size_percent=100,
)

top_bar = bar.Bar([
    widget.Spacer(
        background=Theme.color["green"],
        length=8,
    ),
    widget.TextBox(
        background=Theme.color["green"],
        fontsize="24",
        foreground=Theme.color["black"],
        padding=0,
        text=" ",
    ),
    widget.CheckUpdates(
        background=Theme.color["green"],
        colour_have_updates=Theme.color["black"],
        custom_command="zypper lu",
        custom_command_modify=lambda x: x - 4,
        display_format=" {updates}",
        mouse_callbacks={"Button1": Commands.zypper_dup},
        padding=0,
        update_interval=14400,
    ),
    widget.Spacer(
        background=Theme.color["green"],
        length=8,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[(HOME + "/.config/qtile/icons")],
        foreground=Theme.color["blue"],
        padding=4,
        scale=0.4,
    ),
    sep,
    widget.GroupBox(
        active=Theme.color["bright_magenta"],
        # background=Theme.color["base"],
        block_highlight_text_color=Theme.color["black"],
        borderwidth=0,
        disable_drag=True,
        highlight_color=Theme.color["bright_magenta"],
        highlight_method="block",
        inactive=Theme.color["bright_black"],
        rounded=False,
        this_current_screen_border=Theme.color["bright_magenta"],
        urgent_alert_method="block",
        urgent_border=Theme.color["bright_red"],
        urgent_text=Theme.color["white"],
    ),
    sep,
    widget.Chord(
        chords_colors={
            "Audio": (Theme.color["magenta"], Theme.color["black"]),
            "Gnome": (Theme.color["green"], Theme.color["black"]),
            "Grow": (Theme.color["blue"], Theme.color["black"]),
            "Migrate": (Theme.color["cyan"], Theme.color["black"]),
            "Open": (Theme.color["yellow"], Theme.color["black"]),
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
        cursor_color=Theme.color["red"],
        ignore_dups_history=True,
        prompt=" ",
        visual_bell_color=Theme.color["red"],
    ),
    widget.Clipboard(
        blacklist=["1password", "1Password"],
        fmt=" {}",
        foreground=Theme.color["bright_magenta"],
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
        foreground=Theme.color["green"],
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
        foreground=Theme.color["cyan"],
        format="{icon} {temp:.0f}{temp_units}",
        latitude=30.2,
        longitude=-97.7,
        units="imperial",
    ),
    sep,
    widget.Clock(
        foreground=Theme.color["yellow"],
        format=" %a %B %d",
    ),
    sep,
    widget.Clock(
        foreground=Theme.color["magenta"],
        format=" %I:%M %p",
    ),
    sep,
    widget.Wallpaper(
        directory=HOME + "/Pictures/Wallpapers",
        fontsize=16,
        foreground=Theme.color["white"],
        label="",
        random=True,
    ),
    widget.Spacer(
        length=2,
    ),
], **Theme.bar)
