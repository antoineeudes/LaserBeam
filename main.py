#!/usr/bin/env python
from box import build_interactively
from obstacles import *


if __name__ == '__main__':

    box = build_interactively()
    print(box)
    entry_point = input("Point d'entree? (de la forme >A) : ")



    exit_point, trace = box.simulate_with_trace(entry_point)
    print(box)
    print(box.string_with_trace(trace))

    print("Sorties possibles : {}".format(box.find_exits(entry_point)))
