from PyQt5.QtGui import *
from PyQt5.Qt import *
import sys


class IphoneSwitch(QDialog):
    """checkbox Exclusive"""
    def __init__(self, parent=None):
        super(IphoneSwitch, self).__init__(parent)
        self.set_ui()

    def set_ui(self):
        layout = QHBoxLayout()
        button_group = QButtonGroup()
        self.button_group = button_group
        button_group.setExclusive(True)
        # Exclusive
        for i in range(3):
            checkbox = QCheckBox('switch{}'.format(i), self)
            # button = QPushButton('button{}'.format(i), self)
            layout.addWidget(checkbox)
            # layout.addWidget(button)
            button_group.addButton(checkbox)
            # button_group.addButton(button)
        print(button_group.exclusive())
        layout.setSpacing(20)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = IphoneSwitch()
    win.show()
    sys.exit(app.exec_())
