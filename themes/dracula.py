class Theme(object):
    color = {
        "base": "#44475a",

        # Normal
        "black": "#21222C",
        "red": "#FF5555",
        "green": "#50FA7B",
        "yellow": "#F1FA8C",
        "blue": "#BD93F9",
        "magenta": "#FF79C6",
        "cyan": "#8BE9FD",
        "white": "#F8F8F2",

        # Bright
        "bright_black": "#6272A4",
        "bright_red": "#FF6E6E",
        "bright_green": "#69FF94",
        "bright_yellow": "#FFFFA5",
        "bright_blue": "#D6ACFF",
        "bright_magenta": "#FF92DF",
        "bright_cyan": "#A4FFFF",
        "bright_white": "#FFFFFF",
    }

    bar = {
        "background": color["black"],
        "foreground": color["white"],
        "size": 30,
    }

    layout = {
        "Base": {
            "border_focus": color["bright_magenta"],
            "border_normal": color["black"],
            "border_width": 3,
        },
        "MonadTall": {
            "border_focus_stack": color["bright_magenta"],
            "border_normal_stack": color["black"],
        },
    }

    widget = {
        "background": bar["background"],
        "font": "iM WritingQuattroS Nerd Font",
        "fontsize": 13,
        "foreground": bar["foreground"],
        "padding": 10,
    }
