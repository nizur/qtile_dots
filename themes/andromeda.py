class Theme(object):
    colors = {
        "base": "#2b2d3a",

        # Normal
        "black": "#181a1c",
        "red": "#fb617e",
        "green": "#9ed06c",
        "yellow": "#edc763",
        "blue": "#6dcae8",
        "magenta": "#bb97ee",
        "cyan": "#f89860",
        "white": "#e1e3e4",

        # Bright
        "bright_black": "#3f445b",
        "bright_red": "#f65c79",
        "bright_green": "#99cb67",
        "bright_yellow": "#e8c25e",
        "bright_blue": "#68c5e3",
        "bright_magenta": "#b692e9",
        "bright_cyan": "#f3925b",
        "bright_white": "#dcdedf",
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
