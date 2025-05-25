
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import hashlib


class DatabaseManager:
    def __init__(self):
        self.DB_NAME = "girlteam"
        self.DB_USER = "sofianadraga"
        self.DB_PASSWORD = "awesomepass123@"
        self.DB_HOST = "girlteam.postgres.database.azure.com"
        self.DB_PORT = "5432"

        self.is_initialized = False

    def test_connection(self):
        """Тестове підключення до сервера PostgreSQL"""
        try:
            conn = psycopg2.connect(
                dbname='postgres',
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT,
                connect_timeout=10
            )
            conn.close()
            return True, "Підключення виконано успішно"
        except psycopg2.Error as e:
            return False, f"Помилка підключення: {e}"

    def create_database(self):
        """Створення бази даних"""
        try:
            conn = psycopg2.connect(
                dbname='postgres',
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT
            )
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conn.cursor()

            # Перевірка чи існує БД
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (self.DB_NAME,))
            exists = cur.fetchone()

            if not exists:
                cur.execute(f'CREATE DATABASE "{self.DB_NAME}"')
                message = f"БД '{self.DB_NAME}' створено"
            else:
                message = f"БД '{self.DB_NAME}' вже існує"

            cur.close()
            conn.close()
            return True, message

        except psycopg2.Error as e:
            return False, f"Помилка при створенні бази даних: {e}"

    def create_tables(self):
        """Створення таблиць в БД"""
        try:
            conn = psycopg2.connect(
                dbname=self.DB_NAME,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT
            )
            cur = conn.cursor()

            # Створення Users table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                user_id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

            # Створення History_table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS History_table (
                history_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES Users(user_id) ON DELETE CASCADE,
                origPath TEXT,
                procPath TEXT,
                procMethod TEXT,
                colors TEXT,
                Enc_message TEXT,
                Dec_message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

            conn.commit()
            cur.close()
            conn.close()
            return True, "Таблиці створено успішно"

        except psycopg2.Error as e:
            return False, f"Помилка створення таблиць: {e}"

    def get_connection(self):
        """Отримання підключення до БД"""
        try:
            conn = psycopg2.connect(
                dbname=self.DB_NAME,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT
            )
            return conn
        except psycopg2.Error as e:
            print(f"Помилка підключення до бази даних: {e}")
            return None

    def initialize_database(self):
        """Ініціалізація БД"""
        steps = []

        # Тестове підключення
        success, message = self.test_connection()
        steps.append(("Перевірка з'єднання", success, message))
        if not success:
            return False, steps

        # Створення БД
        success, message = self.create_database()
        steps.append(("Створення бази даних", success, message))
        if not success:
            return False, steps

        # Створення Таблиць
        success, message = self.create_tables()
        steps.append(("Створення таблиці", success, message))
        if not success:
            return False, steps

        self.is_initialized = True
        return True, steps

    def hash_password(self, password):
        """Хешування пароля для безпечного зберігання"""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def register_user(self, username, password):
        """Реєстрація нового користувача"""
        if not username or not password:
            return False, "Ім'я користувача та пароль не можуть бути порожніми"

        if len(username.strip()) < 3:
            return False, "Ім'я користувача повинно містити мінімум 3 символи"

        if len(password) < 4:
            return False, "Пароль повинен містити мінімум 4 символи"

        try:
            conn = self.get_connection()
            if not conn:
                return False, "Помилка підключення до бази даних"

            cur = conn.cursor()

            # Перевіряємо чи існує користувач з таким ім'ям
            cur.execute("SELECT 1 FROM Users WHERE username = %s", (username.strip(),))
            if cur.fetchone():
                cur.close()
                conn.close()
                return False, "Користувач з таким ім'ям вже існує"

            # Хешуємо пароль та додаємо користувача
            hashed_password = self.hash_password(password)
            cur.execute(
                "INSERT INTO Users (username, password) VALUES (%s, %s) RETURNING user_id",
                (username.strip(), hashed_password)
            )

            user_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()

            return True, f"Користувач '{username}' успішно зареєстрований"

        except psycopg2.IntegrityError:
            return False, "Користувач з таким ім'ям вже існує"
        except psycopg2.Error as e:
            return False, f"Помилка реєстрації: {e}"

    def authenticate_user(self, username, password):
        """Аутентифікація користувача"""
        if not username or not password:
            return False, None, "Ім'я користувача та пароль не можуть бути порожніми"

        try:
            conn = self.get_connection()
            if not conn:
                return False, None, "Помилка підключення до бази даних"

            cur = conn.cursor()
            hashed_password = self.hash_password(password)

            cur.execute(
                "SELECT user_id, username FROM Users WHERE username = %s AND password = %s",
                (username.strip(), hashed_password)
            )

            user = cur.fetchone()
            cur.close()
            conn.close()

            if user:
                return True, user, "Успішний вхід"
            else:
                return False, None, "Невірне ім'я користувача або пароль"

        except psycopg2.Error as e:
            return False, None, f"Помилка аутентифікації: {e}"

    def get_user_by_id(self, user_id):
        """Отримання інформації про користувача за ID"""
        try:
            conn = self.get_connection()
            if not conn:
                return None

            cur = conn.cursor()
            cur.execute(
                "SELECT user_id, username, created_at FROM Users WHERE user_id = %s",
                (user_id,)
            )

            user = cur.fetchone()
            cur.close()
            conn.close()

            return user

        except psycopg2.Error as e:
            print(f"Помилка отримання користувача: {e}")
            return None