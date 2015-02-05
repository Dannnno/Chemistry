# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"


import argparse


parser = argparse.ArgumentParser(description="Runs the Chemistry simulator")
parser.add_argument('-c', '--clean', dest='clean',
                    default=False, action='store_true',
                    help='Signals that the directory should get cleaned up')
parser.add_argument('-g', '--gui', dest='gui', default=False,
                    action='store_true', help='Runs the GUI')
args = parser.parse_args()

if args.clean:
    from scripts.make_clean import make_clean
    from scripts.strip_whitespace import strip_whitespace

    make_clean()
    strip_whitespace()

if args.gui:
    import sys
    sys.argv = sys.argv[:1]   # kivy messes up if I don't do this
    from Chemistry import chemgui
    chemgui.main()
else:   # Whatever I'm trying at the moment
    pass
