import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLineEdit, QLabel


# Данные об окне с оплатой кредита
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        # Создание окна
        self.setGeometry(600, 500, 500, 150)
        self.setWindowTitle('Credit')

        # Создание кнопки оплатить
        self.btn = QPushButton("Оплатить", self)
        self.btn.move(250, 70)
        self.btn.clicked.connect(self.oneClick)

        # Подписи, чтобы пользователи могли понять что надо вводить
        self.n1 = QLabel(self)
        self.n1.setText("№")
        self.n1.move(203, 20)
        self.n2 = QLabel(self)
        self.n2.setText("Сумма оплаты кредита")
        self.n2.move(233, 20)

        # Создание окон для ввода данных об оплате кредита
        self.name1 = QLineEdit(self)
        self.name1.move(200, 36)
        self.name1.resize(20, 20)
        self.name2 = QLineEdit(self)
        self.name2.move(230, 36)
        self.name2.resize(200, 20)

        self.nnn = QLabel(self)
        self.nnn.setText("Недостаточно средств")
        self.nnn.move(3600, 3600)

        # Представление о взятых кредитах в окне
        issued_loan = open("issued loan.txt", "r").readlines()
        for i in range(len(issued_loan)):
            # Правильное вынимание данных из файла
            if i == len(issued_loan) - 1:
                k = issued_loan[i]
            else:
                k = issued_loan[i][:-1]
            # Высвечивание данных в окно
            self.name = QLineEdit(self)
            self.name.move(3, 36 + (20 * i))
            self.name.setText(k)
            self.name.setEnabled(False)

    def oneClick(self):  # Последствие от нажатия на кнопку оплатить
        # Получение данных об оформленных кредитах и бюджете
        issued_loan = open("issued loan.txt", "r").readlines()
        money_file = open("money.txt", "r").read()

        if int(money_file) >= int(self.name2.text()):  # Если кредит можно отдать
            # Создаем новые файлы для записи информации о кредиах и деньгах
            issued_loan2 = open("issued loan.txt", "w")
            money_file2 = open("money.txt", "w")
            l = len(issued_loan)  # Количество кредитов
            for i in range(l):  # Проход по кредитам
                a = int(issued_loan[i][0])  # Получение информации о номере кредита
                if int(self.name1.text()) != a:  # Если кредит не тот, что выбрали
                    issued_loan2.write(issued_loan[i])  # то просто записываем его в новый файл
                else:
                    if int(self.name1.text()) == a and l - 1 == i:  # Если кредит последний в списке
                        if int(self.name2.text()) >= int(issued_loan[i][2:]):  # Если  заплатили весь кредит
                            # вычитание денюжек
                            money_file2.write(str(int(money_file) - int(issued_loan[i][2:])))
                        else:
                            # Изменение суммы за кредит
                            credit = issued_loan[i][0] + " " + str(int(issued_loan[i][2:]) - int(self.name2.text()))
                            # вычитание денюжек
                            money_file2.write(str(int(money_file) - int(self.name2.text())))
                            # записываем измененный кредит в файл с кредитами
                            issued_loan2.write(credit)

                    elif int(self.name1.text()) == a and l - 1 > i:  # Если кредит не последний в списке
                        if int(self.name2.text()) >= int(issued_loan[i][2:-1]):  # Если  заплатили весь кредит
                            # вычитание денюжек
                            money_file2.write(str(int(money_file) - int(issued_loan[i][2:-1])))
                        else:
                            # Изменение суммы за кредит
                            credit = issued_loan[i][0] + " " + str(int(issued_loan[i][2:-1]) - int(self.name2.text()))
                            # вычитание денюжек
                            money_file2.write(str(int(money_file) - int(self.name2.text())))
                            # записываем измененный кредит в файл с кредитами
                            issued_loan2.write(credit)

            # закрытие файлов
            issued_loan2.close()
            money_file2.close()
            # просмотр данных о новых кредитах
            issued_loan = open("issued loan.txt", "r").read()
            if issued_loan == "":  # если их не осталось
                # то записываем в файл 0 и закрываем его
                issued_loan2 = open("issued loan.txt", "w")
                issued_loan2.write("0")
                issued_loan2.close()

            # закрываем окно
            quit()
        else:  # если денег не хватает
            # выводим уведомление о нехваки денег
            self.nnn.move(200, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()
