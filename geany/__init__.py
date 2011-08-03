"""
Package file that exposes some of Geany's guts as its own attibutes.  Any
objects where it only makes sense to have one instance of are initialed here
and set as attributes.

You can sort of think of this file as the GeanyData struct from the C API,
though no real attempt is made to mimic that structure here.
"""

import app
import console
import dialogs
import document
import editor
import editorprefs
import encodings
import fileprefs
import filetypes
import highlighting
import indentprefs
import loader
import mainwidgets
import manager
import plugin
import project
import scintilla

from app import App
from editorprefs import EditorPrefs
from fileprefs import FilePrefs
from mainwidgets import MainWidgets
from plugin import Plugin


__all__ = [ "Plugin",
            "main_widgets",
            "editor_prefs",
            "app",
            "file_prefs" ]

# Geany's application data fields
app = App()

# Import GTK+ widgets that are part of Geany's UI
main_widgets = MainWidgets()

# Settings that will by used by Editors
editor_prefs = EditorPrefs()

# Settings relating to how files are handled
file_prefs = FilePrefs()
