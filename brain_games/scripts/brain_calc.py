#!/usr/bin/env python3


from brain_games.games import calc
from brain_games.game_engine import play_to_win


def main():
    play_to_win(calc)


if __name__ == '__main__':
    main()
