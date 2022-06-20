from libqtile.config import Key, KeyChord, ScratchPad
from libqtile.lazy import lazy

from classes import Helpers
from groups import groups

ALT = "mod1"
MOD = "mod4"
CTL = "control"
SHIFT = "shift"

keys = [
    KeyChord([MOD], "a", [
        Key([], "Print",
            lazy.spawn("pamixer -m"),
            desc="Mute Track"),
        Key([], "Up",
            lazy.spawn("pamixer -i 4"),
            desc="Volume Up"),
        Key([], "Down",
            lazy.spawn("pamixer -d 4"),
            desc="Volume Down"),
        # Key([], "Left",
        #     lazy.spawn(Commands.audio_track_prev),
        #     desc="Previous Track"),
        # Key([], "Right",
        #     lazy.spawn(Commands.audio_track_next),
        #     desc="Next Track"),
        # Key([], "Return",
        #     lazy.spawn(Commands.audio_play_pause),
        #     desc="Play/Pause Track"),
    ], mode="Audio"),

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
        Key([], "l",
            lazy.spawn("gnome-screensaver-command -l"),
            desc="Suspend"),
        Key([], "q",
            lazy.spawn("gnome-session-quit --logout --no-prompt"),
            desc="Logout of Gnome"),
        Key([SHIFT], "q",
            lazy.spawn("gnome-session-quit --power-off"),
            desc="Shutdown"),
    ], mode="Gnome"),

    # Custom
    Key([MOD], "d",
        lazy.spawn("rofi -show drun"),
        desc="Run launcher"),
    Key([MOD], "c",
        lazy.spawn("rofi -modi calc -show calc -no-show-match -no-bold"),
        desc="Run calculator"),
    Key([MOD], "q",
        lazy.window.kill(),
        desc="Kill focused window"),
    Key([MOD], "p",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([MOD], "Return",
        lazy.spawn("kitty"),
        desc="Launch terminal"),
    Key([CTL], "F1",
        lazy.function(Helpers.go_to_urgent),
        desc="Switch to urgent group"),
    Key([], "F12",
        lazy.group["dropdown"].dropdown_toggle("term"),
        desc="Toggle the terminal scratchpad"),
    Key([], "Print",
        Helpers.create_screenshot(clipboard=False),
        desc="Take a screenshot"),
    Key([ALT], "Print",
        Helpers.create_screenshot(mode="window", clipboard=False),
        desc="Take a screenshot of a specific window"),
    Key([CTL], "Print",
        Helpers.create_screenshot(mode="select", clipboard=False),
        desc="Take a screenshot of a selected area"),

    # Switch between windows
    Key([MOD], "h",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key([MOD], "l",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key([MOD], "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([MOD], "k",
        lazy.layout.up(),
        desc="Move focus up"),

    Key([MOD, SHIFT], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Flip the layout"),
    Key([MOD], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD, SHIFT], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([MOD, SHIFT], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([MOD, SHIFT], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move window down"),
    Key([MOD, SHIFT], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MOD, SHIFT], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([MOD], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    # Restart/shutdown
    Key([MOD, CTL], "r",
        lazy.restart(),
        desc="Restart Qtile"),
    Key([MOD, CTL], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),
]

for i, group in enumerate(groups, start=1):
    if not isinstance(i, ScratchPad):
        group = group.name
        keys.extend([
            # mod1 + letter of group = switch to group
            Key([MOD], str(i), lazy.group[group].toscreen(),
                desc="Switch to group {}".format(group)),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([MOD, SHIFT], str(i), lazy.window.togroup(group, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group)),

            # mod1 + control + letter of group = switch to & move focused window to group
            #Key([MOD, CTL], i.name, Helpers.windows_to_group(i.name)),
        ])
