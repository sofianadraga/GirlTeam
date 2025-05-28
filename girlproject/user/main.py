import uuid

from PyQt5 import QtWidgets, QtCore
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

        self.b_show.clicked.connect(self.show_elements)
        # Налаштування QScrollArea для вкладки "Генерація"
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1921, 991))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # Контейнер для вмісту QScrollArea
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setMinimumHeight(2500)  # Велика висота для прокрутки

        # Переносимо b_show і b_hide до scrollAreaWidgetContents
        self.b_show.setParent(self.scrollAreaWidgetContents)
        self.b_hide.setParent(self.scrollAreaWidgetContents)
        self.b_show.setGeometry(QtCore.QRect(770, 0, 171, 51))
        self.b_hide.setGeometry(QtCore.QRect(980, 0, 171, 51))

        # Встановлюємо вміст QScrollArea
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Додаємо вертикальну QScrollBar
        self.verticalScrollBar = QtWidgets.QScrollBar(self.tab)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1890, 10, 20, 741))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setVerticalScrollBar(self.verticalScrollBar)

        # Підключаємо кнопку для виходу з профілю b_exit
        self.b_exit.clicked.connect(self.exit_profile)

        # Підключаємо кнопки для входу в файловий діалог
        self.b_AddOrigImage0.clicked.connect(self.enterFileDialog)

        self.b_AddOrigImageEnc.clicked.connect(self.enterFileDialog)
        # Підключаємо кнопки для прибирання оригінального зображення
        self.b_deleteOrigImage0.clicked.connect(self.closeOrigImage)
        self.b_deleteOrigImageEnc.clicked.connect(self.closeOrigImage)

        # Список елементів для керування видимістю на вкладці "Генерація"
        self.tab_elements = [
            self.b_deleteOrigImage0, self.b_AddOrigImage0, self.b_deleteProcImage0, self.b_SaveProcImage0,
            self.l_OrigImage, self.L_ProcImage, self.b_processImage, self.pushButton_1, self.pushButton_2,
            self.pushButton_3, self.colorButton_0_66, self.colorButton_0_67, self.colorButton_0_68,
            self.colorButton_3_66, self.colorButton_3_67, self.colorButton_3_68, self.colorButton_0_69,
            self.colorButton_0_70, self.colorButton_0_71, self.radioButton_1, self.radioButton_2,
            self.radioButton_3
        ]

        for element in self.tab_elements:
            element.setVisible(False)

            # Список елементів для вкладки "Стеганографія"
        self.encryption_elements = [
            self.b_AddOrigImageEnc, self.l_OrigImageEnc, self.b_deleteOrigImageEnc, self.b_deleteProcImageEnc,
            self.l_ProcImageEnc, self.b_SaveProcImageEnc, self.frame_2, self.frame_3
        ]

        # Список елементів для вкладки "Інформація"
        self.info_elements = [self.label_9, self.label_10, self.label_11]

        # Ініціалізація для динамічного додавання елементів
        self.element_groups = []  # Список груп доданих елементів
        self.y_offset = 70  # Початкове зміщення для нових груп

        # Підключаємо сигнали
        self.b_show.clicked.connect(self.add_element_group)
        self.b_hide.clicked.connect(self.remove_element_group)
        self.b_exit.clicked.connect(self.exit_profile)
        self.b_AddOrigImage0.clicked.connect(self.enterFileDialog)
        self.b_AddOrigImageEnc.clicked.connect(self.enterFileDialog)
        self.b_deleteOrigImage0.clicked.connect(self.closeOrigImage)
        self.b_deleteOrigImageEnc.clicked.connect(self.closeOrigImage)
        self.tabWidget.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        """Обробник зміни вкладки."""
        current_tab = self.tabWidget.widget(index)
        if current_tab == self.tab_2:  # Вкладка "Стеганографія"
            self.show_elements()

    def add_element_group(self):
        """Додає новий набір елементів на вкладці 'Генерація'."""
        group_id = str(uuid.uuid4())
        y_offset = self.y_offset

        # Створюємо новий набір елементів
        new_group = []
        for element in self.tab_elements:
            new_element = self._clone_widget(element, group_id, y_offset)
            new_element.setVisible(True)
            new_group.append(new_element)

            # Підключаємо сигнали для відповідних кнопок
            if element.objectName() == "b_AddOrigImage0":
                new_element.clicked.connect(self.enterFileDialog)
            elif element.objectName() == "b_deleteOrigImage0":
                new_element.clicked.connect(self.closeOrigImage)

        self.element_groups.append(new_group)
        self.y_offset += 750  # Збільшуємо зміщення для наступної групи

        # Переміщуємо b_show і b_hide
        self.b_show.setGeometry(QtCore.QRect(770, self.y_offset, 171, 51))
        self.b_hide.setGeometry(QtCore.QRect(980, self.y_offset, 171, 51))

        # Оновлюємо висоту вмісту QScrollArea
        self.scrollAreaWidgetContents.setMinimumHeight(self.y_offset + 1000)

    def remove_element_group(self):
        """Видаляє останній доданий набір елементів."""
        if self.element_groups:
            last_group = self.element_groups.pop()
            for element in last_group:
                element.deleteLater()
            self.y_offset = max(70, self.y_offset - 750)
            self.b_show.setGeometry(QtCore.QRect(770, self.y_offset, 171, 51))
            self.b_hide.setGeometry(QtCore.QRect(980, self.y_offset, 171, 51))
            self.scrollAreaWidgetContents.setMinimumHeight(self.y_offset + 1000)

    def _clone_widget(self, widget, group_id, y_offset):
        """Створює копію віджета з новим ім'ям і зміщеним положенням."""
        if isinstance(widget, QtWidgets.QPushButton):
            new_widget = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            new_widget.setCheckable(widget.isCheckable())
            new_widget.setText(widget.text())
        elif isinstance(widget, QtWidgets.QLabel):
            new_widget = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            new_widget.setAlignment(widget.alignment())
        elif isinstance(widget, QtWidgets.QRadioButton):
            new_widget = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            new_widget.setText(widget.text())
        else:
            return None

        # Копіюємо геометрію зі зміщенням по y
        geom = widget.geometry()
        new_widget.setGeometry(QtCore.QRect(geom.x(), geom.y() + y_offset - 70, geom.width(), geom.height()))
        new_widget.setStyleSheet(widget.styleSheet())
        new_widget.setObjectName(f"{widget.objectName()}_{group_id}")
        return new_widget

    def show_elements(self):
        """Показує всі елементи на поточній вкладці та переміщує кнопки b_show і b_hide на y=800."""
        current_tab = self.tabWidget.currentWidget()
        if current_tab == self.tab:  # Вкладка "Генерація"
            for element in self.tab_elements:
                element.setVisible(True)
            # Переміщення кнопок b_show і b_hide на y=800
            self.b_show.setGeometry(QtCore.QRect(770, 800, 171, 51))
            self.b_hide.setGeometry(QtCore.QRect(980, 800, 171, 51))

    def get_label_by_button(self, button):
        """Визначає відповідний QLabel за кнопкою"""
        button_name = button.objectName()
        print(f"button_name = {button_name}")

        parts = button_name.split('_')
        print(f"parts = {parts}")

        # Якщо є третя частина і вона схожа на UUID (містить дефіси)
        if len(parts) >= 3 and '-' in parts[2]:
            print("Це скопійований елемент")
            # Це скопійований елемент
            base_name = '_'.join(parts[:2])  # b_AddOrigImage0
            group_id = parts[2]  # UUID
            print(f"base_name = {base_name}")
            print(f"group_id = {group_id}")

            # Визначаємо назву відповідного QLabel на основі базової назви кнопки
            target_label_base = None
            if 'AddOrigImage0' in base_name or 'deleteOrigImage0' in base_name:
                target_label_base = 'l_OrigImage'
            elif 'Enc' in base_name:
                target_label_base = 'l_OrigImageEnc'
            elif 'Dec' in base_name:
                target_label_base = 'l_OrigImageDec'

            print(f"target_label_base = {target_label_base}")

            if target_label_base:
                print(f"Шукаємо в {len(self.element_groups)} групах")
                # Знаходимо відповідний QLabel в тій же групі
                for i, group in enumerate(self.element_groups):
                    print(f"Група {i}, елементів: {len(group)}")
                    for j, element in enumerate(group):
                        element_name = element.objectName()
                        print(f"Елемент {j}: {element_name}, тип: {type(element).__name__}")
                        if isinstance(element, QtWidgets.QLabel):
                            print(f"Це QLabel, перевіряємо умови:")
                            expected_name = f"{target_label_base}_{group_id}"
                            print(f"Очікувана назва: {expected_name}")
                            print(f"Фактична назва: {element_name}")
                            if element_name == expected_name:
                                print(f"ЗНАЙДЕНО! Повертаємо {element_name}")
                                return element
        else:
            print("DEBUG: Це оригінальний елемент")
            # Це оригінальний елемент
            if 'AddOrigImage0' in button_name or 'deleteOrigImage0' in button_name:
                print("DEBUG: Повертаємо self.l_OrigImage")
                return self.l_OrigImage
            elif 'Enc' in button_name:
                print("DEBUG: Повертаємо self.l_OrigImageEnc")
                return self.l_OrigImageEnc
            elif 'Dec' in button_name:
                print("DEBUG: Повертаємо self.l_OrigImageDec")
                return self.l_OrigImageDec

        print("DEBUG: Нічого не знайдено, повертаємо None")
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