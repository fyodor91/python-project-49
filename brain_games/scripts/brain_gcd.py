#!/usr/bin/env python3


from brain_games.games import gcd
from brain_games.game_engine import play_to_win


def main():
    play_to_win(gcd)


if __name__ == '__main__':
    main()
