import sys

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import window


def main(argv: list[str]):
    win = window.Window()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


main(sys.argv)
