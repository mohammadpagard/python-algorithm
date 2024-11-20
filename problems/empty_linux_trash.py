"""
    for work with this mini personal package:
        1- install tree package: sudo apt install tree
        2- install all the requirements packages: pip install -r requirements.txt
        3- run the file: python3 empry_linux_trash.py
"""


import os
import pathlib
import subprocess as sp
import shutil
import cowsay
import time
from rich import pretty, panel, console, style

pretty.install()

CONSOLE = console.Console()
YELLOW_STYLE = style.Style(color="yellow", bold=True)
YELLOW_BLINK_STYLE = style.Style(color="yellow", blink=True, bold=True)
DANGER_STYLE = style.Style(color="red", bold=True)

ADDRESS = '/home/{}/.local/share/Trash/files'

files_list = lambda address: [f for f in pathlib.Path(address).iterdir() if f.is_file()]
directories_list = lambda address: [d for d in pathlib.Path(address).iterdir() if d.is_dir()]

def list_trash(username: str) -> str:
    address = ADDRESS.format(username)
    ls_address = os.listdir(address)
    files = files_list(address)
    directories = directories_list(address)
    if ls_address != []:
        for directory in directories:
            directory_name = str(directory).split('/')[-1]
            CONSOLE.print('Directory {} tree:'.format(directory_name), style=YELLOW_BLINK_STYLE)
            sp.run(['tree', directory])
            CONSOLE.print("\nDirectory name: {}".format(directory_name), style=YELLOW_STYLE)
        for file in files:
            file_name = str(file).split('/')[-1]
            CONSOLE.print('File name: {}'.format(file_name), style=YELLOW_STYLE)
        return 'Select empty trash processor to empty your trash...'
    else:
        return cowsay.cow('The trash is already empty...')

def empty_trash(username: str) -> str:
    address = ADDRESS.format(username)
    files = files_list(address)
    directories = directories_list(address)
    for file in files:
        os.remove(file)
        filename = str(file).split('/')
        CONSOLE.print('Removed file {}'.format(filename[-1]), style=DANGER_STYLE)
        time.sleep(3)
    for directory in directories:
        shutil.rmtree(directory)
        directory_name = str(directory).split('/')
        CONSOLE.print('Removed directory {}'.format(directory_name[-1]), style=DANGER_STYLE)
        time.sleep(3)
    return CONSOLE.print('Trash is empty', style=YELLOW_BLINK_STYLE)

def restore_trash(username: str, new_address: str) -> str:
    address = ADDRESS.format(username)
    files = files_list(address)
    directories = directories_list(address)
    for file in files:
        file_name = str(file).split('/')[-1]
        sp.run(['mv', file, new_address])
        CONSOLE.print('Restore file {0} to the {1} address'.format(file_name, new_address+file_name), style=YELLOW_STYLE)
    for directory in directories:
        directory_name = str(directory).split('/')[-1]
        sp.run(['mv', directory, new_address])
        CONSOLE.print('Restore directory {0} to the {1} address'.format(directory_name, new_address+directory_name), style=YELLOW_STYLE)
    return cowsay.cow('Files restored...')

process = input('Wich process?\n1- list trash\n2- empty trash\n3- restore trash\n:')
if process == '1' or process == 'list trash':
    print(list_trash('richie'))
elif process == '2' or process == 'empty trash':
    print(empty_trash('richie'))
elif process == '3' or process == 'restore trash':
    print(restore_trash(username='richie', new_address='/home/richie/Desktop/'))
