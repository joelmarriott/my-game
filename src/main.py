#!/usr/bin/env python3
"""Main entry point for the game

Typical usage example:
    Linux:
        chmod 711 main.py
        pwd
        alias my-game=<contents of pwd>/main.py
        my-game

    Windows/All:
        python3 main.py
"""
from engine.game import Game
from logging.handlers import RotatingFileHandler
import logging, os, sys

user_home = os.path.expanduser('~')
game_files = os.path.join(user_home, 'my-game')
log_path = os.path.join(game_files, 'logs')
dirs = [ game_files, log_path ]
for dir in dirs:
    if not os.path.exists(dir):
        os.mkdir(dir)
    #
#
log_name = 'my-game.log'

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            filename=os.path.join(log_path, log_name),
            mode='a',
            encoding="utf-8",
            maxBytes=512000,
            backupCount=4
        ),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("Application started")


if __name__ == '__main__':
    "Main entry point"
    Game()