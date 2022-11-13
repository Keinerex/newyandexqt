import sqlite3
import uuid

from PyQt5.QtWidgets import QFrame

from src.components.Annotation.annotation_style import Ui_Form


class Annotation(QFrame, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)