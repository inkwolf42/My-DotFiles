import os, subprocess
from libqtile import hook, qtile

@hook.subscribe.float_change
def hide_bar_on_fullscreen():
    # Check if any window on the current screen is fullscreen
    current_screen = qtile.current_screen
    # You can iterate over windows or check if the focused window is fullscreen
    focused = qtile.current_window
    if focused and focused.fullscreen:
        qtile.hide_show_bar('all')
    else:
        qtile.hide_show_bar('all')



@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([os.path.expanduser("~/.config/qtile/autostart.sh")])
    subprocess.Popen(["nm-applet"])
    # subprocess.Popen(["picom", "--backend", "glx", "--vsync"])
    # subprocess.Popen(["picom", "--config", os.path.expanduser("~/.config/picom/picom.conf")])
