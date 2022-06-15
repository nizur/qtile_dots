from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from commands import Commands
from functions import to_urgent

ALT = "mod1"
MOD = "mod4"
CTL = "control"
SHIFT = "shift"

# Switch group & switch to group keys in groups.py

keys = [
    KeyChord([MOD], "o", [
        Key([], "d", lazy.spawn(Commands.discord), desc="Run Discord"),
        Key([], "f", lazy.spawn(Commands.browser), desc="Run browser"),
        Key([], "v", lazy.spawn(Commands.code), desc="Run Visual Studio Code"),
    ], mode="Open"),

    # Resize windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    KeyChord([MOD], "g", [
        Key([], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([], "g", lazy.layout.grow(), desc="Grow window"),
        Key([], "s", lazy.layout.shrink(), desc="Shrink window"),
        Key([], "m", lazy.layout.maximize(), desc="Maximize window"),
        Key([], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    ], mode="Grow"),

    KeyChord([MOD, CTL], "g", [
        Key([], 'l', lazy.spawn('gnome-screensaver-command -l'), desc="Suspend"),
        Key([], 'q', lazy.spawn(
            'gnome-session-quit --logout --no-prompt'), desc="Logout of Gnome"),
        Key([SHIFT], 'q', lazy.spawn(
            'gnome-session-quit --power-off'), desc="Shutdown"),
    ], mode="Gnome"),

    # Custom
    Key([MOD], "d", lazy.spawn(Commands.menu), desc="Run launcher"),
    Key([MOD], "c", lazy.spawn(Commands.calc), desc="Run calculator"),
    Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD], "p", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([MOD], "Return", lazy.spawn(Commands.terminal), desc="Launch terminal"),
    Key([SHIFT], "F12", lazy.function(to_urgent), desc="Switch to urgent group"),
    #Key([MOD], "Escape", lazy.spawn(Commands.powermenu), desc="Run powermenu"),
    Key([], "Print", lazy.spawn(Commands.screenshot), desc="Take screenshot"),

    # Switch between windows
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),

    Key([MOD, SHIFT], "space", lazy.layout.flip(), desc="Flip the layout"),
    Key([MOD], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD, SHIFT], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([MOD, SHIFT], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([MOD, SHIFT], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([MOD, SHIFT], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MOD, SHIFT], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Restart/shutdown
    Key([MOD, CTL], "r", lazy.restart(), desc="Restart Qtile"),
    Key([MOD, CTL], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]
