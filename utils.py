import os
import shutil
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def backup_file(src, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    name = os.path.basename(src)
    backup_name = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy(src, os.path.join(backup_dir, backup_name))
