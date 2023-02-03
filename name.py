import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLineEdit


# Данные об окне с изменением имени
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        # Создание окна
        self.setGeometry(800, 500, 400, 100)
        self.setWindowTitle("Change name")
        # Кнопка для сохранения изменения
        self.btn1 = QPushButton("Изменить", self)
        self.btn1.move(315, 36)
        self.btn1.resize(80, 30)
        self.btn1.clicked.connect(self.change)

        # Просмотр сохраненного имени
        name_file = open("name.txt", "r").read()
        # Создание окна для редактирования сохраненного имени
        self.name1 = QLineEdit(self)
        self.name1.move(10, 36)
        self.name1.resize(300, 30)
        self.name1.setText(name_file)

    def change(self):  # Последствия от нажатия на кнопку изменить
        # Пересохранение нового имени, закрытие окна
        name_input = self.name1.text()
        name_file = open("name.txt", "w")
        name_file.write(name_input)
        name_file.close()
        quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()
