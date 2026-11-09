import os
import libqtile.resources

from libqtile import bar 
from libqtile.config import Screen
from qtile_extras import widget 
from qtile_extras.widget.decorations import PowerLineDecoration


logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
wallpaper = "/home/inkwolf/.config/qtile/wallpapers/default.jpg"

# ---------- Theme ----------
BG      = "#0b1730"   # bar background (dark blue)
BG2     = "#90a040"   # bar background (dark blue)
BG3     = "#246014"   # bar background (dark blue)
BG4     = "#a04840"   # bar background (dark blue)
BG_ALT  = "#1b3366"   # active workspace highlight
FG      = "#d6e2ff"   # text
ACCENT  = "#6ea8ff"   # window title / current workspace text
INACT   = "#4a5a80"   # empty workspaces
WARN    = "#ff5555"

FONT = "JetBrainsMono Nerd Font"


round_right = {"decorations": [PowerLineDecoration(path="rounded_right", size=14)]}
round_left  = {"decorations": [PowerLineDecoration(path="rounded_left",  size=14)]}



# Shared options so every widget uses the same font/colors
base = dict(font=FONT, fontsize=14, foreground=FG, background=BG)
baseNoBG = dict(font=FONT, fontsize=14, foreground=FG)


def loadScreens() -> list[Screen]:
    screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Spacer(length=2),
                    widget.GroupBox(
                        font=FONT,
                        fontsize=14,
                        center_aligned=True,
                        padding_x=7,
                        margin=3,
                        margin_y=10,
                        borderwidth=2,
                        highlight_method="block",
                        rounded=True,
                        active=FG,
                        inactive=INACT,
                        this_current_screen_border=BG_ALT,
                        urgent_border=WARN,
                        background=BG,
                    ),
                    widget.Prompt(**base),
                    widget.WindowName(**{**base, "foreground": ACCENT}, max_chars=60),
                    # widget.Chord(
                    #     chords_colors={
                    #         "launch": ("#ff0000", "#ffffff"),
                    #     },
                    #     name_transform=lambda name: name.upper(),
                    #     **base,
                    #     **round_right
                    # ),
                    widget.Spacer(length=bar.STRETCH),
                    widget.Spacer(length=10,background=BG,**round_right),
                    # cpu
                    widget.CPU(format="\U000f0ee0 {load_percent:.0f}%", **baseNoBG, background=BG2 , width=48 ),
                    # memory
                    widget.Memory(format="\U000f035b {MemPercent:.0f}%", **baseNoBG, background=BG2 , width=48),
                    # brightness
                    widget.Backlight(
                        backlight_name="intel_backlight",
                        fmt="\U000f00df {}",
                        **baseNoBG, background=BG2, width=48
                    ),
                    # volume
                    widget.PulseVolume(fmt="\U000f057e {}", **baseNoBG, background=BG2 , **round_right , width=48),

                    widget.GenPollText(
                        func=lambda: {"power-saver": "\U000f032a", "balanced": "\U000f0079", "performance": "\U000f04c5"}.get(
                            __import__("subprocess").run(["powerprofilesctl", "get"], capture_output=True, text=True).stdout.strip(), "?"),
                        update_interval=5,
                        font=FONT, fontsize=14, foreground=FG,background=BG3
                    ),
                    widget.Spacer(length=10,background=BG3),
                    #  battery
                    widget.Battery(
                        format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                        charge_char="\U000f0084",       # charging
                        discharge_char="\U000f0079",    # discharging
                        full_char="\U000f06a5",         # plug
                        empty_char="\U000f0083",        # alert
                        not_charging_char="\U000f0079",
                        low_percentage=0.15,
                        low_foreground=WARN,
                        update_interval=30,
                        width=88 ,
                        font=FONT, fontsize=14, foreground=FG, background=BG3,**round_right
                    ),
                    widget.Spacer(length=2,background=BG3,**round_right),
                    widget.Systray(background=BG4),
                    # clock
                    widget.Clock(format="\U000f0150 %a %d %b %H:%M", **baseNoBG, background=BG4),
                    widget.Spacer(length=18,background=BG4),

                ],
                36,
                background=BG,          # the bar color lives here, not on Screen
                margin=[6, 8, 0, 8],    # floating look; set to 0 for a flush bar
            ),
            wallpaper=wallpaper,
            wallpaper_mode="center",
            # x11_drag_polling_rate = 60,
        ),
    ]

    return screens
