import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from create_todo import TodoForm
from db import open_connection
from todos_table import TodoTable

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To-Do Appication')
        #central widget and layout
        central_widget= QWidget()
        layout= QVBoxLayout(central_widget)

        self.todo_form= TodoForm(self.add_todo_to_table)
        layout.addWidget(self.todo_form)

        self.todo_table= TodoTable()
        layout.addWidget(self.todo_table)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_todo_to_table(self, name, completed):
        self.todo_table.add_todo_item(name, completed)
    
app= QApplication([])
if not open_connection():
    sys.exit(1)
window= MainWindow()
window.show()
app.exec()