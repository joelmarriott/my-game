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

if __name__ == '__main__':
    "Main entry point"
    Game()