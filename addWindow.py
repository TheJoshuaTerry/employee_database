from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class addWindow(QDialog) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def initUI(self):
        self.setWindowTitle('Employee Database')
        self.setGeometry(400, 400, 300, 260)

        fNameLabel = QLabel('&First Name:',self)
        fNameLineEdit = QLineEdit(self)
        fNameLabel.setBuddy(fNameLineEdit)

        lNameLabel = QLabel('&Last Name:',self)
        lNameLineEdit = QLineEdit(self)
        lNameLabel.setBuddy(lNameLineEdit)

        ageLabel = QLabel('&age:', self)
        ageLineEdit = QLineEdit(self)
        ageLabel.setBuddy(ageLineEdit)

        addressLabel = QLabel('&Address:', self)
        addressLineEdit = QLineEdit(self)
        addressLabel.setBuddy(addressLineEdit)

        phoneLabel = QLabel('&Phone:', self)
        phoneLineEdit = QLineEdit(self)
        phoneLabel.setBuddy(phoneLineEdit)

        emailLabel = QLabel('&Email:', self)
        emailLineEdit = QLineEdit(self)
        emailLabel.setBuddy(emailLineEdit)

        deptLabel = QLabel('&Department:', self)
        deptLineEdit = QLineEdit(self)
        deptLabel.setBuddy(deptLineEdit)

        salaryLabel = QLabel('&Salary:', self)
        salaryLineEdit = QLineEdit(self)
        salaryLabel.setBuddy(salaryLineEdit)

        btnOK = QPushButton('&Submit')
        btnCancel = self.closeButton = QPushButton(self)
        self.closeButton.setText("Cancel")  # text
        self.closeButton.setShortcut('Ctrl+D')  # shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget")  # Tool tip
        self.closeButton.move(100, 100)

        mainLayout = QGridLayout(self)

        mainLayout.addWidget(fNameLabel,0,0)
        mainLayout.addWidget(fNameLineEdit,0,1,1,2)

        mainLayout.addWidget(lNameLabel,1,0)
        mainLayout.addWidget(lNameLineEdit,1,1,1,2)

        mainLayout.addWidget(ageLabel, 2, 0)
        mainLayout.addWidget(ageLineEdit, 2, 1, 1, 2)

        mainLayout.addWidget(addressLabel, 3, 0)
        mainLayout.addWidget(addressLineEdit, 3, 1, 1, 2)

        mainLayout.addWidget(phoneLabel, 4, 0)
        mainLayout.addWidget(phoneLineEdit, 4, 1, 1, 2)

        mainLayout.addWidget(emailLabel, 5, 0)
        mainLayout.addWidget(emailLineEdit, 5, 1, 1, 2)

        mainLayout.addWidget(deptLabel, 6, 0)
        mainLayout.addWidget(deptLineEdit, 6, 1, 1, 2)

        mainLayout.addWidget(salaryLabel, 7, 0)
        mainLayout.addWidget(salaryLineEdit, 7, 1, 1, 2)

        mainLayout.addWidget(btnOK,8,1)
        mainLayout.addWidget(btnCancel,8,2)


app = QApplication(sys.argv)
main = addWindow()
main.show()
sys.exit(app.exec_())