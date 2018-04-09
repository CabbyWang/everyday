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
            checkbox.pressed.connect(self.pressed)
            checkbox.released.connect(self.released)
            # button = QPushButton('button{}'.format(i), self)
            layout.addWidget(checkbox)
            # layout.addWidget(button)
            button_group.addButton(checkbox)
            # button_group.addButton(button)
        # print(button_group.exclusive())
        layout.setSpacing(20)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def pressed(self):
        self.checkboxes = {}
        checkbox = self.sender()
        print('pressed ', checkbox.checkState())
        self.checkboxes[checkbox] = checkbox.checkState()

    def released(self):
        checkbox = self.sender()
        state = checkbox.checkState()
        print('released', state)
        if state == self.checkboxes.get(checkbox, 0):   # 都为2, 说明状态没有改变
            self.button_group.setExclusive(False)
            checkbox.setChecked(False)
            self.button_group.setExclusive(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = IphoneSwitch()
    win.show()
    sys.exit(app.exec_())
