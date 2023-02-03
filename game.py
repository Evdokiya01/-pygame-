import pygame
import os
from random import randint

# Создание переменных для реализации игры

I = 0
SPEEDX = 0
GAME = 0
LOSING = 0

WIDTH2 = 900
WIDTH3 = 900
WIDTH4 = 0
WIDTH5 = 1000
WIDTH6 = 0
HEIGHT2 = -300
HEIGHT4 = -400
HEIGHT3 = 360
HEIGHT5 = 530
HEIGHT6 = 630

MONEY1 = (3600, 3600)
MONEY2 = (3600, 3600)
MONEY3 = (3600, 3600)
MONEY4 = (3600, 3600)
MONEY5 = (3600, 3600)
MONEY6 = (3600, 3600)
MONEY7 = (3600, 3600)


# Данные об основных окнах
class Menu:  # Окно Меню
    def __init__(self):
        pass

    def render(self, screen):  # Создание интерфейса окна "Меню"

        # Надпись МЕНЮ
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 100)
        text = font.render("МЕНЮ", 1, (100, 255, 100))
        screen.blit(text, (380, 100))

        # Создание кнопки ИГРАТЬ
        font = pygame.font.Font(None, 40)
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (30, 300, 200, 80), 0)
        text = font.render("ИГРАТЬ", 1, (100, 255, 100))
        screen.blit(text, (75, 325))

        # Создание кнопки НАСТРОЙКИ
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (265, 300, 200, 80), 0)
        text = font.render("НАСТРОЙКИ", 1, (100, 255, 100))
        screen.blit(text, (277, 325))

        # Создание кнопки МАГАЗИН
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (495, 300, 200, 80), 0)
        text = font.render("МАГАЗИН", 1, (100, 255, 100))
        screen.blit(text, (525, 325))

        # Создание кнопки БАНК
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (725, 300, 200, 80), 0)
        text = font.render("БАНК", 1, (100, 255, 100))
        screen.blit(text, (784, 325))

        # Добавление значков денег и топлива
        screen.blit(pygame.transform.scale(pygame.image.load("toplivo.png"), (70, 60)), (620, -13))
        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), (810, 5))

        # Добавление подпией о количестве топлива и денег
        font = pygame.font.Font(None, 30)  # Изменение размера текста
        money_file = open("money.txt", "r").read()  # Получение информации про деньги
        toplivo_file = open("fuel(toplivo).txt", "r").read()  # Получение информации про топливо
        money = str(money_file) + " руб"
        fuel = str(toplivo_file) + " ml"
        text = font.render(money, 1, (100, 255, 100))  # Вывод на экран сумму денег
        screen.blit(text, (860, 20))
        text = font.render(fuel, 1, (100, 255, 100))  # Вывод на экраз количество топлива
        screen.blit(text, (665, 20))

        # Получение информации про количество удачных полетов и вывод ее на экран
        successful_flights = open("successful flights.txt", "r").read()
        text = font.render(str("УДАЧНЫЕ ПОЛЕТЫ: " + str(successful_flights)), 1, (100, 255, 100))
        screen.blit(text, (300, 20))

        # Получение информации про банкротство
        bankruptcy_file = open("bankruptcy.txt", "r").read()
        if bankruptcy_file == "1":  # Проверка на банкротство
            # Добавление кнопки "Обнулить данные"
            screen.blit(pygame.transform.scale(pygame.image.load("zanovo.png"), (50, 50)), (10, 10))
        else:
            # Получение информации про взятые кредиты
            credit_file = open("issued loan.txt", "r").readlines()
            if int(money_file) < 500 and len(credit_file) == 3 and int(toplivo_file) < 10000:  # Проверка на банкротство
                # Изменение файла с банкротством на положительное значение
                bankruptcy_file = open("bankruptcy.txt", "w")
                bankruptcy_file.write("1")
                bankruptcy_file.close()

    def get_cell(self, mouse_pos):  # Проверка куда кликнул пользователь
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]
        if (x >= 30) and (x <= 230) and (y >= 300) and (y <= 380):  # Проверка нажал ли пользоваель кнопку ИГРАТЬ
            # Изменение окна на окно игры
            claas = open("Class.txt", "w")
            claas.write("Game")
            claas.close()
        elif (x >= 265) and (x <= 465) and (y >= 300) and (y <= 380):  # Проверка нажал ли пользоваель кнопку НАСТРОЙКИ
            # Изменение окна на окно настроек
            claas = open("Class.txt", "w")
            claas.write("Settings")
            claas.close()
        elif (x >= 495) and (x <= 695) and (y >= 300) and (y <= 380):  # Проверка нажал ли пользоваель кнопку МАГАЗИН
            # Изменение окна на окно магазина
            claas = open("Class.txt", "w")
            claas.write("Shop")
            claas.close()
        elif (x >= 725) and (x <= 925) and (y >= 300) and (y <= 380):  # Проверка нажал ли пользоваель кнопку БАНК
            # Изменение окна на окно банка
            claas = open("Class.txt", "w")
            claas.write("Bank")
            claas.close()
        elif (x >= 10) and (x <= 60) and (y >= 10) and (y <= 60):  # Проверка нажал ли пользоваель кнопку "Обнулить данные"
            # Открытие окна для обнуления данных
            os.system("again.py")

    def buy_team(self, mouse_pos):
        pass


class Settings:  # Окно Настройки
    def __init__(self):
        pass

    def render(self, screen):  # Создание интерфейса окна "Настройки"
        # Надпись НАСТРОЙКИ
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        text = font.render("НАСТРОЙКИ", 1, (100, 100, 255))
        screen.blit(text, (270, 100))

        # Создание надписи Имя
        font = pygame.font.Font(None, 40)
        text = font.render("ИМЯ", 1, (100, 100, 255))
        screen.blit(text, (75, 325))

        # Создание кнопки Изменить имя
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (785, 320, 200, 40), 0)
        text = font.render("Изменить имя", 1, (100, 100, 255))
        screen.blit(text, (790, 325))

        #  Создание надписи с именем пользователя
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (265, 300, 500, 80), 0)
        name = open("name.txt", "r").read()
        text = font.render(name, 1, (100, 100, 255))
        screen.blit(text, (330, 325))

        # Изменение размера текста
        font = pygame.font.Font(None, 40)
        # Создание подписи Ракета
        text = font.render("РАКЕТА", 1, (100, 100, 255))
        screen.blit(text, (75, 535))

        # Создание подписи Карта
        text = font.render("КАРТА", 1, (100, 100, 255))
        screen.blit(text, (75, 625))

        # Создание кнопки Изменить
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (465, 550, 200, 80), 0)
        text = font.render("ИЗМЕНИТЬ", 1, (100, 100, 255))
        screen.blit(text, (485, 580))

        # Получение информации про выбранные фон и ракету
        purchases = open("purchases(pokupki).txt", "r").readlines()
        n_2 = int(purchases[int(purchases[0]) + 1])
        rocket_file = open("rocket.txt", "r").readlines()
        background_file = open("background(fon).txt", "r").readlines()
        # Получение названия ракеты в правильном виде
        rocket = purchases[int(rocket_file[0]) + 1][:-1]
        # Получение названия фона в правильном виде
        if int(background_file[0]) == n_2 - 1:
            background = purchases[int(background_file[0]) + 1 + int(purchases[0]) + 1]
        else:
            background = purchases[int(background_file[0]) + 1 + int(purchases[0]) + 1][:-1]

        # Красивенький фон для картинок
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (200, 520, 60, 60), 0)
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (200, 595, 60, 60), 0)

        screen.blit(pygame.transform.scale(pygame.image.load(rocket), (25, 50)), (215, 520))  # Вывод на экран ракеты
        screen.blit(pygame.transform.scale(pygame.image.load(background), (40, 50)), (210, 600))  # Вывод на экран фон
        # Вывод на экран кнопку назад
        screen.blit(pygame.transform.scale(pygame.image.load("back.jpg"), (80, 60)), (20, 20))

    # Проверка куда кликнул пользователь
    def get_cell(self, mouse_pos):
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]
        if (x >= 20) and (x <= 100) and (y >= 20) and (y <= 80):  # Проверка нажал ли игрок кнопку МЕНЮ
            # Изменение окна
            claas = open("Class.txt", "w")
            claas.write("Menu")
            claas.close()
        elif (x >= 465) and (x <= 665) and (y >= 550) and (y <= 630):  # Проверка нажал ли игрок кнопку ИЗМЕНИТЬ
            # Изменение окна
            claas = open("Class.txt", "w")
            claas.write("Shop")
            claas.close()
        elif (x >= 785) and (x <= 985) and (y >= 320) and (y <= 360):  # Проверка нажал ли игрок кнопку ИЗМЕНИТЬ ИМЯ
            # Открытие дополнительного окна для изменения имени
            os.system("name.py")

    def buy_team(self, mouse_pos):
        pass


class Shop:  # Окно Магазин
    def __init__(self):
        pass

    def render(self, screen):  # Создание интерфейса окна "Магазин"
        # Надпись МАГАЗИН
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        text = font.render("МАГАЗИН", 1, (100, 100, 255))
        screen.blit(text, (290, 100))

        # Создание надписи ТОПЛИВО
        font = pygame.font.Font(None, 40)
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (50, 200, 200, 80), 0)
        text = font.render("ТОПЛИВО", 1, (100, 100, 255))
        screen.blit(text, (80, 225))

        # Создание надписи РАКЕТА
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (385, 200, 200, 80), 0)
        text = font.render("РАКЕТА", 1, (100, 100, 255))
        screen.blit(text, (430, 225))
        # Получение информации про купленные ракеты и фоны, а так же про все ракеты и все фоны
        purchases = open("purchases(pokupki).txt", "r").readlines()
        n_2 = int(purchases[int(purchases[0]) + 1])
        rocket_file = open("rocket.txt", "r")
        rocket_file = rocket_file.readlines()
        background_file = open("background(fon).txt", "r")
        background_file = background_file.readlines()

        # Получение данныых в правильном виде
        rocket = purchases[int(rocket_file[0]) + 1][:-1]
        if int(background_file[0]) == n_2 - 1:
            background = purchases[int(background_file[0]) + 1 + int(purchases[0]) + 1]
        else:
            background = purchases[int(background_file[0]) + 1 + int(purchases[0]) + 1][:-1]

        # Вывод на экран картинку выбранной ракеты
        screen.blit(pygame.transform.scale(pygame.image.load(rocket), (25, 50)), (545, 213))

        # Создание надписи КАРТА
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (740, 200, 200, 80), 0)
        text = font.render("КАРТА", 1, (100, 100, 255))
        screen.blit(text, (785, 225))
        # Вывод на экран картинку выбранного фона
        screen.blit(pygame.transform.scale(pygame.image.load(background), (40, 50)), (885, 215))

        # Создание надписей для понимания какие товары у игрока имеются
        text = font.render("Есть", 1, (100, 100, 255))
        screen.blit(text, (100, 325))

        text = font.render("Есть", 1, (100, 100, 255))
        screen.blit(text, (450, 325))

        text = font.render("Есть", 1, (100, 100, 255))
        screen.blit(text, (805, 325))

        # Создание надписей для понимания какие товары у игрока не имеются
        text = font.render("Купить", 1, (100, 100, 255))
        screen.blit(text, (110, 525))

        text = font.render("Купить (300 руб)", 1, (100, 100, 255))
        screen.blit(text, (380, 525))

        text = font.render("Купить (600 руб)", 1, (100, 100, 255))
        screen.blit(text, (735, 525))

        # Получение информации про покупки
        purchases = open("purchases(pokupki).txt", "r").readlines()

        # Номер важных элементов в списке покупок
        n = int(purchases[0])
        n_2 = int(purchases[int(purchases[0]) + 1])
        nn_2 = int(purchases[0]) + 1
        # Вывод купленных ракет на экран
        for i in range(n):
            rocket = str(purchases[i + 1][:-1])  # Получение название ракеты
            if i < 3:  # В ряду по 3 ракеты, всего 2 ряда
                pygame.draw.rect(screen,
                                 (255, 255, 255),
                                 (370 + (80 * i), 360, 60, 60), 0)  #
                # Вывод нужной картинки на экран
                screen.blit(pygame.transform.scale(pygame.image.load(rocket), (25, 50)), (387 + (80 * i), 365))
            else:
                pygame.draw.rect(screen,
                                 (255, 255, 255),
                                 (370 + (80 * (i - 3)), 440, 60, 60), 0)  #
                # Вывод нужной картинки на экран
                screen.blit(pygame.transform.scale(pygame.image.load(rocket), (25, 50)), (387 + (80 * (i - 3)), 445))

        # Вывод купленного фона на экран
        for i in range(n_2):
            # Получение названия фона
            if i == n_2 - 1:
                background = purchases[nn_2 + i + 1]
            else:
                background = purchases[nn_2 + i + 1][:-1]
            pygame.draw.rect(screen,
                             (255, 255, 255),
                             (730 + (80 * i), 360, 60, 60), 0)
            # Вывод нужной картинки на экран
            screen.blit(pygame.transform.scale(pygame.image.load(background), (40, 55)), (738 + (80 * i), 363))

        # Получение информации про не купленные товары
        rocket_file = open("rocket.txt", "r").readlines()
        background_file = open("background(fon).txt", "r").readlines()
        purchases = open("purchases(pokupki).txt", "r").read()
        # проход по ракетам
        for i in range(6):
            # Получение названия ракеты
            if i == 5:
                rocket = rocket_file[i + 1]
            else:
                rocket = rocket_file[i + 1][:-1]
            # Проверка не купили ли эту ракету
            if rocket not in purchases:
                if i < 3:  # В ряду по 3 ракеты, всего 2 ряда
                    pygame.draw.rect(screen,
                                     (255, 255, 255),
                                     (370 + (80 * i), 560, 60, 60), 0)  #
                    # Вывод нужной картинки на экран
                    screen.blit(pygame.transform.scale(pygame.image.load(rocket), (25, 50)), (387 + (80 * i), 565))
                else:
                    pygame.draw.rect(screen,
                                     (255, 255, 255),
                                     (370 + (80 * (i - 3)), 640, 60, 60), 0)  #
                    # Вывод нужной картинки на экран
                    screen.blit(pygame.transform.scale(pygame.image.load(rocket), (25, 50)), (387 + (80 * (i - 3)), 645))

        # Проход по картам
        for i in range(3):
            # Получение названия карты
            if i == 2:
                background = background_file[i + 1]
            else:
                background = background_file[i + 1][:-1]
            # проверка не куплен ли фон
            if background not in purchases:
                pygame.draw.rect(screen,
                                 (255, 255, 255),
                                 (730 + (80 * i), 560, 60, 60), 0)  #
                # вывод нужной картинки на экран
                screen.blit(pygame.transform.scale(pygame.image.load(background), (40, 55)), (738 + (80 * i), 560))

        # Вывод на экран кнопку назад
        screen.blit(pygame.transform.scale(pygame.image.load("back.jpg"), (80, 60)), (20, 20))

        # Получение информации про количество денег и топлива
        money_file = open("money.txt", "r").read()
        toplivo_file = open("fuel(toplivo).txt", "r").read()
        money = str(money_file) + " руб"
        fuel = str(toplivo_file) + " ml"
        # Вывод значка топлина на экран
        screen.blit(pygame.transform.scale(pygame.image.load("toplivo.png"), (70, 60)), (60, 380))
        # Вывод информации про топливо на экран
        text = font.render(fuel, 1, (100, 100, 255))
        screen.blit(text, (100, 405))

        # Вывод Цены на определенное количество топлива
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (19, 569, 320, 30), 0)
        text = font.render("100 ml - 500 руб", 1, (100, 100, 255))
        screen.blit(text, (20, 570))
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (19, 619, 320, 30), 0)
        text = font.render("1000 ml - 4000 руб", 1, (100, 100, 255))
        screen.blit(text, (20, 620))
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (19, 669, 320, 30), 0)
        text = font.render("100000 ml - 300000 руб", 1, (100, 100, 255))
        screen.blit(text, (20, 670))

        font = pygame.font.Font(None, 30)  # Изменение размера текста
        # Вывод на экран информацию про деньги и картинку монетки
        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), (810, 5))
        text = font.render(money, 1, (100, 255, 100))
        screen.blit(text, (860, 20))

        # Важная информация которую нельзя игнорировать
        text = font.render("Чтобы купить/выбрать товар: кликнуть мышкой", 1, (100, 255, 100))
        screen.blit(text, (515, 65))
        text = font.render("и одновременно нажать на пробел", 1, (100, 255, 100))
        screen.blit(text, (645, 85))

    # Проверка куда кликнул пользователь
    def get_cell(self, mouse_pos):
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]
        if (x >= 20) and (x <= 100) and (y >= 20) and (y <= 80):  # Проверка нажал ли игрок кнопку МЕНЮ
            # Изменение окна
            claas = open("Class.txt", "w")
            claas.write("Menu")
            claas.close()

    def buy_team(self, mouse_pos):
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]

        if (x >= 370) and (x <= 590) and (y >= 560) and (y <= 700):  # ЭТО РАКЕТЫ купить
            if (x >= 450) and (x <= 510) and (y >= 560) and (y <= 620):  # Проверка купили ли 2 ракету
                # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                purchases = open("purchases(pokupki).txt", "r").readlines()

                name = "pixil-frame-0 (1).png"
                if name not in purchases and int(money_file) >= 300:  # Проверка на то, что ракету можно купить
                    # Изменение имени ракеты в нужный вид, уменьшение бюджета за счет покупки ракеты
                    name = name + "\n"
                    money_file2.write(str(int(money_file) - 300))

                    money_file2.close()

                    # Получение информации про покупки и создание пустого файла с покупками
                    purchases = open("purchases(pokupki).txt", "r").readlines()
                    purchases2 = open("purchases(pokupki).txt", "w")

                    # Заполнение нового файла старым + именем выбранной ракеты
                    n = int(purchases[0])
                    n_2 = int(purchases[int(purchases[0]) + 1])
                    nn_2 = int(purchases[0]) + 1
                    purchases2.write(str(n + 1) + "\n")
                    for i in range(n):  # Проход по ракетам
                        purchases2.write((purchases[i + 1]))
                    purchases2.write(name)
                    purchases2.write(str(n_2) + "\n")
                    for i in range(n_2):  # Проход по фону
                        purchases2.write(purchases[nn_2 + i + 1])
                    purchases2.close()
            elif (x >= 530) and (x <= 590) and (y >= 560) and (y <= 620):  # Проверка купили ли 3 ракету
                # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                purchases = open("purchases(pokupki).txt", "r").readlines()

                name = "pixil-frame-0 (2).png"
                if name not in purchases and int(money_file) >= 300:  # Проверка на то, что ракету можно купить
                    # Изменение имени ракеты в нужный вид, уменьшение бюджета за счет покупки ракеты
                    name = name + "\n"
                    money_file2.write(str(int(money_file) - 300))

                    money_file2.close()

                    # Получение информации про покупки и создание пустого файла с покупками
                    purchases = open("purchases(pokupki).txt", "r").readlines()
                    purchases2 = open("purchases(pokupki).txt", "w")

                    # Заполнение нового файла старым + именем выбранной ракеты
                    n = int(purchases[0])
                    n_2 = int(purchases[int(purchases[0]) + 1])
                    nn_2 = int(purchases[0]) + 1
                    purchases2.write(str(n + 1) + "\n")
                    for i in range(n):  # Проход по ракетам
                        purchases2.write((purchases[i + 1]))
                    purchases2.write(name)
                    purchases2.write(str(n_2) + "\n")
                    for i in range(n_2):  # Проход по фону
                        purchases2.write(purchases[nn_2 + i + 1])
                    purchases2.close()
            elif (x >= 370) and (x <= 430) and (y >= 640) and (y <= 700):  # Проверка купили ли 4 ракету
                # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                purchases = open("purchases(pokupki).txt", "r").readlines()

                name = "pixil-frame-0 (3).png"
                if name not in purchases and int(money_file) >= 300:  # Проверка на то, что ракету можно купить
                    # Изменение имени ракеты в нужный вид, уменьшение бюджета за счет покупки ракеты
                    name = name + "\n"
                    money_file2.write(str(int(money_file) - 300))

                    money_file2.close()

                    # Получение информации про покупки и создание пустого файла с покупками
                    purchases = open("purchases(pokupki).txt", "r").readlines()
                    purchases2 = open("purchases(pokupki).txt", "w")

                    # Заполнение нового файла старым + именем выбранной ракеты
                    n = int(purchases[0])
                    n_2 = int(purchases[int(purchases[0]) + 1])
                    nn_2 = int(purchases[0]) + 1
                    purchases2.write(str(n + 1) + "\n")
                    for i in range(n):  # Проход по ракетам
                        purchases2.write((purchases[i + 1]))
                    purchases2.write(name)
                    purchases2.write(str(n_2) + "\n")
                    for i in range(n_2):  # Проход по фону
                        purchases2.write(purchases[nn_2 + i + 1])
                    purchases2.close()
            elif (x >= 450) and (x <= 510) and (y >= 640) and (y <= 700):  # Проверка купили ли 5 ракету
                # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                purchases = open("purchases(pokupki).txt", "r").readlines()

                name = "pixil-frame-0 (4).png"
                if name not in purchases and int(money_file) >= 300:  # Проверка на то, что ракету можно купить
                    # Изменение имени ракеты в нужный вид, уменьшение бюджета за счет покупки ракеты
                    name = name + "\n"
                    money_file2.write(str(int(money_file) - 300))

                    money_file2.close()

                    # Получение информации про покупки и создание пустого файла с покупками
                    purchases = open("purchases(pokupki).txt", "r").readlines()
                    purchases2 = open("purchases(pokupki).txt", "w")

                    # Заполнение нового файла старым + именем выбранной ракеты
                    n = int(purchases[0])
                    n_2 = int(purchases[int(purchases[0]) + 1])
                    nn_2 = int(purchases[0]) + 1
                    purchases2.write(str(n + 1) + "\n")
                    for i in range(n):  # Проход по ракетам
                        purchases2.write((purchases[i + 1]))
                    purchases2.write(name)
                    purchases2.write(str(n_2) + "\n")
                    for i in range(n_2):  # Проход по фону
                        purchases2.write(purchases[nn_2 + i + 1])
                    purchases2.close()
            elif (x >= 530) and (x <= 590) and (y >= 640) and (y <= 700):  # Проверка купили ли 6 ракету
                # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                purchases = open("purchases(pokupki).txt", "r").readlines()

                name = "pixil-frame-0 (5).png"
                if name not in purchases and int(money_file) >= 300:  # Проверка на то, что ракету можно купить
                    # Изменение имени ракеты в нужный вид, уменьшение бюджета за счет покупки ракеты
                    name = name + "\n"
                    money_file2.write(str(int(money_file) - 300))

                    money_file2.close()

                    # Получение информации про покупки и создание пустого файла с покупками
                    purchases = open("purchases(pokupki).txt", "r").readlines()
                    purchases2 = open("purchases(pokupki).txt", "w")

                    # Заполнение нового файла старым + именем выбранной ракеты
                    n = int(purchases[0])
                    n_2 = int(purchases[int(purchases[0]) + 1])
                    nn_2 = int(purchases[0]) + 1
                    purchases2.write(str(n + 1) + "\n")
                    for i in range(n):  # Проход по ракетам
                        purchases2.write((purchases[i + 1]))
                    purchases2.write(name)
                    purchases2.write(str(n_2) + "\n")
                    for i in range(n_2):  # Проход по фону
                        purchases2.write(purchases[nn_2 + i + 1])
                    purchases2.close()
        elif (x >= 730) and (x <= 1030) and (y >= 560) and (y <= 620):  # ЭТО ФОН купить
            if (x >= 810) and (x <= 870) and (y >= 560) and (y <= 620):  # Проверка купили ли 2 фон
                # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                purchases = open("purchases(pokupki).txt", "r").readlines()

                name = "long start.png"

                if name not in purchases and int(money_file) >= 300:  # Проверка на то, что фон можно купить
                    # Изменение имени фона в нужный вид, уменьшение бюджета за счет покупки фона
                    name = "\n" + name
                    money_file2.write(str(int(money_file) - 300))

                    # Получение информации про покупки и создание пустого файла с покупками
                    purchases = open("purchases(pokupki).txt", "r").readlines()
                    purchases2 = open("purchases(pokupki).txt", "w")

                    # Заполнение нового файла старым + именем выбранного фона
                    n = int(purchases[0])
                    n_2 = int(purchases[int(purchases[0]) + 1])
                    nn_2 = int(purchases[0]) + 1
                    purchases2.write(purchases[0])
                    for i in range(n):  # Проход по ракетам
                        purchases2.write((purchases[i + 1]))
                    purchases2.write(str(n_2 + 1) + "\n")
                    for i in range(n_2):  # Проход по карте
                        purchases2.write(purchases[nn_2 + i + 1])
                    purchases2.write(name)
                    purchases2.close()
            elif (x >= 890) and (x <= 950) and (y >= 560) and (y <= 620):  # Проверка купили ли 3 фон
                # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                purchases = open("purchases(pokupki).txt", "r").readlines()

                name = "light longe start.png"

                if name not in purchases and int(money_file) >= 300:  # Проверка на то, что фон можно купить
                    # Изменение имени фона в нужный вид, уменьшение бюджета за счет покупки фона
                    name = "\n" + name
                    money_file2.write(str(int(money_file) - 300))

                    # Получение информации про покупки и создание пустого файла с покупками
                    purchases = open("purchases(pokupki).txt", "r").readlines()
                    purchases2 = open("purchases(pokupki).txt", "w")

                    # Заполнение нового файла старым + именем выбранного фона
                    n = int(purchases[0])
                    n_2 = int(purchases[int(purchases[0]) + 1])
                    nn_2 = int(purchases[0]) + 1
                    purchases2.write(purchases[0])
                    for i in range(n):  # Проход по ракетам
                        purchases2.write((purchases[i + 1]))
                    purchases2.write(str(n_2 + 1) + "\n")
                    for i in range(n_2):  # Проход по карте
                        purchases2.write(purchases[nn_2 + i + 1])
                    purchases2.write(name)
                    purchases2.close()
        elif (x >= 19) and (x <= 339) and (y >= 569) and (y <= 699):  # ЭТО ТОПЛИВО
            if (x >= 19) and (x <= 339) and (y >= 569) and (y <= 599):  # Проверка купили 1 вариант топлива
                # Получение данных о деньгах
                money_file = open("money.txt", "r").read()
                if int(money_file) >= 500:  # Проверка на то, что топливо можно купить
                    # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                    money_file2 = open("money.txt", "w")
                    toplivo_file = open("fuel(toplivo).txt", "r").read()
                    toplivo_file2 = open("fuel(toplivo).txt", "w")
                    # Уменьшение бюджета за счет покупки топлива
                    money_file2.write(str(int(money_file) - 500))
                    toplivo_file2.write(str(int(toplivo_file) + 100))
            elif (x >= 19) and (x <= 339) and (y >= 619) and (y <= 649):  # Проверка купили 2 вариант топлива
                # Получение данных о деньгах
                money_file = open("money.txt", "r").read()
                if int(money_file) >= 4000:  # Проверка на то, что топливо можно купить
                    # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                    money_file2 = open("money.txt", "w")
                    toplivo_file = open("fuel(toplivo).txt", "r").read()
                    toplivo_file2 = open("fuel(toplivo).txt", "w")
                    # Уменьшение бюджета за счет покупки топлива
                    money_file2.write(str(int(money_file) - 4000))
                    toplivo_file2.write(str(int(toplivo_file) + 1000))
            elif (x >= 19) and (x <= 339) and (y >= 669) and (y <= 699):  # Проверка купили 3 вариант топлива
                # Получение данных о деньгах
                money_file = open("money.txt", "r").read()
                if int(money_file) >= 300000:  # Проверка на то, что топливо можно купить
                    # Получение информации про покупки и деньги, так же создание пустого файла с деньгами
                    money_file2 = open("money.txt", "w")
                    toplivo_file = open("fuel(toplivo).txt", "r").read()
                    toplivo_file2 = open("fuel(toplivo).txt", "w")
                    # Уменьшение бюджета за счет покупки топлива
                    money_file2.write(str(int(money_file) - 300000))
                    toplivo_file2.write(str(int(toplivo_file) + 100000))

        if (x >= 370) and (x <= 590) and (y >= 360) and (y <= 500):  # ЭТО РАКЕТЫ выбрать
            if (x >= 370) and (x <= 430) and (y >= 360) and (y <= 420):  # Проверка. Выбрали ли 1 ракету
                # получение информации про ракеты, создание пустого файла для ракет
                rocket = open("rocket.txt", "r").readlines()
                rocket2 = open("rocket.txt", "w")
                # Изменение номера выбранной ракеты
                rocket2.write(str(0) + "\n")
                for i in range(6): # добавление всех ракет
                    rocket2.write(rocket[i + 1])
                rocket2.close()
            elif (x >= 450) and (x <= 510) and (y >= 360) and (y <= 420):  # Проверка. Выбрали ли 2 ракету
                # получение информации про ракеты, создание пустого файла для ракет
                rocket = open("rocket.txt", "r").readlines()
                rocket2 = open("rocket.txt", "w")
                # Изменение номера выбранной ракеты
                rocket2.write(str(1) + "\n")
                for i in range(6):  # добавление всех ракет
                    rocket2.write(rocket[i + 1])
                rocket2.close()
            elif (x >= 530) and (x <= 590) and (y >= 360) and (y <= 420):  # Проверка. Выбрали ли 3 ракету
                # получение информации про ракеты, создание пустого файла для ракет
                rocket = open("rocket.txt", "r").readlines()
                rocket2 = open("rocket.txt", "w")
                # Изменение номера выбранной ракеты
                rocket2.write(str(2) + "\n")
                for i in range(6):  # добавление всех ракет
                    rocket2.write(rocket[i + 1])
                rocket2.close()
            elif (x >= 370) and (x <= 430) and (y >= 440) and (y <= 500):  # Проверка. Выбрали ли 4 ракету
                # получение информации про ракеты, создание пустого файла для ракет
                rocket = open("rocket.txt", "r").readlines()
                rocket2 = open("rocket.txt", "w")
                # Изменение номера выбранной ракеты
                rocket2.write(str(3) + "\n")
                for i in range(6):  # добавление всех ракет
                    rocket2.write(rocket[i + 1])
                rocket2.close()
            elif (x >= 450) and (x <= 510) and (y >= 440) and (y <= 500):  # Проверка. Выбрали ли 5 ракету
                # получение информации про ракеты, создание пустого файла для ракет
                rocket = open("rocket.txt", "r").readlines()
                rocket2 = open("rocket.txt", "w")
                # Изменение номера выбранной ракеты
                rocket2.write(str(4) + "\n")
                for i in range(6):  # добавление всех ракет
                    rocket2.write(rocket[i + 1])
                rocket2.close()
            elif (x >= 530) and (x <= 590) and (y >= 440) and (y <= 500):  # Проверка. Выбрали ли 6 ракету
                # получение информации про ракеты, создание пустого файла для ракет
                rocket = open("rocket.txt", "r").readlines()
                rocket2 = open("rocket.txt", "w")
                # Изменение номера выбранной ракеты
                rocket2.write(str(5) + "\n")
                for i in range(6):  #
                    rocket2.write(rocket[i + 1])
                rocket2.close()
        elif (x >= 730) and (x <= 950) and (y >= 360) and (y <= 420):  # ЭТО ФОН
            if (x >= 730) and (x <= 790) and (y >= 360) and (y <= 420):  # Проверка. Выбрали ли 1 фон
                # Получение информации про карты, создание пустого файла для карт
                background = open("background(fon).txt", "r").readlines()
                background2 = open("background(fon).txt", "w")
                # Изменение номера выбранного фона
                background2.write(str(0) + "\n")
                for i in range(3):  # добавление всех карт
                    background2.write(background[i + 1])
                background2.close()
            elif (x >= 810) and (x <= 870) and (y >= 360) and (y <= 420):  # Проверка. Выбрали ли 2 фон
                # Получение информации про карты, создание пустого файла для карт
                background = open("background(fon).txt", "r").readlines()
                background2 = open("background(fon).txt", "w")
                # Изменение номера выбранного фона
                background2.write(str(1) + "\n")
                for i in range(3):  # добавление всех карт
                    background2.write(background[i + 1])
                background2.close()
            elif (x >= 890) and (x <= 950) and (y >= 360) and (y <= 420):  # Проверка. Выбрали ли 3 фон
                # Получение информации про карты, создание пустого файла для карт
                background = open("background(fon).txt", "r").readlines()
                background2 = open("background(fon).txt", "w")
                # Изменение номера выбранного фона
                background2.write(str(2) + "\n")
                for i in range(3):  # добавление всех карт
                    background2.write(background[i + 1])
                background2.close()


class Bank:  # Окно Банк
    def __init__(self):
        pass

    def render(self, screen):  # Создание интерфейса окна "Банк"
        # Надпись БАНК
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        text = font.render("БАНК", 1, (100, 100, 255))
        screen.blit(text, (390, 100))

        # Добавление картинок
        screen.blit(pygame.transform.scale(pygame.image.load("back.jpg"), (80, 60)), (20, 20))  # Рисунок Назад
        screen.blit(pygame.transform.scale(pygame.image.load("toplivo.png"), (70, 60)), (620, -13))  # Рисунок Топливо
        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), (810, 5))  # Рисунок Деньги

        # Изменение размера текста
        font = pygame.font.Font(None, 30)
        # Вывод на экран важной информации
        text = font.render("Чтобы оформить кредит: кликнуть мышкой", 1, (100, 255, 100))
        screen.blit(text, (515, 65))
        text = font.render("и одновременно нажать на пробел", 1, (100, 255, 100))
        screen.blit(text, (645, 85))

        # Получение информации про удачные полеты и вывод ее на экран
        successful_flights = open("successful flights.txt", "r").read()
        text = font.render(str("УДАЧНЫЕ ПОЛЕТЫ: " + str(successful_flights)), 1, (100, 255, 100))
        screen.blit(text, (300, 20))

        # Получение информации про деньги и топливо
        money_file = open("money.txt", "r").read()
        toplivo_file = open("fuel(toplivo).txt", "r").read()
        money = str(money_file) + " руб"
        fuel = str(toplivo_file) + " ml"

        # Вывод на экран информауии про деньги и топливо
        text = font.render(money, 1, (100, 255, 100))
        screen.blit(text, (860, 20))
        text = font.render(fuel, 1, (100, 255, 100))
        screen.blit(text, (665, 20))

        # Создание надписи ОФОРМЛЕННЫЙ
        font = pygame.font.Font(None, 40)
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (100, 250, 250, 80), 0)
        text = font.render("ОФОРМЛЕННЫЙ", 1, (100, 100, 255))
        screen.blit(text, (110, 275))

        # Создание надписи ОФОРМИТЬ
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         (650, 250, 250, 80), 0)
        text = font.render("ОФОРМИТЬ", 1, (100, 100, 255))
        screen.blit(text, (695, 275))

        # Получение информации про оформленные кредиты и все кредиты которые существуют
        issued_loan = open("issued loan.txt", "r").readlines()
        credit_file = open("credit.txt", "r").readlines()
        # Изменение размера текста
        font = pygame.font.Font(None, 35)

        if issued_loan[0] != "0":  # Проверка на то, что есть хотя бы один оформленный кредит
            pygame.draw.rect(screen,
                             (255, 255, 255),
                             (130, 340, 200, 50), 0)  #
            # Создание кнопки оплатить
            text = font.render("ОПЛАТИТЬ", 1, (100, 100, 255))
            screen.blit(text, (160, 355))

            for i in range(len(issued_loan)):  # Проход по оформленным кредитам
                # Получение информации о кредите
                if i == len(issued_loan) - 1:
                    k = issued_loan[i]
                else:
                    k = issued_loan[i][:-1]
                # Вывод информации на экран
                pygame.draw.rect(screen,
                                 (255, 255, 255),
                                 (80, 400 + (80 * i), 300, 40), 0)
                text = font.render(k, 1, (100, 100, 255))
                screen.blit(text, (100, 405 + (80 * i)))
        d = 0
        issued_loan = open("issued loan.txt", "r").read()
        for i in range(len(credit_file)):  # Проход по кредитам
            # Получение информации о кредите
            k = credit_file[i]
            k = k.split()
            if k[0] not in issued_loan:  # Проверка на то, не оформлен ли этот кредит
                # Получение точной информации о кредите
                if i == len(issued_loan):
                    k = credit_file[i]
                else:
                    k = credit_file[i][:-1]
                # Вывод информации на экран
                pygame.draw.rect(screen,
                                 (255, 255, 255),
                                 (650, 400 + (80 * i), 300, 40), 0)
                text = font.render(k, 1, (100, 100, 255))
                screen.blit(text, (670, 405 + (80 * i)))
            d += 1

    # Проверка куда кликнул пользователь
    def get_cell(self, mouse_pos):
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]
        if (x >= 20) and (x <= 100) and (y >= 20) and (y <= 80):  # Проверка нажал ли пользоваель кнопку МЕНЮ
            # Изменение окна
            claas = open("Class.txt", "w")
            claas.write("Menu")
            claas.close()
        elif (x >= 130) and (x <= 330) and (y >= 340) and (y <= 390):  # Проверка нажал ли пользоваель кнопку ОПЛАТИТЬ
            # Открытие дополнительного окна для оплаты кредита
            os.system("credit.py")

    def buy_team(self, mouse_pos):  # Оформление кредита
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]
        if (x >= 650) and (x <= 950) and (y >= 400) and (y <= 600):  # Проверка не нажал ли игрок куда-то ни туда
            if (x >= 650) and (x <= 950) and (y >= 400) and (y <= 440):  # Проверка на оформление 1 кредита
                # Получение информации про оформленные кредиты
                issued_loan = open("issued loan.txt", "r").readlines()
                if issued_loan[0] == "0":  # Проверка не пуст ли файл с оформленными кредитами
                    k = 1
                else:
                    k = 0
                # Создание пустого файла с оформленными кредитами
                issued_loan2 = open("issued loan.txt", "w")
                for i in issued_loan[k:]:  # проход по всем оформелнны кредитам и запись их в новый файл
                    issued_loan2.write(i)
                if k == 1:  # Добавление нового кредита в правильном формате
                    issued_loan2.write("1 10000")
                else:
                    issued_loan2.write("\n" + "1 10000")
                issued_loan2.close()

                # Изменение Бюджета игрока
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                money_file2.write(str(int(money_file) + 10000))
                money_file2.close()
            elif (x >= 650) and (x <= 950) and (y >= 480) and (y <= 520):  # Проверка на оформление 2 кредита
                # Получение информации про оформленные кредиты
                issued_loan = open("issued loan.txt", "r").readlines()
                if issued_loan[0] == "0":  # Проверка не пуст ли файл с оформленными кредитами
                    k = 1
                else:
                    k = 0
                # Создание пустого файла с оформленными кредитами
                issued_loan2 = open("issued loan.txt", "w")
                for i in issued_loan[k:]:  # проход по всем оформелнны кредитам и запись их в новый файл
                    issued_loan2.write(i)
                if k == 1:  # Добавление нового кредита в правильном формате
                    issued_loan2.write("2 200000")
                else:
                    issued_loan2.write("\n" + "2 200000")
                issued_loan2.close()

                # Изменение Бюджета игрока
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                money_file2.write(str(int(money_file) + 200000))
                money_file2.close()
            elif (x >= 650) and (x <= 950) and (y >= 560) and (y <= 600):  # Проверка на оформление 3 кредита
                # Получение информации про оформленные кредиты
                issued_loan = open("issued loan.txt", "r").readlines()
                if issued_loan[0] == "0":  # Проверка не пуст ли файл с оформленными кредитами
                    k = 1
                else:
                    k = 0
                # Создание пустого файла с оформленными кредитами
                issued_loan2 = open("issued loan.txt", "w")
                for i in issued_loan[k:]:  # проход по всем оформелнны кредитам и запись их в новый файл
                    issued_loan2.write(i)
                if k == 1:  # Добавление нового кредита в правильном формате
                    issued_loan2.write("3 3000000")
                else:
                    issued_loan2.write("\n" + "3 3000000")
                issued_loan2.close()

                # Изменение Бюджета игрока
                money_file = open("money.txt", "r").read()
                money_file2 = open("money.txt", "w")
                money_file2.write(str(int(money_file) + 3000000))
                money_file2.close()


class Game:  # Окно Игра
    def __init__(self):
        pass

    def render(self, screen):  # Создание интерфейса окна "Игра"
        # Добавление картинок
        screen.blit(pygame.transform.scale(pygame.image.load("sky1png.png"), (1000, 730)), (0, 0))  # Картинка фона
        screen.blit(pygame.transform.scale(pygame.image.load("back.jpg"), (80, 60)), (20, 20))  # Картинка Назад
        screen.blit(pygame.transform.scale(pygame.image.load("toplivo.png"), (70, 60)), (620, -13))  # Картинка топлива
        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), (810, 5))  # Картинка денег

        # Изменение размера текста
        font = pygame.font.Font(None, 30)
        # Вывод важной информации
        text = font.render("Один полет стоит 10000 ml топлива", 1, (100, 255, 100))
        screen.blit(text, (300, 110))

        if LOSING == 1:  # Проверка не проиграна ли была игра
            # Вывод результата проигрыша
            font = pygame.font.Font(None, 80)
            text = font.render("ВЫ ПРОИГРАЛИ :(", 1, (255, 100, 100))
            screen.blit(text, (230, 500))
            font = pygame.font.Font(None, 30)

        # Получение информации про удачные полеты и вывод ее на экран
        successful_flights = open("successful flights.txt", "r").read()
        text = font.render(str("УДАЧНЫЕ ПОЛЕТЫ: " + str(successful_flights)), 1, (100, 255, 100))
        screen.blit(text, (300, 20))

        # Получение информации про количество топлива и денег
        money_file = open("money.txt", "r").read()
        toplivo_file = open("fuel(toplivo).txt", "r").read()
        money = str(money_file) + " руб"
        fuel = str(toplivo_file) + " ml"

        # Вывод информации про топливо и деньги на экран
        text = font.render(money, 1, (100, 255, 100))
        screen.blit(text, (860, 20))
        text = font.render(fuel, 1, (100, 255, 100))
        screen.blit(text, (665, 20))

        global I, GAME

        if I != 0 and GAME == 0:  # Проверка не остановили ли игру
            # Изменение размера текста
            font = pygame.font.Font(None, 35)
            # Создание кнопки ПРОДОЛЖИТЬ
            pygame.draw.rect(screen,
                             (255, 255, 255),
                             (200, 300, 200, 80), 0)
            text = font.render("ПРОДОЛЖИТЬ", 1, (100, 255, 100))
            screen.blit(text, (205, 330))

            # Создание кнопки МЕНЮ
            pygame.draw.rect(screen,
                             (255, 255, 255),
                             (500, 300, 200, 80), 0)
            text = font.render("МЕНЮ", 1, (100, 255, 100))
            screen.blit(text, (560, 330))
        elif GAME != 0:  # Проверка не выйграли ли игру
            # Изменение размера текста
            font = pygame.font.Font(None, 35)
            # Создание кнопки НОВАЯ ИГРА
            pygame.draw.rect(screen,
                             (255, 255, 255),
                             (200, 300, 200, 80), 0)
            text = font.render("НОВАЯ ИГРА", 1, (100, 255, 100))
            screen.blit(text, (220, 325))
            # Создание кнопки МЕНЮ
            pygame.draw.rect(screen,
                             (255, 255, 255),
                             (500, 300, 200, 80), 0)
            text = font.render("МЕНЮ", 1, (100, 255, 100))
            screen.blit(text, (560, 330))

        elif I == 0 and GAME == 0:  # Проверка не были ли игр раньше
            # Изменение размера текста
            font = pygame.font.Font(None, 40)
            # Создание кнопки ИГРАТЬ
            pygame.draw.rect(screen,
                             (255, 255, 255),
                             (390, 300, 200, 80), 0)
            text = font.render("ИГРАТЬ", 1, (100, 255, 100))
            screen.blit(text, (440, 325))

    def get_cell(self, mouse_pos):  # Проверка куда кликнул пользователь
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]

        global I, GAME, SPEEDX, WIDTH2, WIDTH3, WIDTH4, WIDTH5,\
            WIDTH6, MONEY1, MONEY2, MONEY3, MONEY4, MONEY5, MONEY6, MONEY7, LOSING

        if (x >= 20) and (x <= 100) and (y >= 20) and (y <= 80):  # Проверка не нажали ли на кнопку Назад
            # Обнуление перемещение ракеты
            SPEEDX = 0

            # Обнуление разрешение на игру
            play_file = open("play.txt", "w")
            play_file.write("0")
            play_file.close()

            # Изменение окна
            claas = open("Class.txt", "w")
            claas.write("Menu")
            claas.close()
        if I != 0 and GAME == 0:  # Проверка не остановили ли игру
            # Обнуление выйгрыша
            GAME = 0
            if (x >= 200) and (x <= 400) and (y >= 300) and (y <= 380):  # проверка нажали ли на кнопку ПРОДОЛЖИТЬ
                # Изменение окна
                claas = open("Class.txt", "w")
                claas.write("Play")
                claas.close()
            elif (x >= 500) and (x <= 700) and (y >= 300) and (y <= 380):  # проверка нажали ли на кнопку МЕНЮ
                # Обнуление перемещения и проигрыша
                I = 0
                SPEEDX = 0
                LOSING = 0

                # Обнуление разрешение на игру
                play_file = open("play.txt", "w")
                play_file.write("0")
                play_file.close()

                # Изменение окна
                claas = open("Class.txt", "w")
                claas.write("Menu")
                claas.close()

        elif GAME != 0:  # Проверка не выйграли ли игру
            if (x >= 200) and (x <= 400) and (y >= 300) and (y <= 380):  # проверка нажали ли на кнопку НОВАЯ ИГРА
                # создание рандомного места начала полета препядствий
                WIDTH2 = randint(300, 1300)
                WIDTH3 = randint(300, 1300)
                WIDTH4 = randint(-200, 700)
                WIDTH5 = randint(700, 1300)
                WIDTH6 = randint(-200, 300)

                # создание рандомного места монеток
                MONEY1 = (randint(50, 950), randint(50, 600))
                MONEY2 = (randint(50, 950), randint(50, 600))
                MONEY3 = (randint(50, 950), randint(50, 600))
                MONEY4 = (randint(50, 950), randint(50, 600))
                MONEY5 = (randint(50, 950), randint(50, 600))
                MONEY6 = (randint(50, 950), randint(50, 600))
                MONEY7 = (randint(50, 950), randint(50, 600))

                # обнуление перемещения, выйгрыша и проигрыша
                I = 0
                GAME = 0
                SPEEDX = 0
                LOSING = 0

                os.system("formula.py")  # Открытие дополнительного файла с формулой
                play_file = open("play.txt", "r").read()  # Получение разрешения на игру

                if play_file == "1":  # Разрешена ли игра
                    # Тратим топливо
                    toplivo_file = open("fuel(toplivo).txt", "r").read()
                    toplivo_file2 = open("fuel(toplivo).txt", "w")
                    toplivo_file2.write(str(int(toplivo_file) - 10000))
                    toplivo_file2.close()

                    # Изменение окна
                    claas = open("Class.txt", "w")
                    claas.write("Play")
                    claas.close()
            elif (x >= 500) and (x <= 700) and (y >= 300) and (y <= 380):  # проверка нажали ли на кнопку МЕНЮ
                # обнуление перемещения, выйгрыша и проигрыша
                I = 0
                GAME = 0
                SPEEDX = 0
                LOSING = 0

                # Обнуление разрешение на игру
                play_file = open("play.txt", "w")
                play_file.write("0")
                play_file.close()

                # Изменение окна
                claas = open("Class.txt", "w")
                claas.write("Menu")
                claas.close()

        elif I == 0 and GAME == 0:  # Проверка не было ли игр
            if (x >= 390) and (x <= 590) and (y >= 300) and (y <= 380):  # проверка нажали ли на кнопку ИГРАТЬ
                # обнуление проигрыша
                LOSING = 0
                # создание рандомного места начала полета препядствий
                WIDTH2 = randint(300, 1300)
                WIDTH3 = randint(300, 1300)
                WIDTH4 = randint(-200, 700)
                WIDTH5 = randint(700, 1300)
                WIDTH6 = randint(-200, 300)

                # создание рандомного места монеток
                MONEY1 = (randint(50, 950), randint(50, 600))
                MONEY2 = (randint(50, 950), randint(50, 600))
                MONEY3 = (randint(50, 950), randint(50, 600))
                MONEY4 = (randint(50, 950), randint(50, 600))
                MONEY5 = (randint(50, 950), randint(50, 600))
                MONEY6 = (randint(50, 950), randint(50, 600))
                MONEY7 = (randint(50, 950), randint(50, 600))

                os.system("formula.py")  # Открытие дополнительного файла с формулой
                play_file = open("play.txt", "r").read()  # Получение разрешения на игру

                if play_file == "1":  # Разрешена ли игра
                    # Тратим топливо
                    toplivo_file = open("fuel(toplivo).txt", "r").read()
                    toplivo_file2 = open("fuel(toplivo).txt", "w")
                    toplivo_file2.write(str(int(toplivo_file) - 10000))
                    toplivo_file2.close()

                    # Изменение окна
                    claas = open("Class.txt", "w")
                    claas.write("Play")
                    claas.close()

    def buy_team(self, mouse_pos):
        pass


class Play(pygame.sprite.Sprite):  # Окно игры
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        global I, SPEEDX, GAME, MONEY1, MONEY2, MONEY3, MONEY4, MONEY5, MONEY6, MONEY7, LOSING
        self.i = I

        # Получение информации о фоне
        background_file = open("background(fon).txt", "r").readlines()
        purchases = open("purchases(pokupki).txt", "r").readlines()
        n_2 = int(purchases[int(purchases[0]) + 1])
        if int(background_file[0]) == n_2 - 1:
            background = purchases[int(background_file[0]) + 1 + int(purchases[0]) + 1]
        else:
            background = purchases[int(background_file[0]) + 1 + int(purchases[0]) + 1][:-1]

        # отображение фона, кнопки стоп
        screen.blit(pygame.transform.scale(pygame.image.load(background), (1000, 730)), (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("stop.jpg"), (80, 60)), (20, 20))

        # Получение информации о выбранной ракете
        purchases = open("purchases(pokupki).txt", "r").readlines()
        rocket_file = open("rocket.txt", "r").readlines()
        rocket = purchases[int(rocket_file[0]) + 1][:-1]

        if background != "start square.png":  # Проверка какая карта выбрана и откуда надо начинать полет
            kart = 45
        else:
            kart = 100

        # Сдвиг всех объектов на один пиксель
        I = I + 1
        self.i = I
        # Размещение картинок и спрайтов монет
        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), MONEY1)
        money1_image = pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40))
        money1_rect = money1_image.get_rect()
        money1_rect.center = (MONEY1[0] + 40, MONEY1[1] + 40)

        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), MONEY2)
        money2_image = pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40))
        money2_rect = money2_image.get_rect()
        money2_rect.center = (MONEY2[0] + 40, MONEY2[1] + 40)

        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), MONEY3)
        money3_image = pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40))
        money3_rect = money3_image.get_rect()
        money3_rect.center = (MONEY3[0] + 40, MONEY3[1] + 40)

        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), MONEY4)
        money4_image = pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40))
        money4_rect = money4_image.get_rect()
        money4_rect.center = (MONEY4[0] + 40, MONEY4[1] + 40)

        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), MONEY5)
        money5_image = pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40))
        money5_rect = money5_image.get_rect()
        money5_rect.center = (MONEY5[0] + 40, MONEY5[1] + 40)

        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), MONEY6)
        money6_image = pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40))
        money6_rect = money6_image.get_rect()
        money6_rect.center = (MONEY6[0] + 40, MONEY6[1] + 40)

        screen.blit(pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40)), MONEY7)
        money7_image = pygame.transform.scale(pygame.image.load("money simbol.png"), (40, 40))
        money7_rect = money7_image.get_rect()
        money7_rect.center = (MONEY7[0] + 40, MONEY7[1] + 40)

        # Создание картинки ракеты
        self.image = pygame.transform.scale(pygame.image.load(rocket), (25, 50))
        self.rect = self.image.get_rect()

        # Получение информации об нажатых кнопках
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:  # Нажата левая стрелка
            SPEEDX += -8
        elif keystate[pygame.K_RIGHT]:  # Нажата правая стрелка
            SPEEDX += 8
        # если ракета вышла за пределы поля, то просто появляется с другой стороны поля
        if SPEEDX <= -500 or SPEEDX >= 500:
            SPEEDX = -1 * SPEEDX

        # Размещение картинки ракеты
        self.rect.bottom = WIDTH - kart - self.i
        self.rect.centerx = HEIGHT / 2 + SPEEDX

        # Размещение спрайта ракеты
        rocket_image = pygame.transform.scale(pygame.image.load(rocket), (25, 50))
        rocket_rect = rocket_image.get_rect()
        rocket_rect.center = (HEIGHT / 2 + SPEEDX, WIDTH - kart - self.i)

        # Размещение картинки и спрайта метеорита
        screen.blit(pygame.transform.scale(pygame.image.load("meteorit.png"), (70, 70)),
                    (WIDTH2 - self.i, HEIGHT2 + self.i))  # картинка
        # спрайт
        meteorit_image = pygame.transform.scale(pygame.image.load("meteorit.png"), (70, 70))
        meteorit_rect = meteorit_image.get_rect()
        meteorit_rect.center = (WIDTH2 - self.i + 35, HEIGHT2 + self.i + 70)

        # Размещение картинки и спрайта самолета
        screen.blit(pygame.transform.scale(pygame.image.load("samolet.png"), (100, 50)),
                    (WIDTH3 - self.i, HEIGHT3))  # картинка
        # спрайт
        samolet_image = pygame.transform.scale(pygame.image.load("samolet.png"), (100, 50))
        samolet_rect = samolet_image.get_rect()
        samolet_rect.center = (WIDTH3 - self.i + 50, HEIGHT3 + 50)

        # Размещение картинки и спрайта нло
        screen.blit(pygame.transform.scale(pygame.image.load("nlo.png"), (70, 60)),
                    (WIDTH4 + self.i, HEIGHT4 + self.i))  # картинка
        # спрайт
        nlo_image = pygame.transform.scale(pygame.image.load("nlo.png"), (70, 50))
        nlo_rect = nlo_image.get_rect()
        nlo_rect.center = (WIDTH4 + self.i + 35, HEIGHT4 + self.i + 50)

        # Размещение картинки и спрайта птичек1
        screen.blit(pygame.transform.scale(pygame.image.load("ptichki1.png"), (80, 30)),
                    (WIDTH5 - self.i, HEIGHT5))  # картинка
        # спрайт
        ptichki1_image = pygame.transform.scale(pygame.image.load("ptichki1.png"), (80, 30))
        ptichki1_rect = ptichki1_image.get_rect()
        ptichki1_rect.center = (WIDTH5 - self.i + 40, HEIGHT5 + 30)

        # Размещение картинки и спрайта птичек2
        screen.blit(pygame.transform.scale(pygame.image.load("ptichki2.png"), (80, 30)),
                    (WIDTH6 + self.i, HEIGHT6))  # картинка
        # спрайт
        ptichki2_image = pygame.transform.scale(pygame.image.load("ptichki2.png"), (80, 30))
        ptichki2_rect = ptichki2_image.get_rect()
        ptichki2_rect.center = (WIDTH6 + self.i + 40, HEIGHT6 + 30)

        if rocket_rect.colliderect(samolet_rect) or rocket_rect.colliderect(meteorit_rect) or \
                rocket_rect.colliderect(nlo_rect) or rocket_rect.colliderect(ptichki1_rect) or\
                rocket_rect.colliderect(ptichki2_rect):  # проверка на столкновение ракеты и препядствия
            # изменение важных данных
            LOSING = 1
            I = 0
            GAME = 1
            SPEEDX = 0

            # обнуление разрешения на игру
            play_file = open("play.txt", "w")
            play_file.write("0")
            play_file.close()

            # изменение окна
            claas = open("Class.txt", "w")
            claas.write("Game")
            claas.close()
        elif rocket_rect.colliderect(money1_rect) or rocket_rect.colliderect(money2_rect) or \
                rocket_rect.colliderect(money3_rect) or rocket_rect.colliderect(money4_rect) or \
                rocket_rect.colliderect(money5_rect) or rocket_rect.colliderect(money6_rect) or \
                rocket_rect.colliderect(money7_rect):  # проверка на столкновение ракеты и монеты
            # Изменение бюджета
            money_file = open("money.txt", "r").read()
            money_file2 = open("money.txt", "w")
            money_file2.write(str(int(money_file) + 500))
            money_file2.close()

            # Сдвигаем ненужные монетки с экрана
            if rocket_rect.colliderect(money1_rect):
                MONEY1 = (3600, 3600)
            elif rocket_rect.colliderect(money2_rect):
                MONEY2 = (3600, 3600)
            elif rocket_rect.colliderect(money3_rect):
                MONEY3 = (3600, 3600)
            elif rocket_rect.colliderect(money4_rect):
                MONEY4 = (3600, 3600)
            elif rocket_rect.colliderect(money5_rect):
                MONEY5 = (3600, 3600)
            elif rocket_rect.colliderect(money6_rect):
                MONEY6 = (3600, 3600)
            elif rocket_rect.colliderect(money7_rect):
                MONEY7 = (3600, 3600)

        if self.i > WIDTH - 100:  # Если мы выйграли
            # Изменение важных данных
            I = 0
            GAME = 1
            SPEEDX = 0

            # Увеличение удачных полетов
            successful_flights = open("successful flights.txt", "r").read()
            successful_flights2 = open("successful flights.txt", "w")
            successful_flights2.write(str(int(successful_flights) + 1))
            successful_flights2.close()

            # Изменение бюджеа игрока
            money_file = open("money.txt", "r").read()
            money_file2 = open("money.txt", "w")
            money_file2.write(str(int(money_file) + 5000))
            money_file2.close()

            # Обнуляем разрешение на полет
            play_file = open("play.txt", "w")
            play_file.write("0")
            play_file.close()

            # Изменение окна
            claas = open("Class.txt", "w")
            claas.write("Game")
            claas.close()

    def get_cell(self, mouse_pos):  # Проверка куда кликнул пользователь
        # Вынес координат в числовые переменные
        x = mouse_pos[0]
        y = mouse_pos[1]
        if (x >= 20) and (x <= 100) and (y >= 20) and (y <= 80):  # Проверка нажал ли пользоваель кнопку ИГРАТЬ
            # Изменение окна
            claas = open("Class.txt", "w")
            claas.write("Game")
            claas.close()


if __name__ == '__main__':
    # Вводим константы
    HEIGHT = 1000
    WIDTH = 730
    SIZE = (HEIGHT, WIDTH)
    FPS = 30

    # Создаем полезные штучки и окна
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Симулятор ракеты')
    clock = pygame.time.Clock()
    flag = False
    running = True

    while running:  # Проходим кучу раз ока окно не закроют
        # Получение информации о выбранном классе
        nameclass = open("Class.txt", "r").read()

        # Открытие правильного окна
        if nameclass == "Menu":
            clas = Menu()
        elif nameclass == "Game":
            clas = Game()
        elif nameclass == "Shop":
            clas = Shop()
        elif nameclass == "Bank":
            clas = Bank()
        elif nameclass == "Settings":
            clas = Settings()

        if nameclass == "Play":  # Если запустили саму игру
            # Создаем доп полезные шучки
            all_sprites = pygame.sprite.Group()
            clas = Play()
            all_sprites.add(clas)
            clock.tick(FPS)

            # взаимодействия игрока с клавиатурой или мышкой
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.type != pygame.K_SPACE:  # кликнули мышкой
                    clas.get_cell(event.pos)

            # отправка нужной инфы в класс
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
        else:
            # взаимодействия игрока с клавиатурой или мышкой
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    flag = True
                if event.type == pygame.KEYUP:
                    flag = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.type != pygame.K_SPACE:  # кликнули мышкой
                    clas.get_cell(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN and flag:  # Если нажали пробел и кликнули мышкой одновременно
                    clas.buy_team(event.pos)

            # отправка нужной инфы в класс
            clas.render(screen)
            pygame.display.flip()

    # Закрытие файла
    pygame.quit()