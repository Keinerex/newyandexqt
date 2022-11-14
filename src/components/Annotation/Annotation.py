from PyQt5.QtWidgets import QFrame

from src.components.Annotation.annotation_style import Ui_Form


# Аннотация к книге
class Annotation(QFrame, Ui_Form):
    # Инициализация
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        # Инициализация стилей
        self.setupUi(self)
        self.retranslateUi(self)
