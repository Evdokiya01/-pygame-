import sys
from PyQt5.QtWidgets import QPushButton, QLineEdit, QWidget,  QLabel, QApplication
from PyQt5.QtGui import QPixmap


# Данные об окне с вводом формулы
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        # Создание окна
        self.setGeometry(400, 200, 1000, 500)
        self.setWindowTitle('Make up a formula')

        # Создание кнопки
        self.btn = QPushButton("Проверить", self)
        self.btn.move(600, 250)
        self.btn.clicked.connect(self.verify)
        self.btn.resize(150, 50)

        # Вставка физической формулы
        label = QLabel(self)
        pixmap = QPixmap('formula2.jpg')
        label.setPixmap(pixmap)
        label.move(500, 100)

        # Поле для ввода массы
        self.n1 = QLabel(self)
        self.n1.setText("Переменная масса тела (m)")
        self.n1.move(39, 100)
        self.m = QLineEdit(self)
        self.m.move(36, 120)

        # Поле для ввода скорости
        self.n2 = QLabel(self)
        self.n2.setText("Скорость движения тела переменной массы (V)")
        self.n2.move(39, 150)
        self.v = QLineEdit(self)
        self.v.move(36, 170)

        # Поле для ввода Силы
        self.n3 = QLabel(self)
        self.n3.setText("Внешние силы (F)")
        self.n3.move(39, 200)
        self.f = QLineEdit(self)
        self.f.move(36, 220)

        # Поле для ввода относительной скорости отдаляющихся частиц
        self.n4 = QLabel(self)
        self.n4.setText("Относительная скорость отдаляющихся частиц (u1)")
        self.n4.move(39, 250)
        self.u1 = QLineEdit(self)
        self.u1.move(36, 270)

        # Поле для ввода относительной скорости присоединяющихся частиц
        self.n5 = QLabel(self)
        self.n5.setText("Относительная скорость присоединяющихся частиц (u2)")
        self.n5.move(39, 300)
        self.u2 = QLineEdit(self)
        self.u2.move(36, 320)

        # Важные пометки
        self.n = QLabel(self)
        self.n.setText("В данной игре время является константой (t = const, t = 17)")
        self.n.move(39, 400)

        self.nn = QLabel(self)
        self.nn.setText("d = дельта (△), m1 = m2 = m")
        self.nn.move(39, 420)

        self.nn = QLabel(self)
        self.nn.setText("Как формула представленна в игре:")
        self.nn.move(39, 440)

        self.nn = QLabel(self)
        self.nn.setText("(m * V) / 17 = F + (m / 17) * u1 + (m / 17) * u2")
        self.nn.move(39, 460)

        # Надпись о неправильном вводе данных
        self.nnn = QLabel(self)
        self.nnn.setText("Введены неподхдящие данные")
        self.nnn.move(3600, 3600)

    def verify(self):  # Последствия после нажатия на кнопку проверки формулы
        left = int(self.m.text()) * (int(self.v.text()) / 17)  # Вычисление левой части уравнения
        right = int(self.f.text()) + ((int(self.m.text()) / 17) * int(self.u1.text())) +\
            ((int(self.m.text()) / 17) * int(self.u2.text()))  # Вычисление правой части уравнения

        # Проверка на правильность уравнения
        if left == right:
            # Одобрение на запуск игры, закрытие окна
            play_file = open("play.txt", "w")
            play_file.write("1")
            play_file.close()
            quit()
        else:
            # Обьявление о неправильности вводимых данных
            self.nnn.move(500, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()
