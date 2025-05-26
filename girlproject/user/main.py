
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QPushButton
import sys
from girlproject.ui import Registration, MainMenu, Login
from database_manager import DatabaseManager

# Глобальний об'єкт для роботи з базою даних
db_manager = DatabaseManager()
current_user = None  # Зберігає інформацію про поточного користувача

class MyLoginWindow(QtWidgets.QMainWindow, Login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Підключаємо кнопку "Увійти без реєстрації" до функції переходу в головне меню
        self.b_enterWithoutReg.clicked.connect(self.open_main_menu)

        # Підключаємо кнопку "Зареєструйтеся" до функції переходу в реєстрацію
        self.b_enterMainWindow2.clicked.connect(self.open_registration)

        # Додаємо функціонал для кнопки входу (якщо потрібно)
        self.b_enter.clicked.connect(self.login_with_credentials)

    def login_with_credentials(self):
        """Вхід з обліковими даними"""
        global current_user

        # Припускаємо, що поля для логіну мають назви le_username і le_password
        if not (hasattr(self, 'le_username') and hasattr(self, 'le_password')):
            print("Поля для входу не знайдено")
            return

        username = self.le_username.text().strip()
        password = self.le_password.text()

        if not username or not password:
            self.show_login_message("Помилка", "Введіть ім'я користувача та пароль", QtWidgets.QMessageBox.Warning)
            return

        # Спроба аутентифікації
        success, user_data, message = db_manager.authenticate_user(username, password)

        if success:
            # Успішний вхід
            current_user = {
                'user_id': user_data[0],
                'username': user_data[1]
            }

            self.show_login_message("Успіх", f"Вітаємо, {username}!", QtWidgets.QMessageBox.Information)

            # Очищуємо поля
            self.le_username.clear()
            self.le_password.clear()

            # Переходимо в головне меню
            self.main_menu_window = MyMainMenu()
            self.main_menu_window.show()
            self.close()
        else:
            # Помилка входу
            self.show_login_message("Помилка входу", message, QtWidgets.QMessageBox.Critical)

    def show_login_message(self, title, message, icon_type):
        """Показує повідомлення користувачу в вікні логіну"""
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon_type)

        # Стилізація повідомлення
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #2b2b2b;
                color: white;
            }
            QMessageBox QLabel {
                color: white;
                font-weight: bold;
                background: transparent;
            }
            QMessageBox QPushButton {
                color: white;
                font-weight: bold;
                background-color: #444;
                border: 1px solid #888;
                padding: 5px 15px;
                min-width: 80px;
            }
            QMessageBox QPushButton:hover {
                background-color: #666;
            }
        """)

        msg_box.exec_()
    def open_main_menu(self):
        """Відкриває головне меню та закриває вікно входу"""
        self.main_menu_window = MyMainMenu()
        self.main_menu_window.show()
        self.close()  # Закриваємо вікно входу

    def open_registration(self):
        """Відкриває вікно реєстрації та закриває вікно входу"""
        self.registration_window = MyRegistrationWindow()
        self.registration_window.show()
        self.close()  # Закриваємо вікно входу


class MyRegistrationWindow(QtWidgets.QMainWindow, Registration.Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Підключаємо кнопку "Увійдіть" до функції переходу назад
        self.b_enterMainWindow.clicked.connect(self.back_to_login)

        # Підключаємо кнопку "Увійти без реєстрації" до функції переходу в головне меню
        self.b_enterWithoutReg2.clicked.connect(self.open_main_menu)

        # Підключаємо кнопку реєстрації (pushButton_4) до функції реєстрації
        self.pushButton_4.clicked.connect(self.register_user)

    def register_user(self):
        """Реєстрація нового користувача"""
        global current_user

        # Отримуємо дані з полів введення
        username = self.le_regUsername.text().strip()
        password = self.le_regPassword.text()

        # Валідація вводу
        if not username:
            self.show_message("Помилка", "Введіть ім'я користувача", QtWidgets.QMessageBox.Warning)
            return

        if not password:
            self.show_message("Помилка", "Введіть пароль", QtWidgets.QMessageBox.Warning)
            return

        # Спроба реєстрації через базу даних
        success, message = db_manager.register_user(username, password)

        if success:
            # Успішна реєстрація - аутентифікуємо користувача
            auth_success, user_data, auth_message = db_manager.authenticate_user(username, password)

            if auth_success:
                # Зберігаємо інформацію про поточного користувача
                current_user = {
                    'user_id': user_data[0],
                    'username': user_data[1]
                }

                # Показуємо повідомлення про успішну реєстрацію
                self.show_message("Успіх", f"Вітаємо, {username}! Реєстрацію завершено.",
                                  QtWidgets.QMessageBox.Information)

                # Очищуємо поля
                self.le_regUsername.clear()
                self.le_regPassword.clear()

                # Переходимо одразу в головне меню
                self.open_main_menu_with_user()
            else:
                self.show_message("Помилка", "Реєстрацію завершено, але не вдалося увійти автоматично",
                                  QtWidgets.QMessageBox.Warning)
                self.back_to_login()
        else:
            # Помилка реєстрації
            self.show_message("Помилка реєстрації", message, QtWidgets.QMessageBox.Critical)

    def open_main_menu_with_user(self):
        """Відкриває головне меню з інформацією про користувача"""
        self.main_menu_window = MyMainMenu()
        self.main_menu_window.show()
        self.close()  # Закриваємо вікно реєстрації

    def show_message(self, title, message, icon_type):
        """Показує повідомлення користувачу"""
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon_type)

        # Стилізація повідомлення
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #2b2b2b;
                color: white;
            }
            QMessageBox QLabel {
                color: white;
                font-weight: bold;
                background: transparent;
            }
            QMessageBox QPushButton {
                color: white;
                font-weight: bold;
                background-color: #444;
                border: 1px solid #888;
                padding: 5px 15px;
                min-width: 80px;
            }
            QMessageBox QPushButton:hover {
                background-color: #666;
            }
        """)

        msg_box.exec_()

    def back_to_login(self):
        """Повертається до вікна входу"""
        self.login_window = MyLoginWindow()
        self.login_window.show()
        self.close()

    def open_main_menu(self):
        """Відкриває головне меню та закриває вікно реєстрації"""
        self.main_menu_window = MyMainMenu()
        self.main_menu_window.show()
        self.close()  # Закриваємо вікно входу


class MyMainMenu(QtWidgets.QMainWindow, MainMenu.Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Встановлюємо ім'я користувача, якщо він увійшов
        if current_user:
            # Припускаємо, що la_username - це QLabel для відображення імені користувача
            if hasattr(self, 'la_username'):
                self.la_username.setText(current_user['username'])

        # Встановлюємо центрування для QLabel з зображенням
        self.l_OrigImage.setAlignment(Qt.AlignCenter)

        # Підключаємо перший listWidget до першого stackedWidget
        self.listWidget.currentRowChanged.connect(self.switch_stacked_widget)

        # Підключаємо другий listWidget до другого stackedWidget
        self.listWidget_2.currentRowChanged.connect(self.switch_stacked_widget_2)
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)

        self.listWidget_2.setCurrentRow(0)
        self.stackedWidget_2.setCurrentIndex(0)
        # Підключаємо кнопку для виходу з профілю b_exit
        self.b_exit.clicked.connect(self.exit_profile)

        # Підключаємо кнопки для входу в файловий діалог
        self.b_AddOrigImage0.clicked.connect(self.enterFileDialog)
        self.b_AddOrigImage1.clicked.connect(self.enterFileDialog)
        self.b_AddOrigImage2.clicked.connect(self.enterFileDialog)
        self.b_AddOrigImageEnc.clicked.connect(self.enterFileDialog)
        self.b_AddOrigImageDec.clicked.connect(self.enterFileDialog)
        # Підключаємо кнопки для прибирання оригінального зображення
        self.b_deleteOrigImage0.clicked.connect(self.closeOrigImage)
        self.b_deleteOrigImage1.clicked.connect(self.closeOrigImage)
        self.b_deleteOrigImage2.clicked.connect(self.closeOrigImage)
        self.b_deleteOrigImageEnc.clicked.connect(self.closeOrigImage)
        self.b_deleteOrigImageDec.clicked.connect(self.closeOrigImage)
       # Налаштування кнопок як checkable для сторінки KrivaKoxa
        try:
            self.pushButton.setCheckable(True)
            self.pushButton_2.setCheckable(True)
            self.pushButton_3.setCheckable(True)
            self.pushButton.clicked.connect(self.check_button)
            self.pushButton_2.clicked.connect(self.check_button)
            self.pushButton_3.clicked.connect(self.check_button)
        except AttributeError:
            print("Помилка: Одна або більше кнопок (pushButton, pushButton_2, pushButton_3) не знайдені")

        # Налаштування кнопок як checkable для сторінки NoisePerlin
        try:
            self.pushButton_4.setCheckable(True)
            self.pushButton_5.setCheckable(True)
            self.pushButton_6.setCheckable(True)
            self.pushButton_4.clicked.connect(self.check_button)
            self.pushButton_5.clicked.connect(self.check_button)
            self.pushButton_6.clicked.connect(self.check_button)
        except AttributeError:
            print("Помилка: Одна або більше кнопок (pushButton_4, pushButton_5, pushButton_6) не знайдені")

        # Налаштування кнопок як checkable для сторінки GameOfLife
        try:
            self.pushButton_7.setCheckable(True)
            self.pushButton_8.setCheckable(True)
            self.pushButton_9.setCheckable(True)
            self.pushButton_7.clicked.connect(self.check_button)
            self.pushButton_8.clicked.connect(self.check_button)
            self.pushButton_9.clicked.connect(self.check_button)
        except AttributeError:
            print("Помилка: Одна або більше кнопок (pushButton_7, pushButton_8, pushButton_9) не знайдені")

    def check_button(self):
        """Забезпечує, що лише одна кнопка з відповідної групи може бути вибраною"""
        sender = self.sender()  # Отримуємо кнопку, яка була натиснута

        # Групи кнопок для кожної сторінки
        kriva_koxa_buttons = [self.pushButton, self.pushButton_2, self.pushButton_3]
        noise_perlin_buttons = [self.pushButton_4, self.pushButton_5, self.pushButton_6]
        game_of_life_buttons = [self.pushButton_7, self.pushButton_8, self.pushButton_9]

        # Визначаємо, до якої групи належить натиснута кнопка
        if sender in kriva_koxa_buttons:
            buttons = kriva_koxa_buttons
        elif sender in noise_perlin_buttons:
            buttons = noise_perlin_buttons
        elif sender in game_of_life_buttons:
            buttons = game_of_life_buttons
        else:
            print("Помилка: Натиснута кнопка не належить до жодної групи")
            return

        # Скидаємо стан checked для всіх кнопок у групі, крім натиснутої
        for button in buttons:
            if button != sender:
                button.setChecked(False)

    def show_message(self, title, message, icon_type):
        """Показує стилізоване повідомлення користувачу"""
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon_type)
        msg_box.setStyleSheet("""
              QMessageBox {
                  background-color: #2b2b2b;
                  color: white;
              }
              QMessageBox QLabel {
                  color: white;
                  font-weight: bold;
                  background: transparent;
              }
              QMessageBox QPushButton {
                  color: white;
                  font-weight: bold;
                  background-color: #444;
                  border: 1px solid #888;
                  padding: 5px 15px;
                  min-width: 80px;
              }
              QMessageBox QPushButton:hover {
                  background-color: #666;
              }
          """)
        msg_box.exec_()


    def get_label_by_button(self, button):
        """Визначає відповідний QLabel за кнопкою"""
        button_name = button.objectName()

        if '0' in button_name:
            return self.l_OrigImage
        elif '1' in button_name:
            return self.l_OrigImage_pg1
        elif '2' in button_name:
            return self.l_OrigImage_pg2
        elif 'Enc' in button_name:
            return self.l_OrigImageEnc
        elif 'Dec' in button_name:
            return self.l_OrigImageDec

        return None

    def enterFileDialog(self):
        """Файлове вікно для вибору фото оригіналу тільки в форматі .bmp"""
        # Визначаємо, яка кнопка була натиснута
        sender = self.sender()
        target_label = self.get_label_by_button(sender)

        if not target_label:
            print("Помилка: не вдалося визначити цільовий QLabel")
            return

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Виберіть зображення оригіналу",
            "",
            "Зображення у (*.bmp)"
        )

        if file_name:
            print(f"Обрано файл: {file_name}")
            # завантажуємо
            pixmap = QPixmap(file_name)

            label_size = target_label.size()
            # Масштабуємо зображення
            scaled_pixmap = pixmap.scaled(label_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            # Встановлюємо вирівнювання по центру
            target_label.setAlignment(Qt.AlignCenter)

            # Виводимо в QLabel
            target_label.setPixmap(scaled_pixmap)

    def closeOrigImage(self):
        """Очищує вміст відповідного QLabel"""
        # Визначаємо, яка кнопка була натиснута
        sender = self.sender()
        target_label = self.get_label_by_button(sender)

        if not target_label:
            print("Помилка: не вдалося визначити цільовий QLabel")
            return

        if target_label.pixmap() is not None:
            target_label.clear()
            print(f"Зображення видалено з {target_label.objectName()}")

    def switch_stacked_widget(self, current_row):
        """Перемикає перший QStackedWidget на відповідний індекс (вкладка з методами обробки)"""
        self.stackedWidget.setCurrentIndex(current_row)

    def switch_stacked_widget_2(self, current_row):
        """Перемикає другий QStackedWidget на відповідний індекс (вкладка стеганографія)"""
        self.stackedWidget_2.setCurrentIndex(current_row)

    def exit_profile(self):
        """Вихід з профілю з підтвердженням"""
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle('Підтвердження виходу')
        msg_box.setText('Ви впевнені, що хочете вийти з профілю?')
        msg_box.setIcon(QtWidgets.QMessageBox.Question)

        yes_button = msg_box.addButton("Так", QtWidgets.QMessageBox.YesRole)
        no_button = msg_box.addButton("Ні", QtWidgets.QMessageBox.NoRole)
        yes_button.setStyleSheet("""
        color:white;
        border: 1px solid #FFFFF;
        """)
        no_button.setStyleSheet("""
        color:white;
        border: 1px solid #FFFFF;
        """)
        msg_box.setStyleSheet("""
            QLabel {
                color: white;
                font-weight: bold;
                background: transparent;
            }

            QPushButton {
                color: white;
                font-weight: bold;
                background-color: #444;
                border: 1px solid #888;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #666;
            }

        """)

        msg_box.exec_()

        if msg_box.clickedButton() == yes_button:
            self.close()


if __name__ == "__main__":
    # Ініціалізація бази даних та статусу
    success, steps = db_manager.initialize_database()

    # Статус
    print("=== Ініціалізація бази даних ===")
    for step_name, step_success, message in steps:
        status = "✓ УСПІШНО" if step_success else "✗ ПОМИЛКА"
        print(f"{step_name}: {status} - {message}")

    if success:
        print("\n База даних успішно ініціалізована")
    else:
        print("\n Не вдалося ініціалізувати базу даних")
        # Можна вирішити чи продовжувати роботу програми

    # Start the application
    app = QtWidgets.QApplication(sys.argv)
    login_window = MyLoginWindow()
    login_window.show()
    sys.exit(app.exec_())