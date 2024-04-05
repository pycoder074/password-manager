from PyQt6.QtWidgets import QDialog, QFormLayout, QPushButton
from Entries import Entry
from save_gen_passwrd import save_gen_passwrd
from encryption import encrypt
class addInfo(QDialog):
    def __init__(self, passwrd, parent = None):
        super().__init__()
        self.passwrd = passwrd
        self.parent = parent
        self.setWindowTitle('Add Extra Info')

        layout = QFormLayout()
        self.setLayout(layout)

        self.website = Entry.InfoEntry('Website')
        layout.addWidget(self.website)

        self.username = Entry.InfoEntry('Username: ')
        layout.addWidget(self.username)

        save_btn = QPushButton('Save Information')
        save_btn.clicked.connect(self.save_data)
        layout.addWidget(save_btn)

    def return_data(self):
        data = {
            'website' : self.website.get_value(),
            'username' : self.username.get_value(),
            'password' : self.passwrd
        }
        return data

    def save_data(self):
        data = self.return_data()
        username = encrypt(data['username'])
        password = encrypt(data['password'])
        website = encrypt(data['website'])
        save_gen_passwrd(password, website, username)
        print('Information saved')
        self.close()
        self.parent.close()