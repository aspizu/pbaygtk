import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import headerbar
import infodialog
from torrentlist import TorrentList


class Window(Gtk.Window):
    def __init__(self) -> None:
        super().__init__()
        self.main_grid = Gtk.Grid()
        self.add(self.main_grid)
        self.torrent_list = TorrentList(self)
        self.main_grid.attach(self.torrent_list, 0, 0, 1, 1)
        self.headerbar = headerbar.Headerbar("pbaygtk", self)
        self.set_titlebar(self.headerbar)

        self.set_default_size(800, 600)

        # DEBUG = infodialog.InfoDialog(self, api.Torrent.from_id(41918986))
        # DEBUG.show_all()
