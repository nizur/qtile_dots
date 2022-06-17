class Theme(object):
    colors = {
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
        "background": colors["black"],
        "foreground": colors["white"],
        "size": 32,
    }

    layout = {
        "Base": {
            "border_focus": colors["bright_magenta"],
            "border_normal": colors["black"],
            "border_width": 3,
        },
        "MonadTall": {
            "border_focus_stack": colors["bright_magenta"],
            "border_normal_stack": colors["black"],
        },
        "Columns": {
            "border_focus_stack": colors["bright_blue"],
            "border_normal_stack": colors["black"],
        }
    }

    widget = {
        "background": bar["background"],
        "font": "iM WritingQuattroS Nerd Font",
        "fontsize": 13,
        "foreground": bar["foreground"],
        "padding": 10,
    }
