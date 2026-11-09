
import os
import libqtile.resources

from libqtile import bar, widget
from libqtile.config import Screen


logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
wallpaper = "/home/inkwolf/.config/wallpapers/explorer_orange_sunset.jpg"

def loadScreens()->list[Screen]:
    screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Spacer(length=200),
                    widget.GroupBox(
                        center_aligned=True,
                        font="JetBrainsMono Nerd Font",
                        padding_x=7.25,
                        margin=1,
                        background='101520',
                        border='102030',
                        borderwidth=2
                    ),
                    widget.Prompt(),
                    widget.WindowName(),
                    widget.Chord(
                        chords_colors={
                            "launch": ("#ff0000", "#ffffff"),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                    widget.Backlight(backlight_name="intel_backlight", fmt="☀ {}"),
                    widget.PulseVolume(fmt="🔊 {}"),
                    widget.Battery(
                        format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                        charge_char="⚡", discharge_char="🔋", full_char="🔌",
                        low_percentage=0.15, low_foreground="#ff5555",
                        update_interval=30,
                    ),
                    widget.Systray(),
                    widget.Clock(format="%a %d %b %H:%M"),
                ],
                40,
            ),
            background="#121212",
            wallpaper=wallpaper,
            wallpaper_mode="center",
            # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
            # By default we handle these events delayed to already improve performance, however your system might still be struggling
            # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
            # x11_drag_polling_rate = 60,
        ),
    ]

    return screens