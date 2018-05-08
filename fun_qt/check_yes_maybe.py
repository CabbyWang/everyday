# coding:utf-8

import sys
from PyQt4.QtGui import *
from PyQt4.Qt import *
import os
from enum import Enum, unique


@unique
class CheckState(Enum):
    # name = value
    Yes = 1
    Maybe = 2
    No = 0


class Check_Y_M_N(QDialog):
    """
    Usage:
        check = Check_Y_M_N('test')
        check.checkState()    # return 0/1/2   no/maybe/yes
        check.setCheckState('yes')    # arguments: 'yes' or 'maybe' or 'no'

        check.setObjectName('object_name')
        check.objectName()
        # object_name
    """
    def __init__(self, text, parent=None):
        super(Check_Y_M_N, self).__init__(parent)
        self.text = text
        self.object_name = None
        self.set_ui()

    def checkState(self):
        for btn in self.buttons:
            if not btn.isChecked():
                continue
            index = self.buttons.index(btn)
            if index == 0:
                return CheckState.Yes
            elif index == 1:
                return CheckState.Maybe
            else:
                return CheckState.No

    def setCheckState(self, state):
        if state == CheckState.Yes or state == CheckState.Yes.value:
            self.buttons[0].setChecked(True)
        elif state == CheckState.Maybe or state == CheckState.Maybe.value:
            self.buttons[1].setChecked(True)
        elif state == CheckState.No or state == CheckState.No.value:
            self.buttons[2].setChecked(True)

    def setObjectName(self, object_name):
        # self.objectName()
        self.object_name = object_name

    def objectName(self):
        return self.object_name

    def set_ui(self):
        main_layout = QHBoxLayout()
        label = QLabel(self.text)
        button_yes = QPushButton()
        button_yes.setObjectName('button_yes')
        button_yes.setToolTip('Yes')
        button_maybe = QPushButton()
        button_maybe.setObjectName('button_maybe')
        button_maybe.setToolTip('Maybe')
        button_no = QPushButton()
        button_no.setObjectName('button_no')
        button_no.setToolTip('No')
        self.buttons = [button_yes, button_maybe, button_no]

        qss_dir = os.path.join(os.path.dirname(__file__))
        main_qss = os.path.join(qss_dir, 'qss', 'main.qss')
        with open(main_qss) as f:
            style_sheet = f.read()
        # self.setStyleSheet(style_sheet)

        # styleSheet
        for button in self.buttons:
            button.setStyleSheet(style_sheet)
            button.setFixedSize(24, 24)
            button.setCheckable(True)
            button.toggled.connect(self.state_change)

        main_layout.addWidget(label)
        main_layout.addWidget(button_yes)
        main_layout.addWidget(button_maybe)
        main_layout.addWidget(button_no)
        self.setLayout(main_layout)

    def state_change(self):
        button = self.sender()
        if not button.isChecked():
            return
        for btn in self.buttons:
            if not btn.isChecked() or btn is button:
                continue
            btn.setChecked(False)


class Example(QDialog):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.set_ui()

    def set_ui(self):
        # layout
        main_layout = QVBoxLayout()
        self.checks = []
        for text in ['aaaaaa', 'bbb', 'cccc']:
            check = Check_Y_M_N(text)
            check.setCheckState(2)
            self.checks.append(check)
            main_layout.addWidget(check)
        self.setLayout(main_layout)

    def getCheckState(self):
        for check in self.checks:
            print(check.checkState())
            print(check.checkState() == CheckState.Maybe)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # qss_dir = os.path.join(os.path.dirname(__file__))
    # main_qss = os.path.join(qss_dir, 'qss', 'main.qss')
    # file = QFile(main_qss)
    # file.open(QFile.ReadOnly)
    # style_sheet = file.readAll()
    # style_sheet = unicode(style_sheet, encoding='utf-8')
    # app.setStyleSheet(style_sheet)
    check = Example()
    check.show()
    app.exec_()
    check.getCheckState()
