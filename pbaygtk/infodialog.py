import webbrowser
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import api


class InfoDialog(Gtk.Dialog):
    def __init__(self, parent, torrent: api.Torrent) -> None:
        self.torrent = torrent
        torrent.fetch_more_info()
        super().__init__(title=torrent.name, parent=parent)
        self.set_modal(True)
        self.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
        self.hb = Gtk.HeaderBar()
        self.hb_download_btn = Gtk.Button("Download")
        self.hb.pack_end(self.hb_download_btn)
        self.hb_download_btn.get_style_context().add_class("suggested-action")
        self.hb_download_btn.connect("clicked", self.download)
        self.hb.props.title = torrent.name
        self.hb.set_show_close_button(True)
        self.set_titlebar(self.hb)
        self.set_default_size(500, 500)
        self.description_textbuf = Gtk.TextBuffer()
        self.description_textbuf.insert_at_cursor(
            torrent.description, len(torrent.description)
        )
        self.description_win = Gtk.ScrolledWindow()
        self.description_textview = Gtk.TextView()
        self.description_win.add(self.description_textview)
        self.description_textview.set_editable(False)
        self.description_textview.set_monospace(True)
        self.description_textview.set_buffer(self.description_textbuf)
        box = self.get_content_area()
        box.pack_start(self.description_win, True, True, 0)

    def download(self, ignored) -> None:
        webbrowser.open(self.torrent.magnetlink)
