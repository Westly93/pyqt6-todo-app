from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtSql import QSqlQuery
class TodoTable(QWidget):
    def __init__(self):
        super().__init__()
        layout= QVBoxLayout()
        

        #table widget
        self.todo_table= QTableWidget()
        self.todo_table.setColumnCount(2)
        self.todo_table.setHorizontalHeaderLabels(
            ['Todo Name', "Completed?"]
        )

        layout.addWidget(self.todo_table)

        self.setLayout(layout)

        self.get_todos()
    def get_todos(self):
        query= QSqlQuery()
        query.exec('SELECT name, completed FROM todos')

        while query.next():
            rows= self.todo_table.rowCount()
            self.todo_table.setRowCount(rows + 1)
            self.todo_table.setItem(rows, 0, QTableWidgetItem(query.value(0)))
            status= 'completed' if query.value(1) else 'pending'
            self.todo_table.setItem(rows, 1, QTableWidgetItem(status))
    def add_todo_item(self, name, completed):
        #determine the current row and insert a new row
        row_position= self.todo_table.rowCount()
        self.todo_table.insertRow(row_position)

        #add todo name in the first column
        self.todo_table.setItem(row_position, 0, QTableWidgetItem(name))

        status= 'completed' if completed else 'pending'
        self.todo_table.setItem(row_position, 1, QTableWidgetItem(status))
