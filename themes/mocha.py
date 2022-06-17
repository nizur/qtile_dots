from .palettes.mocha import Palette


class Theme(object):
    colors = {
        "base": Palette.grays["base"],

        "black": Palette.grays["crust"],
        "red": Palette.colors["red"],
        "green": Palette.colors["green"],
        "yellow": Palette.colors["yellow"],
        "blue": Palette.colors["blue"],
        "magenta": Palette.colors["peach"],
        "cyan": Palette.colors["sapphire"],
        "white": Palette.grays["subtext1"],

        "bright_black": Palette.grays["surface0"],
        "bright_red": Palette.colors["maroon"],
        "bright_green": Palette.colors["teal"],
        "bright_yellow": Palette.colors["rosewater"],
        "bright_blue": Palette.colors["sky"],
        "bright_magenta": Palette.colors["flamingo"],
        "bright_cyan": Palette.colors["lavender"],
        "bright_white": Palette.grays["text"],
    }

    bar = {
        "background": colors["black"],
        "foreground": colors["white"],
        "size": 32,
    }

    layout = {
        "Base": {
            "border_focus": colors["blue"],
            "border_normal": colors["black"],
            "border_width": 3,
        },
        "MonadTall": {
            "border_focus_stack": colors["blue"],
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
