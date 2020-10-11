from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation

from main import MainWindow


class UIFunctions(MainWindow):

    def toggle_menu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            max_extend = maxWidth
            standard = 110

            # SET MAX WIDTH
            if width == 110:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
