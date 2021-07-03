import re

from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.output_label.setFont(font)
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_label.setLineWidth(2)
        self.output_label.setMidLineWidth(0)
        self.output_label.setScaledContents(False)
        self.output_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.percent_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.percent_it())
        self.percent_button.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.percent_button.setFont(font)
        self.percent_button.setObjectName("percent_button")
        self.c_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
        self.c_button.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.c_button.setFont(font)
        self.c_button.setObjectName("c_button")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_it())
        self.arrow_button.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.arrow_button.setFont(font)
        self.arrow_button.setObjectName("arrow_button")
        self.divide_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.divide_button.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.divide_button.setFont(font)
        self.divide_button.setObjectName("divide_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nine_button.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.seven_button.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.multiply_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.multiply_button.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.multiply_button.setFont(font)
        self.multiply_button.setObjectName("multiply_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.eight_button.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.six_button.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.four_button.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.minus_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.minus_button.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.five_button.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.three_button.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.one_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.one_button.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.plus_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.plus_button.setGeometry(QtCore.QRect(280, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.plus_button.setFont(font)
        self.plus_button.setObjectName("plus_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.two_button.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.decimal_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        self.decimal_button.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.decimal_button.setFont(font)
        self.decimal_button.setObjectName("decimal_button")
        self.plus_or_minus_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus_it())
        self.plus_or_minus_button.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.plus_or_minus_button.setFont(font)
        self.plus_or_minus_button.setShortcut("")
        self.plus_or_minus_button.setObjectName("plus_or_minus_button")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_it())
        self.equal_button.setGeometry(QtCore.QRect(280, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.zero_button.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.do_not_click_button = QtWidgets.QPushButton(self.centralwidget)
        self.do_not_click_button.setGeometry(QtCore.QRect(10, 560, 341, 101))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.do_not_click_button.setFont(font)
        self.do_not_click_button.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.do_not_click_button.setObjectName("do_not_click_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def percent_it(self):
        try:
            screen = float(self.output_label.text())
            screen = str(screen * 0.01)
            self.output_label.setText(screen)
        except:
            self.output_label.setText("Error")

    # Удалить элемент
    def remove_it(self):
        screen = self.output_label.text()
        if screen[0] == '0':
            pass
        else:
            # Удаляем последний элемент
            screen = screen[:-1]
            self.output_label.setText(screen)

    # Равно
    def math_it(self):
        screen = self.output_label.text()
        # Подсчёт
        try:
            answer = eval(screen)
            self.output_label.setText(f'{round(answer, 2)}')
        except:
            self.output_label.setText('Error')

    def plus_minus_it(self):
        screen = self.output_label.text()
        if len(re.findall(r'\w+', screen)) == 1:
            # print("Самый верх")
            if screen == '0':
                pass
            else:
                if "-" in screen:
                    self.output_label.setText(screen.replace("-", ''))
                else:
                    self.output_label.setText(f'-{screen}')
        else:
            try:
                # получаем попследний элемент строки (вместе со знаком)
                result = re.findall(r'[-+/*]\w+$', screen)[0]
                # получаем индекс начала последнего числа
                index_start = re.search(r'\w+$', screen).start()
                screen = self.change_label(result, screen, index_start)
                self.output_label.setText(screen)
            except IndexError:
                if screen[-1] == ")":
                    # print("под индекс еррор")
                    self.output_label.setText(self.with_dot(screen))
                elif not re.findall(r'[-+/*]\w+$', screen):
                    self.output_label.setText(self.with_dot(screen))
                    # print(self.with_dot(screen))
                    # print("Выполнил")
                else:
                    self.output_label.setText("Error")

    def dot_it(self):
        """Добавляет точку"""
        screen = self.output_label.text()

        if screen[-1] == '.' or screen[-1] == ")" or screen[-1] == "+" or screen[-1] == "-" or screen[-1] == "*" or \
                screen[-1] == "/":
            pass
        else:
            label = re.split(r'[-+/*\s]', screen)
            if "." in label[-1]:
                pass
            else:
                self.output_label.setText(f'{screen}.')

    def add_opetator(self, operator):
        """Проверяет, есть ли в конце какой-либо оператор. Если нет, добавляет"""
        screen = self.output_label.text()

        label = re.split(r'[-+/*.)\s]', screen)
        if not label[-1]:
            pass
        else:
            self.output_label.setText(f'{screen}{operator}')

    def press_it(self, pressed):
        if pressed == "C":
            self.output_label.setText("0")
        elif pressed == "+" or pressed == "-" or pressed == "*" or pressed == "/":
            self.add_opetator(pressed)
        else:
            if self.output_label.text() == "0":
                self.output_label.setText("")
            elif self.output_label.text() == "Error":
                self.output_label.setText("")
            self.output_label.setText(f'{self.output_label.text() + pressed}')

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.c_button.setText(_translate("MainWindow", "C"))
        self.arrow_button.setText(_translate("MainWindow", "<<"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.multiply_button.setText(_translate("MainWindow", "x"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.decimal_button.setText(_translate("MainWindow", "."))
        self.plus_or_minus_button.setText(_translate("MainWindow", "+/-"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.do_not_click_button.setText(_translate("MainWindow", "DO NOT CLICK"))

    @staticmethod
    def change_label(l_result: list, l_screen: str, l_index: int):
        """Повторяющийся функционал, вынес в отдельную функцию. Используется после нахождения
        результата регулярного выражения в функциях with_dot() и plus_minus_it()"""
        if l_result[0] == '-':
            screen = l_screen[: l_index - 1] + "+" + l_screen[l_index:]
        elif l_result[0] == '+':
            screen = l_screen[: l_index - 1] + "-" + l_screen[l_index:]
        elif l_result[0] == '*' or l_result[0] == '/':
            screen = l_screen[: l_index] + f'(-{l_screen[l_index:]})'
        return screen

    def with_dot(self, screen: str) -> str:
        try:
            # получаем индекс начала последнего числа
            index = re.search(r'\w+$', screen)
            screen_temp = screen[:index.start() - 1] + index.group()

            result_with_dot = re.findall(r'[-+/*]\w+$', screen_temp)[0]
            temp_index = re.search(r'\w+$', screen_temp)
            temp_index_start = temp_index.start()

            screen = self.change_label(result_with_dot, screen, temp_index_start)
        except (IndexError, AttributeError):
            try:
                if screen[-1] == ")":
                    result = re.findall(r'[(]-\d+.\d+[)]$', screen)
                    # print(result)
                    index = re.search(rf'{result[0]}', screen)
                    screen = screen[:index.start() - 1] + index.group()[1:]
                else:
                    if '-' in screen:
                        return screen.replace("-", '')
                    else:
                        return f'-{screen}'
            except IndexError:
                result = re.findall(r'[(]-\d+[)]$', screen)
                index = re.search(rf'{result[0]}', screen)
                screen = screen[:index.start() - 1] + index.group()[1:]
        return screen


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
