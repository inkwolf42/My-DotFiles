import hooks
import jojo_wallpapaers
from libqtile import hook

from libqtile.backend.wayland import InputConfig

from collections.abc import Callable

from libqtile import layout
from libqtile.config import  Group,Match, Output, Screen

from key_binings import loadKeys
from mouse_bindings import loadMouseBindings
from screens_config import loadScreens

groups = [Group(i) for i in "123456789"]

keys = loadKeys(groups)


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=5),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=4,
)

extension_defaults = widget_defaults.copy()

screens = loadScreens()

fake_screens: list[Screen] | None = None

generate_screens: Callable[[list[Output]], list[Screen]] | None = None

mouse = loadMouseBindings()

dgroups_key_binder = None
dgroups_app_rules : list = []  
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  
        Match(wm_class="makebranch"),  
        Match(wm_class="maketag"),  
        Match(wm_class="ssh-askpass"),  
        Match(title="branchdialog"),  
        Match(title="pinentry"),  
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

screen_change_debounce_timeout = 1

auto_minimize = True

# wl_input_rules = {
#     "type:keyboard": InputConfig(kb_layout="fr"),
#     "type:touchpad": InputConfig(tap=True, natural_scroll=True, dwt=True),
# }
#
# wl_xcursor_theme = None
# wl_xcursor_size = 24

idle_timers : list = []  
idle_inhibitors : list = []  


wmname = "LG3D"

