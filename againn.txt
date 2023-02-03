import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel


# Данные об окне с обнулением данных
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        # Создание окна
        self.setGeometry(800, 500, 400, 100)
        self.setWindowTitle("Delete")

        # Ключевой вопрос
        self.n = QLabel(self)
        self.n.setText("ВЫ ТОЧНО ХОТИТЕ УДАЛИТЬ ДАННЫЕ?")
        self.n.move(70, 10)

        # Кнопка отвечающая за удаление данных
        self.btn1 = QPushButton("Удалить", self)
        self.btn1.clicked.connect(self.delete)
        self.btn1.move(200, 50)

        # Кнопка отвечающая за отмену выбора
        self.btn2 = QPushButton("Отмена", self)
        self.btn2.clicked.connect(self.cancellation)
        self.btn2.move(80, 50)

    def delete(self):  # Последствия нажатия на кнопку удалить
        # Обнуление банкротства
        bankruptcy_file = open("bankruptcy.txt", "w")
        bankruptcy_file.write("0")
        bankruptcy_file.close()

        # Обнуление данных о выборе фона из возможных
        background_file = open("background(fon).txt", "w")
        background_file.write("0\n")
        background_file.write("start square.png\n")
        background_file.write("long start.png\n")
        background_file.write("light longe start.png")
        background_file.close()

        # Обнуление данных о топливе
        fuel_file = open("fuel(toplivo).txt", "w")
        fuel_file.write("1000000")
        fuel_file.close()

        # Обновление данных о деньгах
        money_file = open("money.txt", "w")
        money_file.write("1000000")
        money_file.close()

        # Обновление данных об имени пользователя
        name_file = open("name.txt", "w")
        name_file.write("Имя Фамилия")
        name_file.close()

        # Обнуление покупок
        purchases_file = open("purchases(pokupki).txt", "w")
        purchases_file.write("1\n")
        purchases_file.write("pixil-frame- 0.png\n")
        purchases_file.write("1\n")
        purchases_file.write("start square.png")
        purchases_file.close()

        # Обнуление данных о выборе ракеты из возможных
        rocket_file = open("rocket.txt", "w")
        rocket_file.write("0\n")
        rocket_file.write("pixil-frame- 0.png\n")
        rocket_file.write("pixil-frame-0 (1).png\n")
        rocket_file.write("pixil-frame-0 (2).png\n")
        rocket_file.write("pixil-frame-0 (3).png\n")
        rocket_file.write("pixil-frame-0 (4).png\n")
        rocket_file.write("pixil-frame-0 (5).png")
        rocket_file.close()

        # Обнуление количества удачных полётов
        successfulflights_file = open("successful flights.txt", "w")
        successfulflights_file.write("0")
        successfulflights_file.close()

        # Обнуление количества кредитов
        successfulflights_file = open("issued loan.txt", "w")
        successfulflights_file.write("0")
        successfulflights_file.close()

        # Невозможность сразу запустить игру
        play_file = open("play.txt", "w")
        play_file.write("0")
        play_file.close()

        # Обнуление выбраного окна, закрытие окна
        class_file = open("Class.txt", "w")
        class_file.write("Menu")
        class_file.close()
        quit()

    def cancellation(self):  # Последствия после нажатия наъ кнопку отмена, закрытие окна
        quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()
