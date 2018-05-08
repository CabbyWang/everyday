# coding:utf-8

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CheckButtons(QWidget):
    def __init__(self, text, parent=None):
        super(CheckButtons, self).__init__(parent)
        self.text = text
        self.init_ui()

    def init_ui(self):
        # layout
        main_layout = QHBoxLayout()

        label = QLabel(self.text)
        button_yes = QPushButton()
        button_maybe = QPushButton()
        button_no = QPushButton()
        # button_yes.setStyleSheet()
        # for button in [button_yes, button_maybe, button_no]:
        #     button.setStyleSheet()
        main_layout.addWidget(label)
        main_layout.addWidget(button_yes)
        main_layout.addWidget(button_maybe)
        main_layout.addWidget(button_no)
        self.setLayout(main_layout)


class CheckButtons(QWidget):
    def __init__(self, text, parent=None):
        super(CheckButtons, self).__init__(parent)
        # self.resize(40, 10)
        # self.setFixedSize(200, 50)
        # print(self)
        self.text = text
        self.init_ui()

    def init_ui(self):
        # layout
        main_layout = QHBoxLayout()

        label = QLabel(self.text)
        check_yes = QCheckBox('Yes')
        check_maybe = QCheckBox('Maybe')
        # check_no = QCheckBox('No')
        # button_yes.setStyleSheet()
        # for button in [button_yes, button_maybe, button_no]:
        #     button.setStyleSheet()
        main_layout.addWidget(label)
        main_layout.addWidget(check_yes)
        main_layout.addWidget(check_maybe)
        # main_layout.addWidget(check_no)
        self.setLayout(main_layout)


class CheckButton(QWidget):
    def __init__(self, text, parent=None):
        super(CheckButton, self).__init__(parent)
        print('checkbutton .. {}'.format(self))
        self.text = text
        self.state = 0
        self.set_ui()

    def set_ui(self):
        main_layout = QHBoxLayout()
        label = QLabel(self.text)
        button = QPushButton()
        button.clicked.connect(self.button_click)
        main_layout.addWidget(label)
        main_layout.addWidget(button)
        self.setLayout(main_layout)

    def button_click(self):
        self.state = self.state + 1 if self.state != 2 else 0
        print(self.state)


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        print('example ... {}'.format(self))
        self.set_ui()
    
    def set_ui(self):
        # layout
        main_layout = QVBoxLayout()
        for text in ['aaaaaa', 'bbb', 'cccc']:
            checkbutton = CheckButtons(text)
            main_layout.addWidget(checkbutton)
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
