from PyQt5 import QtWidgets, QtGui
import os

class Steganography:
    def __init__(self, parent):
        self.parent = parent
        self.is_encryption_mode = True
        self.encryption_elements = []
        self.decryption_elements = []
        self.initialize_elements()
        self.hide_decryption_elements()
        self.parent.b_switchMode.clicked.connect(self.toggle_mode)

    def initialize_elements(self):
        self.encryption_elements = [
            getattr(self.parent, 'l_enc', None),
            getattr(self.parent, 'b_AddOrigImageEnc', None),
            getattr(self.parent, 'b_deleteOrigProcImageEnc', None),
            getattr(self.parent, 'b_ProcImageEncryptedText', None),
            getattr(self.parent, 'b_SaveProcImageEnc', None),
            getattr(self.parent, 'le_EncryptedText', None),
            getattr(self.parent, 'labelEnd', None),
            getattr(self.parent, 'l_OrigImageEnc', None)
        ]
        self.decryption_elements = [
            getattr(self.parent, 'l_dec', None),
            getattr(self.parent, 'b_AddDecryptImage', None),
            getattr(self.parent, 'b_deleteProcImageDec', None),
            getattr(self.parent, 'l_ProcImageDec', None),
            getattr(self.parent, 'b_ProcImageDecryptedText', None),
            getattr(self.parent, 'te_DecryptedText', None)
        ]
        self.encryption_elements = [elem for elem in self.encryption_elements if elem is not None]
        self.decryption_elements = [elem for elem in self.decryption_elements if elem is not None]
        print("Елем шифрування:", [elem.objectName() for elem in self.encryption_elements])
        print("Елем дешифрування:", [elem.objectName() for elem in self.decryption_elements])

    def hide_decryption_elements(self):
        for element in self.decryption_elements:
            print(f"Ховаємо {element.objectName()}")
            element.setVisible(False)

    def toggle_mode(self):
        print("переключання, is_encryption_mode:", self.is_encryption_mode)
        self.is_encryption_mode = not self.is_encryption_mode
        if self.is_encryption_mode:
            print("Показати елементи шифрування, приховати елементи розшифрування")
            for element in self.encryption_elements:
                print(f"Показуємо {element.objectName()}")
                element.setVisible(True)
            for element in self.decryption_elements:
                print(f"Ховаємо {element.objectName()}")
                element.setVisible(False)
        else:
            for element in self.encryption_elements:
                print(f"Ховаємо {element.objectName()}")
                element.setVisible(False)
            for element in self.decryption_elements:
                print(f"Показуємо {element.objectName()}")
                element.setVisible(True)

# Замість MyMainMenu поставити цей метод в 4 випадках там
def create_main_menu_with_steganography():
    from girlproject.user.main import MyMainMenu

    class MainMenuWithSteganography(MyMainMenu):
        def __init__(self):
            super().__init__()
            self.steganography = Steganography(self)

    return MainMenuWithSteganography()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = create_main_menu_with_steganography()
    window.show()
    sys.exit(app.exec_())
