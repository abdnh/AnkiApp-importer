from aqt import mw
from aqt.qt import *
from aqt.utils import getFile, showInfo

from .ankiapp_importer import AnkiAppImporter


def import_from_ankiapp(filename):
    importer = AnkiAppImporter(filename)
    importer.import_to_anki(mw)
    showInfo("Imported successfully.", mw, title="AnkiApp Importer")


action = QAction(mw)
action.setText("Import From AnkiApp")
mw.form.menuTools.addAction(action)
action.triggered.connect(
    lambda: getFile(mw, "AnkiApp database file to import", cb=import_from_ankiapp)
)
