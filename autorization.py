
import sys
from PyQt5.QtWidgets import *
from main_project import main_project

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label_username = QLabel('Логін:', self)
        self.textbox_username = QLineEdit(self)

        self.label_password = QLabel('Пароль:', self)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton('Ввійти', self)
        self.button_login.clicked.connect(self.handle_login)

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.textbox_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.textbox_password)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

        self.setWindowTitle('Вхід')
        self.setGeometry(100, 100, 300, 200)

    def handle_login(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()

        if username == 'LosBoyaka' and password == '123456789000':
            QMessageBox.information(self, 'Успішно!', 'Ви ввійшли в систему')
            self.hide()
            main_project()

        else:
            QMessageBox.warning(self, 'Помилка', 'Неправильний логін або пароль')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())