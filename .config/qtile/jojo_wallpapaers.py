import os
import subprocess
import shutil
from libqtile import hook, qtile

WALL_DIR = os.path.expanduser("~/.config/qtile/wallpapers/BMP/")
WALL_DIR_RAM = "/dev/shm/wallpapers/"
EXT = ".bmp"  # change if your files use another extension


def load_wallpapers():
    os.makedirs(WALL_DIR_RAM, exist_ok=True)

    for name in sorted(os.listdir(WALL_DIR)):
        src = os.path.join(WALL_DIR, name)
        dst = os.path.join(WALL_DIR_RAM, name)

        if not os.path.isfile(src):
            continue

        # Skip files already in RAM and unchanged (same size and mtime)
        if os.path.exists(dst):
            s, d = os.stat(src), os.stat(dst)
            if s.st_size == d.st_size and int(s.st_mtime) == int(d.st_mtime):
                continue

        shutil.copy2(src, dst)

_last = None

def set_wallpaper(group_name):
    global _last
    path = os.path.join(WALL_DIR_RAM, f"{group_name}{EXT}")
    if not os.path.exists(path):
        path = os.path.join(WALL_DIR_RAM, f"default{EXT}")
    if not os.path.exists(path):
        return
    if _last and _last.poll() is None:   # previous one still running
        _last.terminate()
    if _last:
        _last.wait()                     # reap it, no zombies
    _last = subprocess.Popen(["hsetroot", "-cover", path])



@hook.subscribe.setgroup
def on_group_change():
    set_wallpaper(qtile.current_group.name)


import threading

@hook.subscribe.startup_complete
def on_start():
    def work():
        load_wallpapers()
        set_wallpaper(qtile.current_group.name)
    threading.Thread(target=work, daemon=True).start()
