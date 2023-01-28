#!/usr/bin/env python

import sys
import os
import subprocess

if len(sys.argv) < 2:
    print("Error: Missing device port")
    exit(1)

SCRIPT_DIR = os.path.dirname(sys.argv[0])
INKPLATE_TODO_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INKPLATE_TODO_SRC_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../src"))
INKPLATE_MICROPYTHON_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../Inkplate-micropython"))

DEVICE = sys.argv[1]

def get_files():
    out = []
    
    for path, _, files in os.walk(INKPLATE_TODO_SRC_DIR):
        for name in files:
            abs_path = os.path.join(path, name)
            device_path = os.path.relpath(abs_path, INKPLATE_TODO_SRC_DIR).replace('\\', '/')
            out.append([ abs_path, device_path ])
    
    return out

def copy_files_to_device(paths):
    for abs_path, device_path in paths:
        command = f"python {INKPLATE_MICROPYTHON_DIR}/pyboard.py --device {DEVICE} -f cp {abs_path} :{device_path}"
        subprocess.run(["powershell", "-Command", command])

if __name__ == "__main__":
    files = get_files()
    copy_files_to_device(files)
