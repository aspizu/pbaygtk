import webbrowser
from datetime import datetime

import datasize
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import api
import headerbar
import infodialog


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


class TorrentList(Gtk.ScrolledWindow):
    def __init__(self, win) -> None:
        self.win = win
        super().__init__()
        self.store = Gtk.ListStore(
            str,  # NAME
            str,  # SIZE
            str,  # SE
            str,  # LE
            str,  # USER
            str,  # ADDED
        )
        self.treeview = Gtk.TreeView(model=self.store)
        self.add(self.treeview)

        for i, column_title in enumerate(["Name", "Size", "SE", "LE", "User", "Added"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            if column_title in ("Size", "SE", "LE"):
                column.set_alignment(1.0)  # 1.0 -> RIGHT
                renderer.set_alignment(1.0, 0.0)
            column.set_sizing(Gtk.TreeViewColumnSizing.AUTOSIZE)
            column.set_resizable(True)
            self.treeview.append_column(column)

        self.set_vexpand(True)
        self.set_hexpand(True)

    def query(self, search_entry, ignored) -> None:
        search_query = search_entry.get_text()
        self.store.clear()
        self.torrents: list[api.Torrent] = api.Torrent.query(search_query)
        for torrent in self.torrents:
            self.store.append(
                [
                    str(torrent.name),
                    f"{datasize.DataSize(torrent.size):.2a}",
                    str(torrent.seeders),
                    str(torrent.leechers),
                    f"{torrent.username} ({torrent.status})",
                    datetime.utcfromtimestamp(torrent.added).strftime(
                        "%d/%m/%Y %I:%M %p"
                    ),
                ]
            )

    def download(self, ignored) -> None:
        try:
            index = self.treeview.get_selection().get_selected_rows()[1][0][0]
            torrent = self.torrents[index]
            torrent.fetch_more_info()
            webbrowser.open(torrent.magnetlink)
            #  FIXME
            #  Copy magnetlink to clipboard and possibly launch a notification
            # clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
            # clipboard.set_text(torrent.magnetlink)
        except IndexError:
            pass

    def info(self, ignored) -> None:
        try:
            index = self.treeview.get_selection().get_selected_rows()[1][0][0]
            torrent = self.torrents[index]
            torrent.fetch_more_info()
            self.info_window = infodialog.InfoDialog(self.win, torrent)
            self.info_window.show_all()
        except IndexError:
            pass
