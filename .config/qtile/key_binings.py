from libqtile.config import Group, Key
from libqtile import qtile
from libqtile.lazy import lazy
import os, subprocess


mod = "mod4"


basicKeys = [
        #Move Foucs
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
        
        #Move Window
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

        #Resize Window
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        #Close Window
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

        #Fullscreen
        Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen"),
 
        #Others
        Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key([mod], "r", lazy.restart(), desc="Spawn a command using a prompt widget"),
]

laptopKeys = [
    # Volume (PipeWire/WirePlumber)
    Key([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),
    Key([], "XF86AudioMicMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

    # Media
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),

    # Lock / suspend / screenshot
    Key([mod, "shift"], "x", lazy.spawn("betterlockscreen -l blur"), desc="Lock screen"),
    Key([mod, "shift"], "s", lazy.spawn("systemctl suspend"), desc="Suspend"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Screenshot"),

    #PowerSaving
    Key([mod], "p", lazy.spawn(
        "sh -c 'if [ \"$(powerprofilesctl get)\" = power-saver ]; then "
        "powerprofilesctl set balanced; else powerprofilesctl set power-saver; fi'"
    ), desc="Toggle power saver"),

    # Turn Off
    # Key([mod, "shift"], "e", lazy.spawn('rofi -show menu -modi "menu:rofi-power-menu"')),
    # Key([], "XF86PowerOff", lazy.spawn('rofi -show menu -modi "menu:rofi-power-menu"')),
    # Key([], "XF86PowerOff", subprocess.Popen(["xss-lock", "--transfer-sleep-lock", "--", "betterlockscreen", "-l", "blur"])),
    Key([mod, "shift"], "e", lazy.spawn('/home/inkwolf/.config/rofi/powermenu/type-1/powermenu.sh')),
    Key([], "XF86PowerOff", lazy.spawn('/home/inkwolf/.config/rofi/powermenu/type-1/powermenu.sh')),
]

executKeys = [
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "o", lazy.spawn("firefox-aurora"), desc="Launch FireFox Browser"),
    Key([mod], "a", lazy.spawn("rofi -show drun"), desc="Launch app luncher"),
    Key([mod], "n", lazy.spawn("networkmanager_dmenu"), desc="Network manager Rofi"),
    Key([mod], "y", lazy.spawn("kitty -e yazi"), desc="File Manger"),
    Key([mod], "g", lazy.spawn("flatpak run com.heroicgameslauncher.hgl"), desc="Game Luncher"),
    Key([mod,"shift"], "n", lazy.spawn("kitty -e nmtui"), desc="Network manager TUI"),
]

vtKeys = [
    Key(
        ["control", "mod1"],
        f"f{vt}",
        lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
        desc=f"Switch to VT{vt}",
    ) for vt in range(1,8)
]

groupKey = [
    "ampersand",    
    "eacute",       
    "quotedbl",     
    "apostrophe",   
    "parenleft",    
    "minus",        
    "egrave",       
    "underscore",   
    "ccedilla",     
]

def loadKeys(groups:list[Group]) -> list[Key]:

    keys = []

    keys.extend(basicKeys)
    keys.extend(laptopKeys)
    keys.extend(executKeys)
    keys.extend(vtKeys)

    for i, g in enumerate(groups):
        keys.extend([
            Key([mod], groupKey[i], lazy.group[g.name].toscreen()),
            Key([mod, "shift"], groupKey[i], lazy.window.togroup(g.name, switch_group=True)),
        ])

    return keys



