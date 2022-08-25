from functools import partial

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Headerbar(Gtk.HeaderBar):
    def __init__(self, title: str, win) -> None:
        self.win = win
        super().__init__()
        self.set_show_close_button(True)
        self.props.title = title
        self.search_entry = Gtk.SearchEntry()
        self.search_btn = Gtk.Button("Search")
        self.pack_start(self.search_entry)
        self.pack_start(self.search_btn)

        self.download_btn = Gtk.Button("Download")
        self.download_btn.get_style_context().add_class("suggested-action")
        self.info_btn = Gtk.Button("View Info")
        self.pack_end(self.download_btn)
        self.pack_end(self.info_btn)

        self.search_btn.connect(
            "clicked", partial(win.torrent_list.query, self.search_entry)
        )
        self.download_btn.connect("clicked", win.torrent_list.download)
        self.info_btn.connect("clicked", win.torrent_list.info)
