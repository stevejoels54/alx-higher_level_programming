#!/usr/bin/python3
import hidden_4


def get_names():
    names = dir(hidden_4)
    return sorted(name for name in names if not name.startswith('__'))


if __name__ == "__main__":
    names = get_names()
    for name in names:
        print(name)
