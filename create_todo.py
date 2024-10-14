from PyQt6.QtWidgets import (
    QWidget,QVBoxLayout, QMessageBox, QLabel, QLineEdit, QCheckBox,
    QPushButton
)
from PyQt6.QtSql import QSqlQuery
class TodoForm(QWidget):
    def __init__(self, onsubmit_todo_callback):
        super().__init__()
        layout= QVBoxLayout(self)
        self.onsubmit_todo_callback= onsubmit_todo_callback
        #name input
        self.name_lable= QLabel('Todo Name: ')
        layout.addWidget(self.name_lable)
        
        self.name_input= QLineEdit(self)
        layout.addWidget(self.name_input)

        #completed input
        self.completed_lable= QLabel('Completed? ')
        layout.addWidget(self.completed_lable)

        self.completed_checkbox= QCheckBox()
        layout.addWidget(self.completed_checkbox)

        #submit button
        self.submit_button= QPushButton("Submit", self)
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.submit_todo)

        #set the layout
        self.setLayout(layout)
    def submit_todo(self):
        name= self.name_input.text()
        completed= self.completed_checkbox.isChecked()
        if name:
            query= QSqlQuery()
            query.prepare('INSERT INTO todos (name, completed) VALUES (?, ?)')
            query.addBindValue(name)
            query.addBindValue(completed)
            ok= query.exec()
            if ok:
                self.onsubmit_todo_callback(name, completed)

                #Provide the user feedback
                QMessageBox.information(self, "Success", "Todo added successfully")
                self.name_input.clear()
                self.completed_checkbox.setChecked(False)
            else:
                QMessageBox.warning(self, "Error validation", "Ooops Something went wrong, Please try again")
        else:
            QMessageBox.warning(self, "Error validation", "Name is a required field!")